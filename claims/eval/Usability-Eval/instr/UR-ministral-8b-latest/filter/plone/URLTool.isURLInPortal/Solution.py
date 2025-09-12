from plone import api

def isURLInPortal(url):
    portal_url = api.portal.get().absolute_url()
    return url.startswith(portal_url)

# Example usage:
url_to_check = "http://my-plone-site/absolute/url"
if isURLInPortal(url_to_check):
    print(f"{url_to_check} is within the current Plone site.")
else:
    print(f"{url_to_check} is NOT within the current Plone site.")
