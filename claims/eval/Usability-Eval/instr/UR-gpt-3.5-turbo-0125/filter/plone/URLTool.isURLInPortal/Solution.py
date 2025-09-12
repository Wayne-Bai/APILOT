
# Importing the necessary libraries from Plone
from Products.CMFCore.utils import getToolByName

# Define a function to check if a URL is within the current Plone Site
def is_url_in_portal(context, url):
    portal_url = getToolByName(context, 'portal_url')()
    if url.startswith(portal_url):
        return True
    else:
        return False

# Example usage
current_url = 'http://example.com/some-page'
if is_url_in_portal(context, current_url):
    print('The URL is within the current Plone Site')
else:
    print('The URL is outside the current Plone Site')
