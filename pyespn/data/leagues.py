# todo - sports not added yet
#  cricket, field-hockey, lacrosse,
#  mma, rugby-league, australian-football,
#  soccer, water-polo, volleyball, rugby

LEAGUE_API_MAPPING = [
    {
        'id': 1,
        'league_abbv': 'mcbb',
        'sport': 'basketball',
        'league': 'mens-college-basketball',
        'status': 'available' # can be available untested or unavailable
    },
    {
        'id': 2,
        'league_abbv': 'cfb',
        'sport': 'football',
        'league': 'college-football',
        'status': 'available'
    },
    {
        'id': 3,
        'league_abbv': 'nfl',
        'sport': 'football',
        'league': 'nfl',
        'status': 'available'
    },
    {
        'id': 4,
        'league_abbv': 'nba',
        'sport': 'basketball',
        'league': 'nba',
        'status': 'available'
    },
    {
        'id': 5,
        'league_abbv': 'cbb',
        'sport': 'baseball',
        'league': 'college-baseball',
        'status': 'available'
    },
    {
        'id': 6,
        'league_abbv': 'csb',
        'sport': 'baseball',
        'league': 'college-softball',
        'status': 'available'
    },
    {
        'id': 7,
        'league_abbv': 'wnba',
        'sport': 'basketball',
        'league': 'wnba',
        'status': 'available'
    },
    {
        'id': 8,
        'league_abbv': 'f1',
        'sport': 'racing',
        'league': 'f1',
        'status': 'available'
    },
    {
        'id': 9,
        'league_abbv': 'nascar',
        'sport': 'racing',
        'league': 'nascar-premier',
        'status': 'available'
    },
    {
        'id': 10,
        'league_abbv': 'indy',
        'sport': 'racing',
        'league': 'irl',
        'status': 'available'
    },
    {
        'id': 11,
        'league_abbv': 'mlb',
        'sport': 'baseball',
        'league': 'mlb',
        'status': 'available'
    },
    {
        'id': 12,
        'league_abbv': 'nascar2',
        'sport': 'racing',
        'league': 'nascar-secondary',
        'status': 'unavailable'
    },
    {
        'id': 13,
        'league_abbv': 'nascar-truck',
        'sport': 'racing',
        'league': 'nascar-truck',
        'status': 'unavailable'
    },
    {
        'id': 14,
        'league_abbv': 'nhra',
        'sport': 'racing',
        'league': 'nhra',
        'status': 'unavailable'
    },
    {
        'id': 15,
        'league_abbv': 'cfl',
        'sport': 'football',
        'league': 'cfl',
        'status': 'unavailable'
    },
    {
        'id': 16,
        'league_abbv': 'ufl',
        'sport': 'football',
        'league': 'ufl',
        'status': 'unavailable'
    },
    {
        'id': 17,
        'league_abbv': 'xfl',
        'sport': 'football',
        'league': 'xfl',
        'status': 'unavailable'
    },
    {
        'id': 18,
        'league_abbv': 'mens-olympics-basketball',
        'sport': 'basketball',
        'league': 'mens-olympics-basketball',
        'status': 'unavailable'
    },
    {
        'id': 19,
        'league_abbv': 'fiba',
        'sport': 'basketball',
        'league': 'fiba',
        'status': 'unavailable'
    },
    {
        'id': 20,
        'league_abbv': 'g-league',
        'sport': 'basketball',
        'league': 'nba-development',
        'status': 'unavailable'
    },
    {
        'id': 21,
        'league_abbv': 'summer-gs',
        'sport': 'basketball',
        'league': 'nba-summer-golden-state',
        'status': 'unavailable'
    },
    {
        'id': 22,
        'league_abbv': 'summer-lv',
        'sport': 'basketball',
        'league': 'nba-summer-las-vegas',
        'status': 'unavailable'
    },
    {
        'id': 23,
        'league_abbv': 'summer-orl',
        'sport': 'basketball',
        'league': 'nba-summer-orlando',
        'status': 'unavailable'
    },
    {
        'id': 24,
        'league_abbv': 'summer-sac',
        'sport': 'basketball',
        'league': 'nba-summer-sacramento',
        'status': 'unavailable'
    },
    {
        'id': 25,
        'league_abbv': 'summer-utah',
        'sport': 'basketball',
        'league': 'nba-summer-utah',
        'status': 'unavailable'
    },
    {
        'id': 26,
        'league_abbv': 'nbl',
        'sport': 'basketball',
        'league': 'nbl',
        'status': 'unavailable'
    },
    {
        'id': 27,
        'league_abbv': 'womens-olympics-basketball',
        'sport': 'basketball',
        'league': 'womens-olympics-basketball',
        'status': 'unavailable'
    },
    {
        'id': 28,
        'league_abbv': 'wcbb',
        'sport': 'basketball',
        'league': 'womens-college-basketball',
        'status': 'unavailable'
    },
    {
        'id': 29,
        'league_abbv': 'atp',
        'sport': 'tennis',
        'league': 'atp',
        'status': 'unavailable'
    },
    {
        'id': 30,
        'league_abbv': 'wta',
        'sport': 'tennis',
        'league': 'wta',
        'status': 'unavailable'
    },
    {
        'id': 31,
        'league_abbv': 'champions-tour',
        'sport': 'golf',
        'league': 'champions-tour',
        'status': 'unavailable'
    },
    {
        'id': 32,
        'league_abbv': 'eur',
        'sport': 'golf',
        'league': 'eur',
        'status': 'unavailable'
    },
    {
        'id': 33,
        'league_abbv': 'liv',
        'sport': 'golf',
        'league': 'liv',
        'status': 'unavailable'
    },
    {
        'id': 34,
        'league_abbv': 'lpga',
        'sport': 'golf',
        'league': 'lpga',
        'status': 'unavailable'
    },
    {
        'id': 35,
        'league_abbv': 'mens-olympics-golf',
        'sport': 'golf',
        'league': 'mens-olympics-golf',
        'status': 'unavailable'
    },
    {
        'id': 36,
        'league_abbv': 'ntw',
        'sport': 'golf',
        'league': 'ntw',
        'status': 'unavailable'
    },
    {
        'id': 37,
        'league_abbv': 'pga',
        'sport': 'golf',
        'league': 'pga',
        'status': 'unavailable'
    },
    {
        'id': 38,
        'league_abbv': 'womens-olympics-golf',
        'sport': 'golf',
        'league': 'womens-olympics-golf',
        'status': 'unavailable'
    },
    {
        'id': 39,
        'league_abbv': 'winter-dominican',
        'sport': 'baseball',
        'league': 'dominican-winter-league',
        'status': 'unavailable'
    },
    {
        'id': 40,
        'league_abbv': 'llb',
        'sport': 'baseball',
        'league': 'llb',
        'status': 'unavailable'
    },
    {
        'id': 41,
        'league_abbv': 'winter-mexican',
        'sport': 'baseball',
        'league': 'mexican-winter-league',
        'status': 'unavailable'
    },
    {
        'id': 42,
        'league_abbv': 'caribbean',
        'sport': 'baseball',
        'league': 'caribbean-series',
        'status': 'unavailable'
    },
    {
        'id': 43,
        'league_abbv': 'olympics-baseball',
        'sport': 'baseball',
        'league': 'olympics-baseball',
        'status': 'unavailable'
    },
    {
        'id': 44,
        'league_abbv': 'winter-pr',
        'sport': 'baseball',
        'league': 'puerto-rican-winter-league',
        'status': 'unavailable'
    },
    {
        'id': 45,
        'league_abbv': 'winter-ven',
        'sport': 'baseball',
        'league': 'venezuelan-winter-league',
        'status': 'unavailable'
    },
    {
        'id': 46,
        'league_abbv': 'wbc',
        'sport': 'baseball',
        'league': 'world-baseball-classic',
        'status': 'unavailable'
    },
    {
        'id': 47,
        'league_abbv': 'nhl',
        'sport': 'hockey',
        'league': 'nhl',
        'status': 'unavailable'
    },
    {
        'id': 48,
        'league_abbv': 'mens-college-hockey',
        'sport': 'hockey',
        'league': 'mens-college-hockey',
        'status': 'unavailable'
    },
    {
        'id': 49,
        'league_abbv': 'hwc',
        'sport': 'hockey',
        'league': 'hockey-world-cup',
        'status': 'unavailable'
    },
    {
        'id': 50,
        'league_abbv': 'olympics-mens-hockey',
        'sport': 'hockey',
        'league': 'olympics-mens-ice-hockey',
        'status': 'unavailable'
    },
    {
        'id': 51,
        'league_abbv': 'olympics-womens-hockey',
        'sport': 'hockey',
        'league': 'olympics-womens-ice-hockey',
        'status': 'unavailable'
    },
    {
        'id': 52,
        'league_abbv': 'mens-college-hockey',
        'sport': 'hockey',
        'league': 'mens-college-hockey',
        'status': 'unavailable'
    },
]

PRO_LEAGUES = [
    'nfl', 'nba', 'nhl', 'mlb', 'wnba'
]

COLLEGE_LEAGUES = [
    'cfb', 'mcbb', 'wcbb', 'cbb', 'csb'
]
