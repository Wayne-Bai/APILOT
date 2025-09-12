from Products.CMFPlone.utils import getToolByName

def isURLInPortal(url):
    portal = getToolByName(None, 'portal_url')
    return portal.isSafeURL(url)
