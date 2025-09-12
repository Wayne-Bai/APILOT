from PIL import Image, ImageDraw

# Function to create a simple 2D vector representation
def create_vector_image(width, height, vector_start, vector_end, output_path):
    # Create a new blank image
    img = Image.new('RGB', (width, height), color='white')
    
    # Create a Draw object
    draw = ImageDraw.Draw(img)
    
    # Draw the vector as a line
    draw.line([vector_start, vector_end], fill='black', width=3)
    
    # Save the image
    img.save(output_path)

# Example usage
width = 400
height = 400
vector_start = (100, 200)
vector_end = (300, 200)
output_path = 'vector_image.png'

create_vector_image(width, height, vector_start, vector_end, output_path)
