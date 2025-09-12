from PIL import Image

def evaluate_image_expression(image_path, expression):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to RGB if it's not
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Split the expression into operands and operators
    operands = expression.split()
    operators = ['+', '-', '*', '/']

    # Evaluate the expression
    result = operands[0]
    for i in range(1, len(operands), 2):
        operand1 = operands[i-1]
        operand2 = operands[i]
        if operand2 in operators:
            if operand2 == '+':
                result += operand1
            elif operand2 == '-':
                result -= operand1
            elif operand2 == '*':
                result *= operand1
            elif operand2 == '/':
                result /= operand1

    return result

# Example usage:
image_path = 'path/to/your/image.jpg'
expression = '2+2*3/4'
result = evaluate_image_expression(image_path, expression)
print(result)
