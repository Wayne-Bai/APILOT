from urllib.parse import urlparse
from plone import api

def is_url_in_portal(url):
    """
    Check if a URL is within the current Plone Site.

    :param url: The URL to check.
    :return: True if the URL is within the site, False otherwise.
    """
    # Parse the input URL
    parsed_url = urlparse(url)

    # Get the portal object
    portal = api.portal.get()

    # Get the portal URL and parse it
    portal_url = api.portal.get().absolute_url()
    parsed_portal_url = urlparse(portal_url)

    # Compare the network locations
    return (
        parsed_url.netloc == parsed_portal_url.netloc and
        parsed_url.path.startswith(parsed_portal_url.path)
    )

# Example usage:
url = "http://example.com/plone/some-page"
if is_url_in_portal(url):
    print("The URL is inside the current Plone Site.")
else:
    print("The URL is outside the current Plone Site.")
