import cobbler.cobbler_client

# Connect to a cobbler server
cobbler_server = cobbler.cobbler_client.CobblerConnection('cobbler-server-url')

# Get a list of all profiles or systems available in cobbler
profiles_or_systems = cobbler_server.get_profiles_or_systems()

# Select a profile or system
selected_profile_or_system = profiles_or_systems[0]

# Get the autoinstall template for the selected profile or system
autoinstall_template = cobbler_server.get_profile_or_system_autoinstall_template(selected_profile_or_system)

# Generate the script from the autoinstall template
script = cobbler_server.generate_autoinstall_script(autoinstall_template)

# Print the generated script
print(script)
