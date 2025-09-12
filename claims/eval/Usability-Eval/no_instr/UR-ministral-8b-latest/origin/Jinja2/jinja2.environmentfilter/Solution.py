import jinja2

def my_custom_decorator(func):
    def wrapper(env, *args, **kwargs):
        @jinja2.tasks.run
        def inner_wrapper():
            func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@my_custom_decorator
def my_function(env, *args, **kwargs):
    template = env.get_template('hello_world.html')
    return template.render(context={})

if __name__ == "__main__":
    env = jinja2.Environment()
    result = my_function(env)
