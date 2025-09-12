
import zope.component
from Products.CMFCore.utils import getToolByName

def isURLInPortal(url):
    portal_url = zope.component.getUtility(IApplicationServer).root()
    parsed_url = urlparse(url)
    if parsed_url.netloc == portal_url:
        return True
    else:
        return False
