from AccessControl.SecurityManagement import newSecurityManager, getSecurityManager
from AccessControl.SpecialUsers import NoUser
from AccessControl.User import nobody
from Products.CMFCore.utils import getToolByName
from Testing import ZopeTestCase as ztc
from plone.testing import zca

def setUp(self):
    ztc.ZopeTestCase.setUp(self)
    setUpPloneSite = self.get('setUpPloneSite')
    self.app.REQUEST['PARENTS'] = [self.app]
    setUpPloneSite(self.portal)
    self.request = self.app.REQUEST
    self.request['PARENTS'] = [self.request]
    self.folder = self.portal.my_folder
    self.user = self.createUser()
    newSecurityManager(None, self.user.__of__(self.portal.acl_users))

def tearDown(self):
    getSecurityManager().setSecurityPolicy(self.old_policy)
    ztc.ZopeTestCase.tearDown(self)

def createUser(self,item_id="test_user"):
    roles = ['Member', 'Contributor' ]
    self.portal.portal_registration.addMember(item_id, 'secret', roles, [])
    self.portal.portal_workflow.doActionFor(self.portal.portal_membership.getMemberById(item_id), 'activateMember')
    return self.portal.portal_membership.getMemberById(item_id)

def isURLInPortal(self, url):
    if url.strip().startswith(self.portal.absolute_url()):
        return True
    else:
        return False
