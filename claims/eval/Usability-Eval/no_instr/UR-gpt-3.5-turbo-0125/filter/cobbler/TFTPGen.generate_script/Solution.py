
import cobbler

# Connect to Cobbler server
cob = cobbler.Cobbler('CobblerServerIP')

# Get profile or system details
profile_name = 'my_profile'
profile = cob.get_profile(profile_name)

# Generate autoinstall script from the template
autoinstall_template = profile['kickstart']
autoinstall_script = f'#!/bin/bash\n{autoinstall_template}'

print(autoinstall_script)
