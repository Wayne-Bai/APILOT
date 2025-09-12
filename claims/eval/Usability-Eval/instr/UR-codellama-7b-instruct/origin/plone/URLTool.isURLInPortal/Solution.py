
from Products.PloneGetTool import getUtility

def isURLInPortal(url):
    portal_url = getUtility(IServerProxy).getServerURL()
    return url.startswith(portal_url)
