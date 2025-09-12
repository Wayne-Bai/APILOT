from Products.Five.browser import BrowserView
from AccessControl.subject import getSubject
from OFS.ObjectManager import ObjectManager
from Products.CMFCore.utils import getToolByName

class IsURLInPortal(BrowserView):
    def isURLInPortal(self, url):
        subject = getSubject()
        if not subject.hasPermission('View', self.context):
            return False

        portal = self.context.getPhysicalPath()
        if not portal:
            return False

        url_parts = url.split('://')
        if len(url_parts) != 2:
            return False

        url_host = url_parts[1].split('/')[0]
        portal_host = portal.split('://')[-1].split('/')[0]

        return url_host == portal_host
