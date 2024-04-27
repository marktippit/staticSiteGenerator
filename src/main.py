import os
import shutil

from copystatic import copy_files_recursive

from_path = "./"
dir_path_static = "../static"
dir_path_public = "./public"


def main():
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()