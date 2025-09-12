from plone import api
from plone.dexterity.utils import createContentInContainer

def is_url_in_portal(url):
    site_url = api.portal.get().absolute_url()
    return url.startswith(site_url)
