from cobbler import Cobbler

# Initialize Cobbler
cobbler = Cobbler()

# Load the autoinstall script template
template = cobbler.templates.load("autoinstall_template.py")

# Set the profile or system name
profile_name = "my_profile"

# Generate the script for the given profile or system
script = template.render(profile_name=profile_name)

# Save the generated script to a file
with open(f"{profile_name}.py", "w") as f:
    f.write(script)
