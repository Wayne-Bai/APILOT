from cobbler import api

def generate_autoinstall_script(profile_name, system_name=None):
    # Initialize the Cobbler API
    cobbler_api = api.CobblerAPI()

    # Fetch the profile or system
    if system_name:
        item = cobbler_api.get_system(system_name)
    else:
        item = cobbler_api.get_profile(profile_name)

    if not item:
        raise ValueError("Profile or System not found.")

    # Generate the autoinstall script template
    autoinstall_template = item.autoinstall_template

    # Render the template
    rendered_script = cobbler_api.render_autoinstall_template(autoinstall_template, item)

    return rendered_script

# Example usage
profile_name = "example_profile"
system_name = "example_system"  # Optional, if generating for a specific system

autoinstall_script = generate_autoinstall_script(profile_name, system_name)
print(autoinstall_script)
