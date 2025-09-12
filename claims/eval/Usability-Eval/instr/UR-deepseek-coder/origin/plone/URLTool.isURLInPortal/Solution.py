from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from zope.component import getMultiAdapter
from zope.interface import alsoProvides
from zope.publisher.browser import BrowserView

class URLChecker(BrowserView):
    def isURLInPortal(self, url):
        """
        Check if the given URL is within the current Plone Site.

        :param url: The URL to check.
        :type url: str
        :return: True if the URL is within the portal, False otherwise.
        :rtype: bool
        """
        portal_url = api.portal.get().absolute_url()
        if url.startswith(portal_url):
            return True
        return False

# Example usage:
# checker = URLChecker(context, request)
# is_safe = checker.isURLInPortal('http://example.com/plone/some-page')
