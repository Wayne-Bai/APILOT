# Import the Cobbler library
import cobbler

# Create a Cobbler object to interact with the Cobbler server
c = cobbler.api()

# Set the profile or system name
profile_name = "your_profile_name"

# Set the autoinstall template name
autoinstall_template_name = "your_autoinstall_template_name"

# Get the profile object from Cobbler
profile = c.find_profile(profile_name)
if profile is None:
    print(f"Profile {profile_name} not found.")
    exit(1)

# Get the autoinstall template object from Cobbler
autoinstall_template = c.find_autoinstall_template(autoinstall_template_name)
if autoinstall_template is None:
    print(f"Autoinstall template {autoinstall_template_name} not found.")
    exit(1)

# Generate a script from the autoinstall script template
script = c.system_profile_to_script(profile, autoinstall_template_name)

# Print the generated script
print("\nGenerated Script:")
print("-------------------")
print(script)
