import jinja2
cache = jinja2.bccache.BucketCache('/tmp/jinja2_cache',
patterns=['{filename}.py', '{filename}_{mtime}.py'])
jinja2.Template.cache_class = cache
