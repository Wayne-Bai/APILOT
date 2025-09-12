from svgwrite import Drawing

# Create a new drawing
d = Drawing()

# Add a rectangle (2-dimensional vector data)
d.add(d.rect(insert=(50, 50), size=(100, 50), fill='blue'))

# Save the drawing to an SVG file
d.save('vector_data.svg')
