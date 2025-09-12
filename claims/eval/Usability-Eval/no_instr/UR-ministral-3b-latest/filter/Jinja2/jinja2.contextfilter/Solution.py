from jinja2 import Environment

def process_content(context):
    env = Environment()
    env.globals = context
    template = env.from_string(template_string)
    return template.render()

def main():
    # Example context
    context = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }

    # Your template string should go here
    template_string = """
    <div>
        <h1>{{ name }}</h1>
        <p>Age: {{ age }}</p>
        <p>City: {{ city }}</p>
    </div>
    """

    result = process_content(context)
    print(result)
