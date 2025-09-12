from jinja2 import Environment, select_autoescape

# Create the base environment
base_env = Environment(
    loader=SomeLoader(),
    autoescape=select_autoescape(['html', 'xml']),
    extensions=['jinja2_time.TimeExtension'],
    # Other base environment settings...
)

# Create the overlay environment
overlay_env = base_env.overlay(
    loader=base_env.loader,
    autoescape=base_env.autoescape,
    extensions=base_env.extensions,
    # Other overlay environment settings...
)
