
from flask import current_app
from os.path import join, abspath

def safe_join(base_dir, *untrusted_parts):
    # Join the untrusted parts with the base directory
    joined_path = join(abspath(base_dir), *untrusted_parts)

    # Check if the joined path is within the allowed scope
    if not current_app.config["ALLOWED_SCOPE"].__contains__(joined_path):
        raise ValueError("The joined path is outside of the allowed scope")

    return joined_path
