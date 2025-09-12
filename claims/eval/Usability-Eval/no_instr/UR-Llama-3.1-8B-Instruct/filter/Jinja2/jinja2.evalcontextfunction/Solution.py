from jinja2 import Template, EvaluationError
from functools import wraps

# Define a function that will serve as a decorator
def pass_eval_context(func):
    """
    Passed the EvalContext as the first argument to the decorated function when called.
    """
    
    # Use the wraps decorator from functools to preserve the metadata of the original function
    @wraps(func)
    def wrapper(eval_context, *args, **kwargs):
        try:
            # Render the template and call the decorated function with the result and additional arguments
            result = func(eval_context, *args, **kwargs)
            return result
        except EvaluationError as e:
            # Handle any exceptions that occur during template rendering or function execution
            return f"An error occurred: {str(e)}"
    
    return wrapper

# Example usage:
# Template rendering and evaluation
template = Template("Hello, {{ name }}!")
eval_context = {"name": "John"}

# Apply the decorator to a function that takes an eval_context and string as arguments
@pass_eval_context
def render_template(eval_context, string):
    result = template.render(name=eval_context.get("name"), string=string)
    return result

# Test the decorator
rendered = render_template(eval_context, "This is a test.")
print(rendered)
