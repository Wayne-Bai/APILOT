import os
importuuid
from cobbler.cobbler_collections import collection

# Initialize Cobbler instance
cobbler_api = collection.CobblerAPI()

def generate_autoinstall_script(profile_or_system):
    """
    Generate a script from an autoinstall script template 
    for a given profile or system.

    Args:
    profile_or_system (str): The name of the profile or system to generate the script for.

    Returns:
    str: The generated script
    """
    try:
        # Get the profile or system object
        obj = cobbler_api.find_item(name=profile_or_system, no_fail=True)

        if obj is None:
            print(f"Object '{profile_or_system}' not found.")
            return None

        # Get the associated renderable to generate the script from
        renderable = obj.autoinstall_script_template

        # Generate the script
        script = obj.render_autoinstall_script(renderable)

        return script
    except Exception as e:
        print(f"Failed to generate script: {str(e)}")
        return None

# Usage example
profile_or_system_name = "my_profile"
script = generate_autoinstall_script(profile_or_system_name)

if script:
    with open(f"{profile_or_system_name}.sh", "w") as f:
        f.write(script)
    print(f"Script saved to {profile_or_system_name}.sh")
