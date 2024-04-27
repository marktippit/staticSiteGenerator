import os
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_page, generate_pages_recursive

from_path = "./content/"
dest_path = "./public/"
template_path = "./template.html"

def main():
    generate_pages_recursive(from_path, template_path, dest_path)
    

main()