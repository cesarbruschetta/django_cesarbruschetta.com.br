from django import template

from unidecode import unidecode

register = template.Library()


@register.filter
def truncatesmart(value, limit=250):
    """
    Truncates a string after a given number of chars keeping whole words.

    Usage:
        {{ string|truncatesmarts }}
        {{ string|truncatesmart:50 }}
    """

    try:
        # invalid literal for int()
        limit = int(limit)
    except ValueError:
        # Fail silently.
        return value

    # Make sure it's unicode
    value = unidecode(value)

    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value

    # Cut the string
    value = value[:limit]

    # Break into words and remove the last
    words = value.split(' ')[:-1]

    # Join the words and return
    return ' '.join(words) + '...'
