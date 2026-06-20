"""
mock_data.py — CoinScanner Static Exchange Data
=================================================
This file stores all the static data about crypto exchanges
used on the Compare Exchanges page (/compare).

WHY "MOCK" DATA?
  Exchange details (fees, features, leverage) don't change daily.
  We store them here as Python dicts rather than in a database
  or calling an API. This makes them:
    - Fast (no DB query or API call needed)
    - Easy to update (just edit this file)
    - Easy to read and understand

LOGO URLS:
  We use Google Favicons API with sz=128 for reliable, high-res logos.
  Works without DNS restrictions: https://www.google.com/s2/favicons?domain={domain}&sz=128

HOW IT'S USED:
  In app.py:
    import mock_data as data
    exchanges = data.get_exchanges()
    insights  = data.get_insights()

  Passed to compare.html via render_template().

ADDING A NEW EXCHANGE:
  Copy any existing exchange dict and fill in the fields.
  Make sure the 'id' field is lowercase with no spaces.
  The logo URL should be: "https://www.google.com/s2/favicons?domain={exchange-domain}&sz=128"

TODO:
  When you have more exchanges, consider moving this to a database
  table so non-developers can update it without touching code.
"""


def get_exchanges():
    """
    Return a list of all exchanges with their details.

    Each exchange is a dict with these keys:
      id          — unique identifier, used in JS data-id attributes
      name        — display name
      logo        — URL to the exchange logo (Google Favicons API)
      about       — dict: founded, headquarters, founders, regulated, website, description
      fees        — dict: spot, futures trading fees
      leverage    — maximum leverage offered (string, e.g. "20x")
      usp1        — Unique Selling Point 1 (short, e.g. "Zero Maker Fee")
      usp2        — Unique Selling Point 2 (short, e.g. "Instant INR Withdrawal")
      withdrawal  — dict: limit (minimum), charges (fee per withdrawal)
      deposit     — dict: limit (minimum), charges (fee)
      currencies  — number of coins supported (string, e.g. "500+")
      earning     — earning options like "Staking, Refer"
      mining      — mining options or "-" if not supported
      referral_link — affiliate/signup link for the exchange (empty string if not available)
      features    — dict of boolean flags:
                      spot             → spot trading
                      investment       → SIP / passive investing
                      derivatives_fno  → futures and options
                      p2p              → peer-to-peer trading
                      inr_support      → Indian Rupee deposit/withdrawal

    Returns:
        list[dict] — list of exchange dicts
    """
    return [

        # ── INDIAN EXCHANGES ──────────────────────────────

        {
            "id":   "coindcx",
            "name": "CoinDCX",
            # Google Favicons with sz=128 — reliable, no DNS issues
            "logo": "https://img.icons8.com/color/96/coindcx.png",
            "about": {
                "founded":       "2018",
                "headquarters":  "Mumbai, India",
                "founders":      "Sumit Gupta, Neeraj Khandelwal",
                "regulated":     "FIU-IND Registered",
                "website":       "https://coindcx.com",
                "description":   "India's largest crypto exchange by volume, offering spot, futures, and staking with full INR support via UPI and bank transfer.",
            },
            "fees": {
                "spot":    "0.03% – 0.50%",
                "futures": "0.03% – 0.05%",
            },
            "leverage":   "20x",
            "usp1":       "Zero Maker Fee",
            "usp2":       "Instant INR Withdrawal",
            "withdrawal": {"limit": "₹100",  "charges": "₹0"},
            "deposit":    {"limit": "₹100",  "charges": "₹0"},
            "currencies": "500+",
            "earning":    "Staking, Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      True,
                "derivatives_fno": True,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "wazirx",
            "name": "WazirX",
            "logo": "https://www.google.com/s2/favicons?domain=wazirx.com&sz=128",
            "about": {
                "founded":       "2018",
                "headquarters":  "Mumbai, India",
                "founders":      "Nischal Shetty, Siddharth Menon, Sameer Mhatre",
                "regulated":     "FIU-IND Registered",
                "website":       "https://wazirx.com",
                "description":   "One of India's oldest crypto exchanges, known for its simple UI and WRX token ecosystem.",
            },
            "fees": {
                "spot":    "0.10% – 0.40% / ₹99 pm",
                "futures": "-",
            },
            "leverage":   "-",
            "usp1":       "WRX Token Rewards",
            "usp2":       "Zero Deposit Fee",
            "withdrawal": {"limit": "₹500", "charges": "₹10 (Instant)"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "250+",
            "earning":    "Staking, Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      False,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "zebpay",
            "name": "ZebPay",
            "logo": "https://www.google.com/s2/favicons?domain=zebpay.com&sz=128",
            "about": {
                "founded":       "2014",
                "headquarters":  "Singapore (India ops)",
                "founders":      "Saurabh Agarwal, Sandeep Goenka, Mahin Gupta",
                "regulated":     "FIU-IND Registered",
                "website":       "https://zebpay.com",
                "description":   "One of India's first crypto exchanges, now operating globally with a focus on security and compliance.",
            },
            "fees": {
                "spot":    "0.03% – 0.45%",
                "futures": "0.029% – 0.020%",
            },
            "leverage":   "75x",
            "usp1":       "India's Pioneer Exchange",
            "usp2":       "Global Operations & Compliance",
            "withdrawal": {"limit": "₹100", "charges": "₹15"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "400+",
            "earning":    "Staking, Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      True,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "coinswitch",
            "name": "CoinSwitch",
            "logo": "https://www.google.com/s2/favicons?domain=coinswitch.co&sz=128",
            "about": {
                "founded":       "2017",
                "headquarters":  "Bengaluru, India",
                "founders":      "Ashish Singhal, Govind Soni, Vimal Sagar",
                "regulated":     "FIU-IND Registered",
                "website":       "https://coinswitch.co",
                "description":   "India's most downloaded crypto app, focused on retail investors with a simple SIP-style investing experience.",
            },
            "fees": {
                "spot":    "0.1% – 0.5%",
                "futures": "0.015%",
            },
            "leverage":   "50x",
            "usp1":       "Most Downloaded Crypto App",
            "usp2":       "SIP-Style Crypto Investing",
            "withdrawal": {"limit": "₹100", "charges": "₹0"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "100+",
            "earning":    "Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      True,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "mudrex",
            "name": "Mudrex",
            "logo": "https://www.google.com/s2/favicons?domain=mudrex.com&sz=128",
            "about": {
                "founded":       "2019",
                "headquarters":  "San Francisco, USA / India",
                "founders":      "Edul Patel, Alankar Saxena",
                "regulated":     "FIU-IND Registered",
                "website":       "https://mudrex.com",
                "description":   "Crypto investment platform offering coin sets, algo trading, and automated strategies for passive investors.",
            },
            "fees": {
                "spot":    "0.12% – 0.45%",
                "futures": "0.03% – 0.05%",
            },
            "leverage":   "100x",
            "usp1":       "Algo Trading & Coin Sets",
            "usp2":       "650+ Coins, Zero Trade Fee",
            "withdrawal": {"limit": "5 USDT",  "charges": "0–1% + 1% TDS"},
            "deposit":    {"limit": "₹100",    "charges": "₹0"},
            "currencies": "650+",
            "earning":    "Staking, Refer",
            "mining":     "-",
            "referral_link": "https://mudrex.go.link/84KZD",
            "features": {
                "spot":            False,
                "investment":      True,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "unocoin",
            "name": "Unocoin",
            "logo": "https://www.google.com/s2/favicons?domain=unocoin.com&sz=128",
            "about": {
                "founded":       "2013",
                "headquarters":  "Bengaluru, India",
                "founders":      "Sathvik Vishwanath, Harish BV, Abhinand Kaseti, Sunny Ray",
                "regulated":     "FIU-IND Registered",
                "website":       "https://unocoin.com",
                "description":   "India's oldest crypto company, primarily focused on Bitcoin with SIP and OTC services for long-term holders.",
            },
            "fees": {
                "spot":    "-",
                "futures": "-",
            },
            "leverage":   "-",
            "usp1":       "India's Oldest Crypto Company",
            "usp2":       "Bitcoin SIP from ₹100",
            "withdrawal": {"limit": "0.001 BTC", "charges": "Network fees"},
            "deposit":    {"limit": "₹100",      "charges": "₹0"},
            "currencies": "50+",
            "earning":    "-",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      True,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "bitbns",
            "name": "Bitbns",
            "logo": "https://www.google.com/s2/favicons?domain=bitbns.com&sz=128",
            "about": {
                "founded":       "2017",
                "headquarters":  "Bengaluru, India",
                "founders":      "Gaurav Dahake",
                "regulated":     "FIU-IND Registered",
                "website":       "https://bitbns.com",
                "description":   "Indian exchange known for fixed deposit crypto products and a wide range of altcoins with INR pairs.",
            },
            "fees": {
                "spot":    "0.25% – 0.03%",
                "futures": "0.1% (Futures only)",
            },
            "leverage":   "4x",
            "usp1":       "Crypto Fixed Deposit Plans",
            "usp2":       "Wide Altcoin INR Pairs",
            "withdrawal": {"limit": "₹100", "charges": "₹0"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "100+",
            "earning":    "Fixed Deposits, Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      False,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "giottus",
            "name": "Giottus",
            "logo": "https://www.google.com/s2/favicons?domain=giottus.com&sz=128",
            "about": {
                "founded":       "2018",
                "headquarters":  "Chennai, India",
                "founders":      "Vikram Subburaj, Arjun Vijay",
                "regulated":     "FIU-IND Registered",
                "website":       "https://giottus.com",
                "description":   "South India's leading crypto exchange with lending, staking, and a strong focus on customer support.",
            },
            "fees": {
                "spot":    "0.05% – 0.4%",
                "futures": "0.008% – 0.048%",
            },
            "leverage":   "50x",
            "usp1":       "South India's Leading Exchange",
            "usp2":       "Crypto Lending & Staking",
            "withdrawal": {"limit": "₹100", "charges": "₹0"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "350+",
            "earning":    "Staking, Refer, Lend",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      False,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "pi42",
            "name": "Pi42",
            "logo": "https://www.google.com/s2/favicons?domain=pi42.com&sz=128",
            "about": {
                "founded":       "2023",
                "headquarters":  "Delhi, India",
                "founders":      "Avinash Shekhar",
                "regulated":     "FIU-IND Registered",
                "website":       "https://pi42.com",
                "description":   "India's newest crypto futures exchange offering INR-margined contracts — no USDT needed. Zero conversion fees.",
            },
            "fees": {
                "spot":    "0.02% – 0.029%",
                "futures": "0.0127% – 0.0169%",
            },
            "leverage":   "150x",
            "usp1":       "INR-Margined Futures — No USDT",
            "usp2":       "Zero Conversion Fees",
            "withdrawal": {"limit": "₹100", "charges": "₹0"},
            "deposit":    {"limit": "₹100", "charges": "₹0"},
            "currencies": "500+",
            "earning":    "Refer",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            False,
                "investment":      False,
                "derivatives_fno": True,
                "p2p":             False,
                "inr_support":     True,
            },
        },

        {
            "id":   "delta",
            "name": "Delta Exchange",
            "logo": "https://www.google.com/s2/favicons?domain=delta.exchange&sz=128",
            "about": {
                "founded":       "2018",
                "headquarters":  "Bengaluru, India",
                "founders":      "Pankaj Balani, Abhishek Malhotra",
                "regulated":     "FIU-IND Registered",
                "website":       "https://delta.exchange",
                "description":   "India's leading crypto derivatives platform, built for serious traders with advanced order types and deep futures liquidity.",
            },
            "fees": {
                "spot":    "0.05% – 0.02%",
                "futures": "0.01% – 0.02%",
            },
            "leverage":   "50x",
            "usp1":       "Advanced Order Types",
            "usp2":       "Deep Futures Liquidity",
            "withdrawal": {"limit": "₹500", "charges": "₹0"},
            "deposit":    {"limit": "₹1",   "charges": "₹0"},
            "currencies": "150+",
            "earning":    "Staking, Refer",
            "mining":     "-",
            "referral_link": "https://www.delta.exchange/?code=CDXTHS",
            "features": {
                "spot":            False,
                "investment":      False,
                "derivatives_fno": True,
                "p2p":             False,
                "inr_support":     False,
            },
        },

        # ── GLOBAL EXCHANGES ─────────────────────────────

        {
            "id":   "coinbase",
            "name": "Coinbase",
            "logo": "https://www.google.com/s2/favicons?domain=coinbase.com&sz=128",
            "about": {
                "founded":       "2012",
                "headquarters":  "San Francisco, USA",
                "founders":      "Brian Armstrong, Fred Ehrsam",
                "regulated":     "SEC Registered, FinCEN MSB, NASDAQ Listed",
                "website":       "https://coinbase.com",
                "description":   "World's most trusted crypto exchange, publicly listed on NASDAQ. Best for beginners with a clean UI and strong compliance.",
            },
            "fees": {
                "spot":    "0.05% – 0.6%",
                "futures": "-",
            },
            "leverage":   "-",
            "usp1":       "NASDAQ-Listed, Insured Wallets",
            "usp2":       "Beginner-Friendly Interface",
            "withdrawal": {"limit": "No min", "charges": "Network fee"},
            "deposit":    {"limit": "No min", "charges": "₹0"},
            "currencies": "150+",
            "earning":    "Staking, Rewards",
            "mining":     "-",
            "referral_link": "",
            "features": {
                "spot":            True,
                "investment":      True,
                "derivatives_fno": False,
                "p2p":             False,
                "inr_support":     False,
            },
        },

        {
            "id":   "kucoin",
            "name": "KuCoin",
            "logo": "https://www.google.com/s2/favicons?domain=kucoin.com&sz=128",
            "about": {
                "founded":       "2017",
                "headquarters":  "Seychelles",
                "founders":      "Michael Gan, Eric Don, Top Lan, Kent Li",
                "regulated":     "Seychelles FSA",
                "website":       "https://kucoin.com",
                "description":   "Known as the 'People's Exchange', KuCoin offers 1200+ coins, lending, mining, and one of the widest altcoin selections.",
            },
            "fees": {
                "spot":    "0.005% – 0.165%",
                "futures": "0.006% / 0.048%",
            },
            "leverage":   "125x",
            "usp1":       "1,200+ Altcoins Available",
            "usp2":       "Built-in Lending & Mining",
            "withdrawal": {"limit": "P2P",  "charges": "₹0"},
            "deposit":    {"limit": "P2P",  "charges": "₹0"},
            "currencies": "1,200+",
            "earning":    "Staking, Lend",
            "mining":     "KuMining",
            "referral_link": "https://www.kucoin.com/r/broker/CXEBKDY1",
            "features": {
                "spot":            True,
                "investment":      False,
                "derivatives_fno": True,
                "p2p":             True,
                "inr_support":     False,
            },
        },

        {
            "id":   "bybit",
            "name": "Bybit",
            "logo": "https://www.google.com/s2/favicons?domain=bybit.com&sz=128",
            "about": {
                "founded":       "2018",
                "headquarters":  "Dubai, UAE",
                "founders":      "Ben Zhou",
                "regulated":     "Dubai VARA Licensed",
                "website":       "https://bybit.com",
                "description":   "World's 2nd largest crypto derivatives exchange. Preferred by professional traders for low fees and deep liquidity.",
            },
            "fees": {
                "spot":    "0.045% – 0.1%",
                "futures": "0.03% – 0.02%",
            },
            "leverage":   "100x",
            "usp1":       "World's 2nd Largest Derivatives",
            "usp2":       "2,400+ Coins & Liquidity Mining",
            "withdrawal": {"limit": "Crypto only", "charges": "₹0"},
            "deposit":    {"limit": "Crypto only", "charges": "₹0"},
            "currencies": "2,400+",
            "earning":    "Staking, Refer",
            "mining":     "Liquidity Mining",
            "referral_link": "",
            "features": {
                "spot":            False,
                "investment":      False,
                "derivatives_fno": True,
                "p2p":             False,
                "inr_support":     False,
            },
        },

        {
            "id":   "binance",
            "name": "Binance",
            "logo": "https://www.google.com/s2/favicons?domain=binance.com&sz=128",
            "about": {
                "founded":       "2017",
                "headquarters":  "Cayman Islands (Global)",
                "founders":      "Changpeng Zhao (CZ)",
                "regulated":     "Multiple jurisdictions (VASP registered)",
                "website":       "https://binance.com",
                "description":   "World's largest crypto exchange by volume. Offers the most comprehensive product suite — spot, futures, P2P, mining, staking, NFTs.",
            },
            "fees": {
                "spot":    "0.023% – 0.10%",
                "futures": "0.024%",
            },
            "leverage":   "150x",
            "usp1":       "World's Largest Crypto Exchange",
            "usp2":       "Spot, Futures, P2P & NFTs",
            "withdrawal": {"limit": "P2P",  "charges": "₹0"},
            "deposit":    {"limit": "P2P",  "charges": "₹0"},
            "currencies": "600+",
            "earning":    "Staking, Learn & Earn, Refer",
            "mining":     "Mining Pool",
            "features": {
                "spot":            True,
                "investment":      False,
                "derivatives_fno": True,
                "p2p":             True,
                "inr_support":     False,
            },
        },

    ]


def get_insights():
    """
    Return a list of insight cards shown at the top of the compare page.

    Each insight highlights a specific exchange for a notable trait.
    Type can be: "good" (green), "bad" (red), "neutral" (yellow).

    Returns:
        list[dict] — list of insight cards
    """
    return [
        {
            "type":     "good",
            "title":    "Cheapest Overall",
            "exchange": "Binance",
            "desc":     "Lowest Fees Overall",
            "sub":      "Average 0.10% Trading Fee",
        },
        {
            "type":     "bad",
            "title":    "Watch Out",
            "exchange": "WazirX",
            "desc":     "Monthly Subscription Model",
            "sub":      "₹99/month fee on some plans",
        },
        {
            "type":     "neutral",
            "title":    "Best for Beginners",
            "exchange": "Coinbase",
            "desc":     "Easiest to Use",
            "sub":      "Simple UI & 24/7 support",
        },
    ]


def get_wallets():
    """
    Return a list of popular crypto wallets.
    Currently unused in templates but available for future wallet comparison page.

    Returns:
        list[dict] — list of wallet dicts
    """
    return [
        {
            "id":               "metamask",
            "name":             "MetaMask",
            "type":             "software",
            "custody":          "non-custodial",
            "platforms":        ["Browser", "iOS", "Android"],
            "supported_chains": ["Ethereum", "BNB", "Polygon", "Arbitrum"],
            "fees":             "Network fees only",
            "best_for":         "DeFi & Web3 users",
            "security_level":   "Medium",
            "beginner_friendly": True,
            "details": {
                "recovery":         "12-word seed phrase",
                "open_source":      True,
                "hardware_support": ["Ledger", "Trezor"],
                "notes":            "Popular but phishing-prone if user is careless",
            },
        },
        {
            "id":               "ledger",
            "name":             "Ledger Nano X",
            "type":             "hardware",
            "custody":          "non-custodial",
            "platforms":        ["Hardware", "Desktop", "Mobile"],
            "supported_chains": ["Bitcoin", "Ethereum", "Solana", "1000+ tokens"],
            "fees":             "One-time device cost",
            "best_for":         "Long-term holders",
            "security_level":   "Very High",
            "beginner_friendly": False,
            "details": {
                "recovery":        "24-word seed phrase",
                "secure_element":  True,
                "bluetooth":       True,
                "notes":           "Top-tier security, some learning curve",
            },
        },
    ]