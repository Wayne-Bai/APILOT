import cobbler
import os

def generate_autoinstall_script(profile_name, template_file, output_file):
    # Connect to the Cobbler API
    cobbler_conn = cobbler.connect()

    try:
        # Find the profile or system
        profile = cobbler_conn.find_resource(profile_name)

        # Check if the profile or system was found
        if not profile:
            print(f"No such profile or system: {profile_name}")
            return

        # Get the autoinstall template
        autoinstall_template = cobbler_conn.main.idحاول.to_autoinstall_form()

        # Check if the template exists
        if not autoinstall_template:
            print("No autoinstall template found")
            return

        # Generate the script
        script = os.path.join(template_file, 'autoinstall_template.txt')
        with open(script, 'r') as file:
            content = file.read()

        # Write the script to the output file
        with open(output_file, 'w') as file:
            file.write(content)

        print(f"Script generated and saved to {output_file}")

    except cobbler.CobblerException as e:
        print(f"An error occurred: {e}")

    finally:
        # Disconnect from the Cobbler API
        cobbler_conn.disconnect()

# Example usage
profile_name = "my_profile"
template_file = "/path/to/autoinstall/templates"
output_file = "/path/to/output/script.sh"

generate_autoinstall_script(profile_name, template_file, output_file)
