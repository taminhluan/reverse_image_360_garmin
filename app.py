import os
import sys

parent_dirs = os.listdir()

for parent_dir in parent_dirs:
    if (os.path.isdir(parent_dir)):
        dirs = os.listdir(parent_dir)
        for dir in dirs:
            images = os.listdir(f'{parent_dir}/{dir}')
            for image in images:
                print(f'{parent_dir}/{dir}/{image}\n')

                split_dir = f'../360_SPLIT/{parent_dir}/{dir}'
                result_dir = f'../360_RESULT/{parent_dir}/{dir}'
                if not os.path.exists(split_dir):
                    os.makedirs(split_dir)
                if not os.path.exists(result_dir):
                    os.makedirs(result_dir)
                os.system(f'magick {parent_dir}/{dir}/{image} -crop 50%x100% +repage {split_dir}/{image}_%02d.jpg')
                os.system(f'convert +append {split_dir}/{image}_01.jpg {split_dir}/{image}_00.jpg {result_dir}/{image}')
                os.system(f'exiftool -TagsFromFile {parent_dir}/{dir}/{image} {result_dir}/{image}')


