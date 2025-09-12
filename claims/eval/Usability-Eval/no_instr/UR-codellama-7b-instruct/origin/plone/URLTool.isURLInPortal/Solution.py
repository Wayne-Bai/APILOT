
from Products.CMFCore.utils import getToolByName

def isURLInPortal(url):
    portal = getToolByName(context, 'portal_url')
    return portal.has_url(url)
