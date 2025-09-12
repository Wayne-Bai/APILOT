import cobbler

def generate_script_from_template(profile, system):
    # Get the profile and system
    cob_profile = cobbler.connection.getProfile(profile)
    cob_system = cobbler.connection.getSystem(system)

    # Create a new autoinstall file from the profile's autoinstall template
    courier = cob_profile.getProperty('courier_params')
    cobbler.connection.createSystemAutoinstall(
        system=cob_system,
        filename='autoinstall Isidhre',
        params=courier,
        template=cob_profile.getProperty('autoinstall_template')
    )

    print(f"Template 'autoinstall' has been generated for {profile}")

# Example usage (replace 'profile_name' and 'system_name' with actual values)
generate_script_from_template('profile_name', 'system_name')
