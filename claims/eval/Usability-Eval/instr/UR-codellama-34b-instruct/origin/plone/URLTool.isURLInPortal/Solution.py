import plone

def isURLInPortal(url):
    # Get the current Plone site object
    site = plone.api.portal.get()
    
    # Get the absolute URL of the current site
    base_url = site.absolute_url()
    
    # Strip off any leading or trailing slashes from the URL
    url = url.strip("/")
    
    # Check if the URL is a child of the current site
    if not url.startswith(base_url):
        return False
    
    # Check if the URL exists in the current site
    try:
        resource = plone.api.portal.getResource(url)
    except plone.api.portal.ResourceNotFoundError:
        return False
    
    # If we get this far, then the URL is within the current Plone site
    return True
