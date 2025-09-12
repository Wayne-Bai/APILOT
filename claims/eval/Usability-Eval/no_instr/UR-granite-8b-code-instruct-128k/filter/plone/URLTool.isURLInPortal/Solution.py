import plone

def isURLInPortal(url):
    """
    Checks if a url is (probably) within the current Plone Site. If so, then this url is safe to redirect to, or is safe to show on a page.
    """
    portal = plone.api.portal.get()
    return portal.relativeURL(url).startswith('/')