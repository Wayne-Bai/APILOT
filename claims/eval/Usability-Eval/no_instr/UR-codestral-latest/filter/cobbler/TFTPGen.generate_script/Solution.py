import cobbler.api as cobblerapi

# Connect to Cobbler
cobbler = cobblerapi.CobblerAPI()

# Xmlrpc object provides methods for Cobbler objects
cobbler_object = cobbler.get_autoinstall_profile("auto_profile_name")

# Get autoinstall script from specified template
auto_script = cobbler.get_autoinstall_template("auto_template_name").autoinstall

# Assign the script to the profile
cobbler_object.set_autoinstall_meta("AutoinstallSpec", auto_script)

# Save the changes to the profile
cobbler.save_profile("auto_profile_name")

# Synchronize the changes with Cobbler
cobbler.sync()
