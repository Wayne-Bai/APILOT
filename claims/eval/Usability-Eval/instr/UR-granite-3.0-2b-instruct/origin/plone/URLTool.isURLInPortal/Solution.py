from plone import IAAC

def is_url_in_portal(url):
    """
    Check if a URL is within the current Plone site.

    :param url: The URL to check.
    :return: True if the URL is within the current Plone site, False otherwise.
    """
    # Get the current Plone site
    site = IAAC.getCurrentSite()

    # Check if the URL starts with the site's URL
    return site.url.startswith(url)
