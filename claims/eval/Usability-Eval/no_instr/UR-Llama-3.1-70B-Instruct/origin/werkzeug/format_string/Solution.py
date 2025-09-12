from werkzeug import Template

# Define the template string
template_string = '''
<div>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</div>
'''

# Create a Template object
template = Template(template_string)

# Define the data to be rendered
data = {
    "title": "Hello, World!",
    "message": "This is a test message",
    "items": ["Item 1", "Item 2", "Item 3"]
}

# Render the template
rendered_template = template.render(data)

# Print the rendered template
print(rendered_template)
