from jinja2 import Environment, FileSystemLoader

def generate_cache_filename(directory, pattern):
    return f"{directory}/{pattern}"

def main():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('cache_filename.jinja2')
    cache_filename = template.render(directory='cache_dir', pattern='cache_pattern')
    print(cache_filename)

if __name__ == '__main__':
    main()
