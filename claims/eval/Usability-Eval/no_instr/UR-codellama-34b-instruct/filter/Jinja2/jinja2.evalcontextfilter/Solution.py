from jinja2 import Environment, evalcontextfilter

# create a new Jinja2 environment
env = Environment()

# define a decorator that accepts a function and returns a new function that passes the EvalContext as the first argument
def my_decorator(func):
    @evalcontextfilter
    def wrapper(*args, **kwargs):
        # pass the EvalContext as the first argument to the decorated function
        return func(env.eval_context, *args, **kwargs)
    return wrapper

# use the decorator on a template function
@my_decorator
def my_template_function(ctx):
    # access the EvalContext in the function body
    print("EvalContext:", ctx)

# render the template with the decorated function
env.from_string('{% macro my_macro() %}Hello, world!{{ my_template_function() }}{% endmacro %}').render(my_macro=my_macro())
