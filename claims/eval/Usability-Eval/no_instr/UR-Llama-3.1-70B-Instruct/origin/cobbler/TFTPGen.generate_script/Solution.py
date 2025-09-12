import subprocess
import shutil
import os
from cobbler import autoinstall_gen as gen

# Cobbler configuration and template directory
cobbler_config = "/etc/cobbler/settings.yaml"
template_dir = "/etc/cobbler/templates"

def generate_autoinstall_script(profile_or_system_name, output_path):
    """
    Generate a script from an autoinstall script template for a given profile or system.
    
    Parameters:
    profile_or_system_name (str): The name of the profile or system.
    output_path (str): The path to save the generated script.
    """
    
    # Create the AutoInstallGen object
    autoinstall_gen = gen.AutoInstallGen(cobbler_config)
    
    # Check if the profile or system exists
    if autoinstall_gen.collection.systems().find(name=profile_or_system_name):
        # Generate the autoinstall script for a system
        script = autoinstall_gen.generate_system_autoinstall(profile_or_system_name)
    elif autoinstall_gen.collection.profiles().find(name=profile_or_system_name):
        # Generate the autoinstall script for a profile
        script = autoinstall_gen.generate_profile_autoinstall(profile_or_system_name)
    else:
        raise ValueError("Profile or system does not exist")
    
    # Write the script to the output file
    with open(output_path, 'w') as f:
        f.write(script)

# Example usage
profile_or_system_name = "my_profile"
output_path = "/path/to/script.sh"
generate_autoinstall_script(profile_or_system_name, output_path)
