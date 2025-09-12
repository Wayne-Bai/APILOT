from flask import safe_join

base_directory = '/home/user/myproject'
untrusted_paths = ['..', 'file.txt']

safe_path = safe_join(base_directory, *untrusted_paths)
print(safe_path)  # Output: /home/user/myproject/file.txt
