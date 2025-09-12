from jinja2 import Environment, FileSystemLoader

# Create the original environment
original_env = Environment(loader=FileSystemLoader('templates'))

# Create the overlay environment
overlay_env = original_env.overlay(autoescape=True, optimized=True)
