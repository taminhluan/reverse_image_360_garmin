import os
import sys

parent_dirs = os.listdir('')

for parent_dir in parent_dirs:
    dirs = os.listdir(parent_dir)
    for dir in dirs:
        image = os.listdir(f'{parent_dir}/{dir}')
        print(f'{parent_dir}/{dir}/{image}')


