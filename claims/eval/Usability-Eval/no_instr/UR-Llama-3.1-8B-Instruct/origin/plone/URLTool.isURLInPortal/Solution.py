from urllib.parse import urlparse
from plone.app.layout.navigation.interfaces import INavigationRoot

def is_url_in_portal(url):
    """
    Checks if a URL is within the current Plone site.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is within the current Plone site, False otherwise.
    """
    
    # Get the current navigation root, which represents the current Plone site
    nav_root = INavigationRoot(getCurrentNavigationRoot())
    
    # Get the portal URL, which is the URL of the current Plone site
    portal_url = getSite().absolute_url()
    
    # Parse the URL to get its components
    parsed_url = urlparse(url)
    
    # Parse the portal URL to get its components
    portal_parsed_url = urlparse(portal_url)
    
    # Check if the URL is within the current Plone site by checking if its path
    # starts with the portal URL's path
    return parsed_url.path.startswith(portal_parsed_url.path)

# Helper function to get the current navigation root
def getCurrentNavigationRoot():
    portal = getSite()
    return portal.portalTypeName =='Folder' and portal or portal.aq_parent

# Helper function to get the site
from Products.CMFCore import utils
def getSite():
    return utils.getSite()
