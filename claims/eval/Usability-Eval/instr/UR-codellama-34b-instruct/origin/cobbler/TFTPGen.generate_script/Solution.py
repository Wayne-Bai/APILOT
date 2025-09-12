import cobbler

# Connect to Cobbler
c = cobbler.Cobbler()

# Get the profile or system information
profile_or_system_name = "my-profile"
profile_or_system = c.find_profile(name=profile_or_system_name)

# Generate a script from a autoinstall script template for the given profile or system
template_path = "/usr/share/cobbler/templates/autoinstall/generic.ks"
script_path = f"/var/lib/cobbler/{profile_or_system_name}.ks"
c.render_template(template_path, script_path)
