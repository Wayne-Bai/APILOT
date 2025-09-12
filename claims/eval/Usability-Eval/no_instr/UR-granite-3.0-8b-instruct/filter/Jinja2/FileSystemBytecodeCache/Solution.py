from jinja2 import Environment, FileSystemLoader

def generate_cache_filename(directory, pattern):
    return f"{directory}/{pattern}.pyc"

def generate_cache_path(directory, pattern):
    return generate_cache_filename(directory, pattern)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cache_template.txt')

cache_directory = "path/to/cache/directory"
cache_pattern = "my_module"

cache_path = generate_cache_path(cache_directory, cache_pattern)
cache_filename = template.render(cache_path=cache_path)

print(cache_filename)
