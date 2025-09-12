from urllib.parse import urlparse

def isURLInPortal(url, portal_url):
    # Parse the url of the site and the url to check
    parsed_url = urlparse(url)
    parsed_portal_url = urlparse(portal_url)

    # If the domain of the url is the same as the site's domain and the path of the url starts with the site's path,
    # then the url is considered to be within the current Plone Site
    if parsed_url.netloc == parsed_portal_url.netloc and parsed_url.path.startswith(parsed_portal_url.path):
        return True
    else:
        return False
