from jinja2 import Template

def create_overlay環設定(env):
    """
    Create a new overlay environment from the current environment, excluding cache and overridden attributes.
    """
    overlay_config = {
        "environment": env,
        "cache": False,
        "attributes": {"_overridden": False},
        "extensions": [ext for ext in env.extensions]
    }

    # Create a new environment configuration template
    template_str = """
{% macro create_overlay(env):
    overlay_config = {
        "environment": env,
        "cache": {{ env.cache }},
        "attributes": {{ env.attributes }},
        "extensions": {{ env.extensions }}
    }
    return overlay_config
%}
"""

    # Load the template
    template = Template(template_str)

    # Render the template with the overlays environment context
    new_env = template.render(env=env, cache=False, attributes={"_overridden": False})

    return new_env
