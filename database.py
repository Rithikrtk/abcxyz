"""
database.py — CoinScanner Database Layer
==========================================
Supports both local SQLite and AWS RDS / Aurora PostgreSQL.

The app uses the same query style in both modes. This module
translates `?` placeholders to `%s` when PostgreSQL is enabled.
"""

import os
import sqlite3


DB_PATH = os.path.join(os.path.dirname(__file__), "coinscanner.db")
# Use DATABASE_URL for production Postgres. Leave empty to use local SQLite.
DATABASE_URL = os.environ.get("DATABASE_URL") or ""


def _use_postgres():
    return DATABASE_URL.startswith(("postgres://", "postgresql://"))


def _translate_sql(sql):
    """
    Canonicalize SQL parameter style.
    The codebase will use Postgres-style `%s` placeholders. When running
    against SQLite (local dev), translate `%s` -> `?` so sqlite3 accepts it.
    """
    if _use_postgres():
        return sql
    # sqlite's paramstyle is qmark (?), so convert %s -> ? for SQLite
    return sql.replace("%s", "?")


class _CursorWrapper:
    def __init__(self, cursor):
        self._cursor = cursor

    def execute(self, sql, params=()):
        self._cursor.execute(_translate_sql(sql), params)
        return self

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    def close(self):
        return self._cursor.close()

    def __iter__(self):
        return iter(self._cursor)

    def __getattr__(self, name):
        return getattr(self._cursor, name)


class _ConnectionWrapper:
    def __init__(self, connection):
        self._connection = connection

    def cursor(self):
        if _use_postgres():
            from psycopg2.extras import RealDictCursor

            return _CursorWrapper(self._connection.cursor(cursor_factory=RealDictCursor))
        return _CursorWrapper(self._connection.cursor())

    def execute(self, sql, params=()):
        return self.cursor().execute(sql, params)

    def commit(self):
        return self._connection.commit()

    def rollback(self):
        return self._connection.rollback()

    def close(self):
        return self._connection.close()

    def __getattr__(self, name):
        return getattr(self._connection, name)


def _connect_native():
    if _use_postgres():
        import psycopg2
        # Allow optional SSL mode via environment (useful for managed DBs)
        sslmode = os.environ.get("PG_SSLMODE") or os.environ.get("PGSSLMODE")
        try:
            if sslmode:
                return psycopg2.connect(DATABASE_URL, sslmode=sslmode)
            return psycopg2.connect(DATABASE_URL)
        except Exception:
            # Reraise to let app startup fail loudly in production
            raise

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_db_connection():
    """Return a DB-API-like connection for the active backend."""
    return _ConnectionWrapper(_connect_native())


