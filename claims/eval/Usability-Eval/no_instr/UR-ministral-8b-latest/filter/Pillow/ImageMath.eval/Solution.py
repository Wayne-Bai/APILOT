from PIL import Image, ImageOps

def evaluate_image_expressions(image_path, expression, replace_dict):
    """
    Evaluates an image expression and returns the result image.

    Parameters:
    - image_path: Path to the input image.
    - expression: A string expression where key and values are template placeholders.
    - replace_dict: A dictionary to replace the key-placeholders with their respective images.

    Returns:
    - result_image: The final image after evaluating the expression.
    """
    # Load the input image
    image = Image.open(image_path)

    # Parse and apply the template-wise expression
    for key, expr in replace_dict.items():
        if key in expression:
            placeholders = f"{{{{ {key} }}}}"
            image = image.replace_paste(expr[1], expression.format(replace_dict[key]), expr[0])

    return image

# Example usage
if __name__ == '__main__':
    # Load images from files
    cat_image = Image.open("cat.jpg")
    dog_image = Image.open("dog.jpg")

    # Define the expression with template placeholders
    expression = "Replace with {key} and over {overlay}"

    # Define the replace_dict
    replace_dict = {
        "cat": ("cat_mask.png", cat_image),
        "dog": ("dog_mask.png", dog_image)
    }

    # Define the expressions for overlays
    overlay = cat_image.resize((200, 200))

    final_image = evaluate_image_expressions("main_image.jpg", expression, replace_dict)

    # Save final image
    final_image.save("final_image.jpg")
