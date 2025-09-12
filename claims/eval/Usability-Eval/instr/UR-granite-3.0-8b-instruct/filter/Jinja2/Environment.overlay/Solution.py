from jinja2 import Environment, FileSystemLoader

class OverlayEnvironment:
    def __init__(self, base_env, override_attributes=None):
        self.base_env = base_env
        self.override_attributes = override_attributes or {}
        self.env = Environment(
            loader=FileSystemLoader(base_env.loader.path),
            extensions=base_env.extensions,
            autoescape=base_env.autoescape,
            trim_blocks=base_env.trim_blocks,
            lstrip_blocks=base_env.lstrip_blocks,
        )
        self.env.filters.update(base_env.filters)
        self.env.tests.update(base_env.tests)
        self.env.globals.update(base_env.globals)
        self.env.environment.attributes.update(base_env.environment.attributes)

    def get_template(self, template_name):
        template = self.base_env.get_template(template_name)
        for attr, value in self.override_attributes.items():
            setattr(template, attr, value)
        return template
