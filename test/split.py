import image_slicer
tiles = image_slicer.slice('V0051076_2.JPG', 2, save=False)
join = image_slicer.join(tiles).save('V0051076_2_RESULT.JPG')
# image_slicer.save_tiles(tiles, prefix='slice', directory='.', format='PNG')


# JOIN
# import sys
# from PIL import Image

# images = [Image.open(x) for x in ['slice_01_02.png', 'slice_01_01.png']]
# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('result2.jpg')
