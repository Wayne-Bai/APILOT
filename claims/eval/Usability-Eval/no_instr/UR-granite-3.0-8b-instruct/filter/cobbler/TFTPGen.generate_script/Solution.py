import cobbler

def generate_script(profile_name):
    # Connect to the Cobbler server
    cobbler_server = cobbler.CobblerServer('http://localhost:8080')

    # Get the profile
    profile = cobbler_server.get_profile(profile_name)

    # Generate the script
    script = cobbler_server.generate_script(profile)

    # Save the script to a file
    with open('script.sh', 'w') as f:
        f.write(script)

# Example usage
generate_script('my_profile')
