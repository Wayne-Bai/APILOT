from werkzeug import local

# Create a class to inherit from LocalProxy
class ScriptNameLocator(local.LocalProxy):
    def __init__(self, get_current_object):
        self.get_current_object = get_current_object
        super(ScriptNameLocator, self).__init__(None)
        self.app = None  # You need to set this to your application instance

class Application(object):
    def __init__(self, name):
        self.name = name

    @property
    def script_name(self):
        return '/%s' % self.name


# Usage
app = Application('myapp')

# Create an instance of the ScriptNameLocator class
script_name = ScriptNameLocator(lambda: app.get_script_name__)

# You can now access the script name like this:
script_name = script_name()

print(script_name)  # Outputs: /myapp
