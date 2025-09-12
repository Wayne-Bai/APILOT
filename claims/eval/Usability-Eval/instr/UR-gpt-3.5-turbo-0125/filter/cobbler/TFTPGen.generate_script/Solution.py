
# Importing necessary modules
import subprocess
import os

# Define the function to generate an autoinstall script from a template for a given profile or system
def generate_autoinstall_script(profile_name):
    # Set the path to the autoinstall script template file
    template_file = "/path/to/autoinstall_template.cfg"

    # Check if the template file exists
    if os.path.exists(template_file):
        # Using subprocess to run the cobbler command to generate the autoinstall script
        subprocess.run(["cobbler", "profile", "getks", "--name=" + profile_name, "--template", template_file])
        print("Autoinstall script generated successfully.")
    else:
        print("Autoinstall script template file not found.")

# Provide the profile name for which to generate the autoinstall script
profile_name = "my_profile"

# Call the function to generate the autoinstall script for the provided profile
generate_autoinstall_script(profile_name)
