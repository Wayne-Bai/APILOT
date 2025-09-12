import cobbler.api as cobbler_api

def generate_script_from_autoinstall_template(profile_name):
    # Connect to the Cobbler server
    cobbler_api.init()
    cobbler_api_client = cobbler_api.Client()

    # Get the profile from Cobbler
    try:
        profile = cobbler_api_client.get_profile(profile_name)
    except:
        print(f"Could not find profile: {profile_name}")
        return

    # Generate the autoinstall script
    try:
        template = profile['autoinstall']
        autoinstall_script = cobbler_api_client.generate_autoinstall_script(template)
        print(f"Autoinstall script:\n{autoinstall_script}")
    except KeyError:
        print(f"Profile: {profile_name} does not have an associated autoinstall template.")

# Example usage
generate_script_from_autoinstall_template('my_profile')
