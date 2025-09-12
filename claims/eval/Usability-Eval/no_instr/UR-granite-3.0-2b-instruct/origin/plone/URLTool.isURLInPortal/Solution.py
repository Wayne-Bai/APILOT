from plone import IURLRequest

def isURLInPortal(url):
    request = IURLRequest()
    return request.isURLWithinPortal(url)
