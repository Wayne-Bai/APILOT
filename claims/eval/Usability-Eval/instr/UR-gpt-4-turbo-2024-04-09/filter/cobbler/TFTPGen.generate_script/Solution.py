import cobbler.api

# Initialize the cobbler API
cobbler_api = cobbler.api.BootAPI()

def generate_script(profile_or_system_name, is_profile=True):
    # Retrieve the profile or system object
    if is_profile:
        item = cobbler_api.find_profile(name=profile_or_system_name)
    else:
        item = cobbler_api.find_system(name=profile_or_system_name)
    
    if item is None:
        print(f"No {'profile' if is_profile else 'system'} found with the name {profile_or_system_name}")
        return

    # Generate the autoinstallation script for the profile or system
    script = cobbler_api.generate_autoinstall(item)
    
    print(f"Generated script for {'profile' if is_profile else 'system'} '{profile_or_system_name}':")
    print(script)

# Example usage:
generate_script("example_profile", is_profile=True)
