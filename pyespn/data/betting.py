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
    }
}

LEAGUE_CHAMPION_FUTURES_MAP = {
    'nfl': 'NFL - Super Bowl Winner',
    'nba': 'NBA - Winner',
    'cfb': 'NCAA(F) - Championship',
    'mcbb': 'NCAA(B) - Winner'
}
