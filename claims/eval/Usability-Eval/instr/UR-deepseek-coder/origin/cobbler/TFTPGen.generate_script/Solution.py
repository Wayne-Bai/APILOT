from cobbler import api

def generate_autoinstall_script(profile_name=None, system_name=None):
    # Initialize the Cobbler API
    cobbler_api = api.CobblerAPI()

    # Fetch the profile or system object
    if profile_name:
        item = cobbler_api.get_profile(profile_name)
    elif system_name:
        item = cobbler_api.get_system(system_name)
    else:
        raise ValueError("Either profile_name or system_name must be provided.")

    if not item:
        raise ValueError(f"No {'profile' if profile_name else 'system'} found with name {profile_name or system_name}")

    # Generate the autoinstall script from the template
    autoinstall_template = item.autoinstall_meta.get("autoinstall_template", "")
    autoinstall_script = cobbler_api.generate_autoinstall_script(item, autoinstall_template)

    return autoinstall_script

# Example usage:
# autoinstall_script = generate_autoinstall_script(profile_name="my_profile")
# print(autoinstall_script)
