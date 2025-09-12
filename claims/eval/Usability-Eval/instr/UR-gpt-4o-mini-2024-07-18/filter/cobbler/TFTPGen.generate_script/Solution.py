import cobbler

def generate_autoinstall_script(profile_name, template_path, output_path):
    # Initialize Cobbler object
    cobbler_api = cobbler.Cobbler()

    # Fetch profile details based on profile name
    profile = cobbler_api.get_profile(profile_name)

    if not profile:
        print(f"Profile '{profile_name}' not found.")
        return

    # Read template
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Replace placeholders in template with profile details
    script_content = template_content.format(**profile)

    # Write the generated script to output path
    with open(output_path, 'w') as output_file:
        output_file.write(script_content)

    print(f"Autoinstall script generated at '{output_path}'.")

# Example usage:
# generate_autoinstall_script('my_profile', 'template_script.sh', 'output_script.sh')
