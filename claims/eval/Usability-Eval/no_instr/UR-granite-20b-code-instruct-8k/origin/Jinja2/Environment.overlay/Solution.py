from jinja2 import Environment, FileSystemLoader

# Set up the initial environment
initial_env = Environment(loader=FileSystemLoader('/path/to/templates'))

# Create an overlay environment
overlay_env = initial_env.overlay(autoescape=True)
