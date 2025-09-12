import cobbler.api as cobblerapi

def generate_script(profile_name):
    cobbler_connection = cobblerapi.CobblerAPI()
    system = cobbler_connection.find_system(profile_name)

    if system is None:
        print(f"No system found with the name {profile_name}")
        return

    autoinstall_meta = system.autoinstall_meta

    # Assuming autoinstall meta has a 'script' field
    if 'script' in autoinstall_meta:
        autoinstall_script = autoinstall_meta['script']
        print(f"Autoinstall script for {profile_name}:\n{autoinstall_script}")
    else:
        print(f"No autoinstall script found for {profile_name}")
