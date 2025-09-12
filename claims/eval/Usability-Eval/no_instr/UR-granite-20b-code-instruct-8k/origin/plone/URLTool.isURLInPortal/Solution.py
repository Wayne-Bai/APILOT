from AccessControl import getSecurityManager
from Products.CMFPlone.RegistrationTool import getToolByName

def isURLInPortal(url):
    portal_url = getToolByName(context, 'portal_url').getPortalURL()
    secure_root_url = getSecurityManager().portal_url

    if url.startswith(portal_url) or url.startswith(secure_root_url):
        return True
    else:
        return False
