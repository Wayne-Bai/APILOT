import cobbler

def generate_script(profile, system):
    """Generates a script from a autoinstall script template for a given profile or system.

    Args:
        profile (str): The name of the profile to use for the script generation.
        system (dict): A dictionary containing information about the system that will be installing the script, including the OS, architecture, and distribution.

    Returns:
        str: The generated script, formatted as a Python string.
    """
    # Load the autoinstall template
    with open("autoinstall_template.txt", "r") as f:
        template = f.read()

    # Replace placeholders in the template with actual values for the given system
    replaced_template = template.replace("{{profile}}", profile)
    replaced_template = replaced_template.replace("{{os}}", system["os"])
    replaced_template = replaced_template.replace("{{arch}}", system["architecture"])
    replaced_template = replaced_template.replace("{{distro}}", system["distribution"])

    # Return the generated script
    return replaced_template
