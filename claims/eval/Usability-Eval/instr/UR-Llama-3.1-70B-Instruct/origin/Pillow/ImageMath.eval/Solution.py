# Importing necessary libraries from Pillow
from PIL import Image, ImageDraw, ImageFont

# Open an image file
def open_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

# Evaluate an image expression by drawing text onto the image
def evaluate_image_expression(img, expression, position=(10, 10)):
    try:
        # Create a drawing context
        drawing_context = ImageDraw.Draw(img)

        # Set the font and font size
        font = ImageFont.load_default()
        font_size = 20

        # Draw the text on the image
        drawing_context.text(position, text=expression, fill=(255, 255, 255), font=font, stroke_width=2)

        return img
    except Exception as e:
        print(f"Error evaluating image expression: {e}")
        return None

# Save the evaluated image
def save_image(img, output_path):
    try:
        img.save(output_path)
    except Exception as e:
        print(f"Error saving image: {e}")

# Main function
def main():
    # Open the image
    img = open_image("input.jpg")
    
    if img is not None:
        # Evaluate the image expression
        expression = "Hello, World!"
        evaluated_img = evaluate_image_expression(img, expression)

        if evaluated_img is not None:
            # Save the evaluated image
            save_image(evaluated_img, "output.jpg")

if __name__ == "__main__":
    main()
