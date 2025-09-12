from flask import Flask
import jinja2

app = Flask(__name__)
app.jinja_env = jinja2.Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=jinja2.FileSystemLoader('templates')
)

@app.context_processor
def inject_variable():
    return {
        'example_variable': 'My super variable!'
    }

@app.route('/')
def home():
    return app.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
