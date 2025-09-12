from plone import api

def isURLInPortal(url):
    """ Check if the provided URL is within the current Plone site. """
    portal_url = api.portal.get().absolute_url()
    return url.startswith(portal_url)
