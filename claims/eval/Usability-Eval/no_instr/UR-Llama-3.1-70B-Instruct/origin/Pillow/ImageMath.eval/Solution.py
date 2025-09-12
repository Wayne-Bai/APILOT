# Import the necessary Pillow library
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Evaluate an image expression: Open an Image file
def evaluate_image_expression(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Get image size
        width, height = image.size
        
        # Get image mode
        mode = image.mode
        
        # Get image format
        format = image.format
        
        # Display the image size, mode, and format
        print(f"Image Size: {width}x{height}")
        print(f"Image Mode: {mode}")
        print(f"Image Format: {format}")
        
        # Resize the image (Optional)
        # image = image.resize((800, 600))
        
        # Convert image to grayscale (Optional)
        # image = image.convert('L')
        
        # Apply image filter (Optional)
        # image = image.filter(ImageFilter.GaussianBlur(radius=5))
        
        # Show the image
        image.show()
        
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
evaluate_image_expression('path_to_your_image.jpg')
