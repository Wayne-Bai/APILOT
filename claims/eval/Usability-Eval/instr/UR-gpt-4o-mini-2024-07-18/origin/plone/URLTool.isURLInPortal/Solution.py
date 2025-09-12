from plone.api.portal import get_tool

def is_url_in_portal(url):
    """
    Check if a given URL is within the current Plone site.

    :param url: The URL to check.
    :return: True if the URL is within the portal, False otherwise.
    """
    portal_url = get_tool('portal_url').get()
    return url.startswith(portal_url)
