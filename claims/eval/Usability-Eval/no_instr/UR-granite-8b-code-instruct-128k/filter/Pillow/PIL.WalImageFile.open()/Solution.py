from PIL import Image
# Open the image file
img = Image.open('quake2_texture.wal')
# Convert the image to RGB mode
img = img.convert('RGB')
# Save the image as a new file
img.save('quake2_texture.png')
