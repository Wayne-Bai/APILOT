import os
from jinja2 import Environment, FileSystemLoader
cache_dir = "/path/to/cache/directory"
pattern = "mypattern"
env = Environment(loader=FileSystemLoader(searchpath=cache_dir))
templates = env.glob(pattern)
for template in templates:
    bytecode = env.get_template(template).compile()
    with open(os.path.join(cache_dir, template + ".bytecode"), "wb") as f:
        f.write(bytecode)
