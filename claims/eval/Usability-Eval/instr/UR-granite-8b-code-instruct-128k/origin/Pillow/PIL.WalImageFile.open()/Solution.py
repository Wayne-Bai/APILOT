import PIL.Image
# Open the WAL file in binary mode
with open('texture.wal', 'rb') as f:
 # Read the file contents
 data = f.read()
# Create a PIL Image object from the WAL data
image = PIL.Image.open(data)
# Save the image as a PNG file
image.save('texture.png')
