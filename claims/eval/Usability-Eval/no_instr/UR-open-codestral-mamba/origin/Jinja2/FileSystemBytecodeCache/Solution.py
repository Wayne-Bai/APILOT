import jinja2

def build_filename(directory, pattern):
    return jinja2.ByteCodeCache(directory, pattern)

# Now you can call the function with directory and pattern arguments
cache_folder = '/path/to/cache'
cache_pattern = '%(basename)s.%(modtime)d.cache'
bytecode_cache = build_filename(cache_folder, cache_pattern)
