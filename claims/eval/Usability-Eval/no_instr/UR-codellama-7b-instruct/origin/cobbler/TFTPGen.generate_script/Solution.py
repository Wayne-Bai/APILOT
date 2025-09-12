
import cobbler

# Get the system profile
system_profile = cobbler.get_system_profile("my-profile")

# Generate an install script from the autoinstall template for the given system profile
install_script = cobbler.generate_install_script(system_profile)

# Print the generated install script to the console
print(install_script)
