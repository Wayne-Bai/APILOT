from jinja2 import Template

def create_bytecode_cache(directory, pattern):
    # Define a template string containing dynamic content
    template = """
{% if directory %}
These settings will store the bytecode cache in "{{ directory }}" directory.
{% else %}
So sorry about the trouble. Directory for cache is necessary.
{% endif %}

Pattern: "{{ pattern }}"
"""

    # Parse the template and render it with the required variable
    rendered = Template(template).render(directory=directory, pattern=pattern)
    print(rendered)
