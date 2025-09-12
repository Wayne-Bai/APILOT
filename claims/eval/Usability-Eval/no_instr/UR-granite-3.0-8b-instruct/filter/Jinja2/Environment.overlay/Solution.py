from jinja2 import Environment, FileSystemLoader

def create_overlay_environment(base_env, overlay_dir):
    # Create a new environment for the overlay
    overlay_env = Environment(loader=FileSystemLoader(overlay_dir))

    # Copy all templates from the base environment to the overlay environment
    for template_name in base_env.list_templates():
        overlay_env.templates[template_name] = base_env.get_template(template_name)

    # Remove cache and overridden attributes
    for template in overlay_env.templates.values():
        template.cache = {}

    # Add optional extra extensions to the overlay environment
    # ...

    return overlay_env
