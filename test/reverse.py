import sys
from PIL import Image

image = Image.open('V0051076_2.JPG')

width, height = image.size
result = Image.new('RGB', (width, height))

im1 = image.crop((0, 0, width//2, height))
im2 = image.crop((width//2, 0, width, height))


result.paste(im1, (0, 0))
result.paste(im2, (width//2, 0))

result.save('result_reverse.mpo', format='MPO')

