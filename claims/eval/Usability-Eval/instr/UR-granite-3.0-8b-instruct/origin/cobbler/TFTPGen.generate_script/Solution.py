import subprocess

def generate_script(template, profile, system):
    command = f"cobbler profile create --name={profile} --kickstart=/path/to/ks.cfg"
    subprocess.run(command, shell=True)

    command = f"cobbler script generate --template={template} --profile={profile} --system={system}"
    subprocess.run(command, shell=True)

# Replace 'your_template.cfg', 'your_profile', and 'your_system' with your actual values
generate_script("your_template.cfg", "your_profile", "your_system")
