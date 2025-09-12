from plone import api
from urllib.parse import urlparse

def isURLInPortal(url):
    portal_url = api.portal.get().absolute_url()
    parsed_url = urlparse(url)

    # Compare netloc of the given URL with the portal URL's netloc
    if parsed_url.netloc and parsed_url.netloc != urlparse(portal_url).netloc:
        return False
    return True
