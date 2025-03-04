BETTING_PROVIDERS = [
    'DraftKings',
    'SugarHouse',
    'Caesars Sportsbook (New Jersey)',
    'PointsBet',
    'Caesars Sportsbook (Colorado)',
    'Holland Casino',
    'Caesars Sportsbook (Tennessee)',
    'FanDuel',
    'Unibet',
    'Bet365',
    "Betradar"
]

DEFAULT_BETTING_PROVIDERS_MAP = {
    'mlb': 'Unibet',
    'nfl': 'Betradar',
    'nba': 'Betrader',
    'mcbb': 'Betrader',
    'cfb': 'Betrader',
    'wnba': 'Betrader',
}

LEAGUE_DIVISION_FUTURES_MAPPING = {
    'nfl': {
        'afc west': 'Pro Football (A) West Division - Winner',
        'afc north': 'Pro Football (A) North Division - Winner',
        'afc south': 'Pro Football (A) South Division - Winner',
        'afc east': 'Pro Football (A) East  Division - Winner',
        'afc': 'Pro Football (A) Conference Winner',
        'nfc west': 'Pro Football (N) West Division - Winner',
        'nfc north': 'Pro Football (N) North Division - Winner',
        'nfc south': 'Pro Football (N) South Division - Winner',
        'nfc east': 'Pro Football (N) East  Division - Winner',
        'nfc conf': 'Pro Football (N) Conference Winner'
    },
    'nba': {
        'east': 'NBA - Eastern Conference - Winner',
        'west': 'NBA - Western Conference - Winner'
    },
    'cfb': {
        'big12': 'NCAA(F) - Big 12 Conference',
        'big10': 'NCAA(F) - Big Ten Conference',
        'big10 east': 'NCAA(F) - Big Ten Conference - East Division - Winner (reg. season)',
        'big10 west': 'NCAA(F) - Big Ten Conference - West Division - Winner (reg. season)',
        'acc': 'NCAA(F) - Atlantic Coast Conference',
        'aac': 'NCAA(F) - American Athletic Conference',
        'usa': 'NCAA(F) - Conference USA',
        'mid-am': 'NCAA(F) - Mid-American Conference',
        'mid-am east': 'NCAA(F) - Conference - Mid-American - Division East',
        'mid-am west': 'NCAA(F) - Conference - Mid-American - Division West',
        'mt west': 'NCAA(F) - Mountain West Conference',
        'pac12': 'NCAA(F) - Pacific-12 Conference',
        'sec': 'NCAA(F) - Southeastern Conference',
        'sec west': 'NCAA(F) - Southeastern Conference - West Division - Winner (reg. season)',
        'sec east': 'NCAA(F) - Southeastern Conference - East Division - Winner (reg. season)',
        'sun belt': 'Sun Belt Conference Champion',
    },
    'mcbb': {
        'mwc': 'NCAA(B) - Mountain West Conference - Winner (reg. season)',
        'final four': 'NCAA(B) - To Make The Final 4',
        'big12': 'NCAA(B) - Big 12 Conference - Winner (reg. season)',
        'acc': 'NCAA(B) - Atlantic Coast Conference - Winner (reg. season)',
        'sec': 'NCAA(B) - Southeastern Conference - Winner (reg. season)',
        'big10': 'NCAA(B) - Big Ten Conference - Winner (reg. season)',
        'big east': 'NCAA(B) - Big East Conference - Winner (reg. season',

    },
    'mlb': {
        'nl': 'MLB - National League - Winner',
        'al': 'MLB - American League - Winner',
        'nl west': 'MLB - National League West',
        'nl east': 'MLB - National League East',
        'nl central': 'MLB - National League Central',
        'al west': 'MLB - American League West',
        'al east': 'MLB - American League East',
        'al central': 'MLB - American League Central',
        'all star': 'MLB - Winning League',

    }
}

LEAGUE_CHAMPION_FUTURES_MAP = {
    'nfl': 'NFL - Super Bowl Winner',
    'nba': 'NBA - Winner',
    'cfb': 'NCAA(F) - Championship',
    'mcbb': 'NCAA(B) - Winner',
    'wnba': 'WNBA - Winner',
    'mlb': 'MLB  - World Series - Winner'
}

BETTING_AVAILABLE = [
    'nfl', 'nba', 'wnba', 'mcbb', 'cfb', 'mlb'
]
