from PIL import Image
import requests

# Function to generate color palette
def generate_color_palette(image_url):
    # Download image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Generate color palette
    palette = image.getpalette()
    color_palette = [palette[i:i+3] for i in range(0, len(palette), 3)]

    return color_palette

# Example usage
image_url = "https://example.com/image.jpg"
color_palette = generate_color_palette(image_url)
print(color_palette)
