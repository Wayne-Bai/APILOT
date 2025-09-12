from flask import Flask, render_template
from jinja2 import Environment, BaseLoader

app = Flask(__name__)

# Custom Kernel object to pass eval context
class CustomKernel:
    def run_code(self, code):
        # Just an example stub, you can add your code execution logic here
        print(f"Running code: {code}")

# Processor to evaluate code in context
class Processor:
    def __init__(self, kernel):
        self.kernel = kernel

    def process(self, code):
        # Here, you would pass and probably run the given code within the kernel context
        return self.kernel.run_code(code)

# Custom EvalContext
class CustomEvalContext:
    def __init__(self, processor):
        self.processor = processor

    def evaluate(self, code):
        # Here, we should use processor to execute given code
        self.processor.process(code)
        return self.processor(processor=processor)

# TemplateLoader and Environment setup
loader = BaseLoader()
env = Environment(loader=loader)

@app.route('/render_template/<eval_code>')
def render_template_test(eval_code):
    eval_context = CustomEvalContext(Processor(CustomKernel()))
    eval_context.evaluate(eval_code)

    template = env.from_string("This is a test template", "test/context.html")
    with tempfile.NamedTemporaryFile("w") as tmp:
        template.render(eval_context=eval_context)
        return template.render(eval_context=eval_context)

if __name__ == '__main__':
    app.run()
