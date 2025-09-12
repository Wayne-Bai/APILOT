from cobbler.plugins.base import PluginBase

class GenerateScriptPlugin(PluginBase):
    def run(self):
        profile = self.profile
        template_file = "autoinstall_script_template.py"

        with open(template_file, "r") as f:
            template = f.read()

        script = template.format(profile=profile)

        with open("generated_script.py", "w") as f:
            f.write(script)

        print("Script generated successfully!")

# Usage
generate_script_plugin = GenerateScriptPlugin()
generate_script_plugin.run()
