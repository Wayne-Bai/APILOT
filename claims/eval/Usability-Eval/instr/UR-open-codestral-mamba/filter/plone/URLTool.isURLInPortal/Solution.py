from plone import api
from plone.app.uuid.utils import uuid_for
from plone.dexterity.utils import createContentInContainer

def isURLInPortal(url):
    portal = api.portal.get()
    portal_path = '/'.join(portal.getPhysicalPath())
    return url.startswith(portal_path)
