from jinja2 import Template

# Define the Jinja2 template for the bytecode cache
template = Template("""
Cache directory: {{ cache_dir }}
Cache pattern: {{ cache_pattern }}

bytecode cache: {}
""")

# Call usage to print the defined template
print(template.render(cache_dir='/path/to/cache', cache_pattern="*.pyc"))