def init_db():
    """Create tables and run lightweight migrations if needed."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if _use_postgres():
        users_ddl = """
        CREATE TABLE IF NOT EXISTS users (
            id                 SERIAL PRIMARY KEY,
            name               TEXT    NOT NULL,
            email              TEXT    UNIQUE NOT NULL,
            phone              TEXT    UNIQUE,
            password_hash      TEXT    NOT NULL,
            is_verified        INTEGER DEFAULT 0,
            email_verified     INTEGER DEFAULT 0,
            phone_verified     INTEGER DEFAULT 0,
            otp_code           TEXT,
            otp_expiry         INTEGER,
            email_otp          TEXT,
            email_otp_expiry   INTEGER,
            phone_otp          TEXT,
            phone_otp_expiry   INTEGER,
            failed_attempts    INTEGER DEFAULT 0,
            locked_until       INTEGER DEFAULT 0,
            session_version    INTEGER DEFAULT 0,
            created_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        coin_watchlist_ddl = """
        CREATE TABLE IF NOT EXISTS coin_watchlist (
            id          SERIAL PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            coin_id     TEXT    NOT NULL,
            coin_name   TEXT    NOT NULL,
            coin_symbol TEXT    NOT NULL,
            coin_image  TEXT    DEFAULT '',
            added_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, coin_id),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
        exchange_watchlist_ddl = """
        CREATE TABLE IF NOT EXISTS exchange_watchlist (
            id            SERIAL PRIMARY KEY,
            user_id       INTEGER NOT NULL,
            exchange_id   TEXT    NOT NULL,
            exchange_name TEXT    NOT NULL,
            exchange_logo TEXT    DEFAULT '',
            added_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, exchange_id),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
        login_log_ddl = """
        CREATE TABLE IF NOT EXISTS login_log (
            id         SERIAL PRIMARY KEY,
            ip         TEXT,
            identifier TEXT,
            success    INTEGER DEFAULT 0,
            reason     TEXT,
            timestamp  INTEGER
        )
        """
    else:
        users_ddl = """
        CREATE TABLE IF NOT EXISTS users (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            name               TEXT    NOT NULL,
            email              TEXT    UNIQUE NOT NULL,
            phone              TEXT    UNIQUE,
            password_hash      TEXT    NOT NULL,
            is_verified        INTEGER DEFAULT 0,
            email_verified     INTEGER DEFAULT 0,
            phone_verified     INTEGER DEFAULT 0,
            otp_code           TEXT,
            otp_expiry         INTEGER,
            email_otp          TEXT,
            email_otp_expiry   INTEGER,
            phone_otp          TEXT,
            phone_otp_expiry   INTEGER,
            failed_attempts    INTEGER DEFAULT 0,
            locked_until       INTEGER DEFAULT 0,
            session_version    INTEGER DEFAULT 0,
            created_at         DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        coin_watchlist_ddl = """
        CREATE TABLE IF NOT EXISTS coin_watchlist (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            coin_id     TEXT    NOT NULL,
            coin_name   TEXT    NOT NULL,
            coin_symbol TEXT    NOT NULL,
            coin_image  TEXT    DEFAULT '',
            added_at    DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, coin_id),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
        exchange_watchlist_ddl = """
        CREATE TABLE IF NOT EXISTS exchange_watchlist (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id       INTEGER NOT NULL,
            exchange_id   TEXT    NOT NULL,
            exchange_name TEXT    NOT NULL,
            exchange_logo TEXT    DEFAULT '',
            added_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, exchange_id),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
        login_log_ddl = """
        CREATE TABLE IF NOT EXISTS login_log (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            ip         TEXT,
            identifier TEXT,
            success    INTEGER DEFAULT 0,
            reason     TEXT,
            timestamp  INTEGER
        )
        """

    cursor.execute(users_ddl)

    new_columns = [
        ("failed_attempts",  "INTEGER DEFAULT 0"),
        ("locked_until",     "INTEGER DEFAULT 0"),
        ("session_version",  "INTEGER DEFAULT 0"),
        ("email_verified",   "INTEGER DEFAULT 0"),
        ("phone_verified",   "INTEGER DEFAULT 0"),
        ("email_otp",        "TEXT"),
        ("email_otp_expiry", "INTEGER"),
        ("phone_otp",        "TEXT"),
        ("phone_otp_expiry", "INTEGER"),
    ]
    for col_name, col_def in new_columns:
        try:
            if _use_postgres():
                cursor.execute(f"ALTER TABLE users ADD COLUMN IF NOT EXISTS {col_name} {col_def}")
            else:
                cursor.execute(f"ALTER TABLE users ADD COLUMN {col_name} {col_def}")
            conn.commit()
        except Exception:
            try:
                conn.rollback()
            except Exception:
                pass

    cursor.execute(coin_watchlist_ddl)
    cursor.execute(exchange_watchlist_ddl)
    cursor.execute(login_log_ddl)

    conn.commit()
    conn.close()


def purge_old_logs(days=90):
    """Delete login_log entries older than `days` days."""
    cutoff = int(__import__('time').time()) - (days * 86400)
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM login_log WHERE timestamp < %s", (cutoff,))
        conn.commit()
    except Exception:
        try:
            conn.rollback()
        except Exception:
            pass
    finally:
        conn.close()
