import cobbler
from cobbler import cobbler_xmlrpc

def generate_autoinstall_script(target_name, target_type):
    # Set up XMLRPC connection variables
    server_url = "http://localhost/cobbler_api"
    server_user = "cobbler_user"
    server_password = "cobbler_password"

    # Connect to the Cobbler XMLRPC API
    server = cobbler_xmlrpc.BootAPI(server_url, server_user, server_password)

    # Check if the target_type is valid
    if target_type not in ["system", "profile"]:
        raise ValueError("Invalid target_type. Please use 'system' or 'profile'.")

    # Fetch the autoinstall script based on target_type
    if target_type == "system":
        system = server.find_system({"name": target_name})
        if not system:
            raise ValueError(f"System '{target_name}' not found.")
        autoinstall_script = server.get_system_autoinstall_template(system[0]["name"])
    else:
        profile = server.find_profile({"name": target_name})
        if not profile:
            raise ValueError(f"Profile '{target_name}' not found.")
        autoinstall_script = server.get_profile_autoinstall_template(profile[0]["name"])

    # Return the autoinstall script
    return autoinstall_script

# Example usage
try:
    target_name = "example_profile"  # Replace with actual profile or system name
    target_type = "profile"  # Change to "system" if targeting a system
    script = generate_autoinstall_script(target_name, target_type)
    print(script)
except Exception as e:
    print(f"An error occurred: {e}")
