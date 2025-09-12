
from Products.CMFCore.utils import getToolByName

def isURLInPortal(portal, url):
    portal_url = portal.absolute_url()
    
    if url.startswith(portal_url):
        return True
    
    portal_catalog = getToolByName(portal, 'portal_catalog')
    portal_path = portal.getPhysicalPath()
    url_path = url.split('/')
    
    if url_path[1:] == portal_path[1:]:
        return True
    
    return False
