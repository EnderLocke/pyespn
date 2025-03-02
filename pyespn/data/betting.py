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
        'nfc west': 'Pro Football (A) West Division - Winner',
        'nfc north': 'Pro Football (A) North Division - Winner',
        'nfc south': 'Pro Football (A) South Division - Winner',
        'nfc east': 'Pro Football (A) East  Division - Winner',
        'nfc conf': 'Pro Football (A) Conference Winner'
    },
    'nba': {
        'east': 'NBA - Eastern Conference - Winner',
        'west': 'NBA - Western Conference - Winner'
    },
    'cfb': {

    }
}

LEAGUE_CHAMPION_FUTURES_MAP = {
    'nfl': 'NFL - Super Bowl Winner',
    'nba': 'NBA - Winner',
    'cfb': 'NCAA(F) - Championship',
}
