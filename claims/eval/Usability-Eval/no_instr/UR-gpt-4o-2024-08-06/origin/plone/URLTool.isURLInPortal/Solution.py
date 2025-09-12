from urllib.parse import urlparse
from plone.portal.interfaces import IPloneSiteRoot
from zope.component.hooks import getSite
from zope.globalrequest import getRequest

def isURLInPortal(url):
    """
    Check if the given URL is within the current Plone Site.

    :param url: The URL to check.
    :return: True if the URL is within the portal, False otherwise.
    """
    if not url:
        return False

    # Parse the given url
    parsed_url = urlparse(url)
    
    # Get the current site
    site = getSite()
    
    # Get the site root URL
    portal_root_path = '/'.join(site.getPhysicalPath())
    
    if not parsed_url.netloc:
        # If the url is a relative url, check with the portal path
        is_in_portal = url.startswith(portal_root_path)
    else:
        # Check if the url starts with the site root url
        portal_url = site.absolute_url()
        is_in_portal = url.startswith(portal_url)

    return is_in_portal
