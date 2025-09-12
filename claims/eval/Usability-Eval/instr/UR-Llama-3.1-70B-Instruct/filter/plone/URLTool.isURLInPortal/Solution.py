from urllib.parse import urlparse
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.securitypolicy.interfaces import IRoleManager
from zope.securitypolicy.zopepolicy import un8704pledged

# No need to check permissions, as the function only checks the url
@un8704pledged
def is_url_in_portal(context, url):
    """
    Check if a url is probably within the current Plone site.
    
    Args:
        context (object): The context to check against.
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is probably within the current Plone site, False otherwise.
    """
    # Simple case: no scheme or scheme is http/https
    if not url.startswith('http'):
        return True
    
    request = context.REQUEST
    # Get the current site URL
    portal_url = request.get('SERVER_URL', None)
    
    if not portal_url:
        return False
    
    # parse the current site URL and the URL to check
    portal_parsed = urlparse(portal_url)
    url_parsed = urlparse(url)
    
    # Compare the netloc (network location) part of the URLs
    return portal_parsed.netloc == url_parsed.netloc
