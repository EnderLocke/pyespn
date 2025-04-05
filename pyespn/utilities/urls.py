

def get_team_id(url):
    """
    Extracts the team ID from the given URL.

    Args:
        url (str): The URL containing the team information.

    Returns:
        int: The extracted team ID.

    Example:
        >>> url = "https://www.example.com/teams/12345/details"
        >>> get_team_id(url)
        12345
    """
    team_id = url.split('/')[url.split('/').index('teams') + 1].split('?')[0]
    return int(team_id)


def get_athlete_id(url):
    """
    Extracts the athlete ID from the given URL.

    Args:
        url (str): The URL containing the athlete information.

    Returns:
        int: The extracted athlete ID.

    Example:
        >>> url = "https://www.example.com/athletes/98765/stats"
        >>> get_athlete_id(url)
        98765
    """
    athlete_id = url.split('/')[url.split('/').index('athletes') + 1].split('?')[0]
    return int(athlete_id)


def get_schedule_type(url):
    """
    Extracts the schedule type from the given URL.

    Args:
        url (str): The URL containing the schedule type information.

    Returns:
        int: The extracted schedule type.

    Example:
        >>> url = "https://www.example.com/schedules/types/1"
        >>> get_schedule_type(url)
        1
    """
    schedule_type = url.split('/')[url.split('/').index('types') + 1].split('?')[0]
    return int(schedule_type)


def get_an_id(url, slug):
    """
    Extracts a specific ID from the given URL based on the provided slug.

    Args:
        url (str): The URL from which to extract the ID.
        slug (str): The slug used to identify the ID in the URL.

    Returns:
        int: The extracted ID based on the slug.

    Example:
        >>> url = "https://www.example.com/teams/12345/details"
        >>> get_an_id(url, "teams")
        12345
    """
    try:
        this_id = url.split('/')[url.split('/').index(slug) + 1].split('?')[0]
    except ValueError as e:
        return None
    return int(this_id)


def get_a_value(url, slug):
    try:
        this_id = url.split('/')[url.split('/').index(slug) + 1].split('?')[0]
    except ValueError as e:
        this_id = None
    return this_id
