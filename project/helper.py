import os
import PIL
from PIL import Image
from shutil import copytree


def resize_func(img: Image.Image, width: int, height: int) -> Image.Image:
    '''
    Function for resizing image.
    Parameters
    ----------
    img: An instance of the Image class from PIL library.
    width: Width of resized image.
    height: Height of resized image.
    Returns
    -------
    Image.Image
               An instance of the Image class from PIL library.
    '''
    return img.resize((width, height))


def copy(src: str, dest: str) -> None:
    '''
    Recursively copy an entire directory tree rooted at src to a directory
    named dst and return the destination directory using copytree.
    Parameters
    ----------
    src: Directory rooted at src.
    dest: Destination directory.
    Returns
    -------
    None
    '''
    copytree(src, dest, dirs_exist_ok=True)
    print(f'Copied files from {src} to {dest}')


def looking(path: str) -> None:
    '''
    Check supported PIL file formats in a directory tree.
    Parameters
    ----------
    path: Directory rooted at path.
    Returns
    -------
    None
    Raises
    ------
    PIL.UnidentifiedImageError
        If file format is not supported by PIL.
    Notes
    -----
    If file format is not supported by PIL it will be removed.
    '''
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                Image.open(os.path.join(root, file))
            except PIL.UnidentifiedImageError:
                print('Not supported PIL format for', os.path.join(root, file), '- this file will be removed')
                os.remove(os.path.join(root, file))