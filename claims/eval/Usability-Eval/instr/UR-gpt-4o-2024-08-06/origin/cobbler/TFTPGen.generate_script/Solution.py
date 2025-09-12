import cobbler.api
import json

def generate_autoinstall_script(profile_name, system_name=None):
    api = cobbler.api.BootAPI()

    # Try to fetch the system or profile
    try:
        if system_name:
            system = api.systems().find(system_name)
            if not system:
                raise ValueError(f"System '{system_name}' does not exist.")
            autoinstall_script_template = system.get('autoinstall_template', None)
        else:
            profile = api.profiles().find(profile_name)
            if not profile:
                raise ValueError(f"Profile '{profile_name}' does not exist.")
            autoinstall_script_template = profile.get('autoinstall_template', None)
        
        if not autoinstall_script_template:
            raise ValueError("Autoinstall script template not found for the given profile or system.")
        
        # Generate the autoinstall script from the template
        # Assuming a simple json-based template for demonstration purposes
        script_data = json.loads(autoinstall_script_template)
        autoinstall_script = process_template(script_data)  # hypothetical function to process template

        return autoinstall_script
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def process_template(template_data):
    # Implement template processing logic
    # This is a placeholder function
    return json.dumps(template_data, indent=4)

# Example usage
if __name__ == "__main__":
    profile_name = "example_profile"
    system_name = "example_system"
    script = generate_autoinstall_script(profile_name, system_name)
    if script:
        print("Generated Autoinstall Script:\n", script)
