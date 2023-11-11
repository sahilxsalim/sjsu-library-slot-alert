from datetime import datetime, timedelta

def increment_date(date_string, days=1):
    """
    Increment the given date string by a specified number of days.

    Parameters:
    - date_string (str): Date in the format '%Y-%m-%d'.
    - days (int): Number of days to increment (default is 1).

    Returns:
    - str: Updated date string.
    """
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d')

    # Increment the day by the specified number of days
    new_date = date_object + timedelta(days=days)

    # Convert the result back to a string
    new_date_string = new_date.strftime('%Y-%m-%d')

    return new_date_string
