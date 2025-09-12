from PIL import Image

def create_palette_mapped_image(input_image_path, output_image_path, palette_file_path):
    with Image.open(input_image_path) as img:
        # Create a palette from the image
        palette = img.getpalette()

        def remap_image(img, palette):
            # Convert the image data to PIL Raster
            pixels_list = list(img.getdata())
            # Make a new list of pixels with the palette mapped
            mapped_pixels_list = []
            for px in pixels_list:
                pixel_index = px[0] + (px[1] * 256) + (px[2] * 65536)
                mapped_pixel = palette[pixel_index]
                mapped_pixels_list.append(mapped_pixel)

            # Update the image data with the palette mapped pixels
            img.putdata(mapped_pixels_list)

        remap_image(img, palette)

    # Save the palette mapped image
    img.save(output_image_path)

# Example usage
create_palette_mapped_image('input_image.png', 'output_image.png', 'palette.pal')
