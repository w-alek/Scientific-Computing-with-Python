import os
from PIL import Image
import numpy as np
import preprocessing
from helper import resize_func, copy, looking
from settings import DATA_PATH, RESULTS_PATH, WIDTH, HEIGHT, PREPROCESS_FUNC, EXTENSION, EPSILON


def func(path: str, resize: tuple, preprocess: str, extension: str) -> None:
    '''
    Main function which applies preprocessing.
    Parameters
    ----------
    path: Data directory rooted at path.
    resize: Resize parameters (width, height) packed in tuple.
    preprocess: Type of preprocessing.
    extension: Extension save format.
    Returns
    -------
    None
    Raises
    ------
    ValueError
        If preprocessing is not supported.
    '''
    modified_path = os.path.join(RESULTS_PATH, 'modified', str(resize[0]) +'x' + str(resize[1]), preprocess)
    orig_path = os.path.join(RESULTS_PATH, 'original')
    os.makedirs(modified_path, exist_ok=True)
    os.makedirs(orig_path, exist_ok=True)
    if preprocess == 'global_centering':
        preprocess_func = preprocessing.global_centering
    elif preprocess == 'local_centering':
        preprocess_func = preprocessing.local_centering
    elif preprocess == 'global_standarization':
        preprocess_func = preprocessing.global_standarization
    elif preprocess == 'local_standarization':
        preprocess_func = preprocessing.local_standarization
    elif preprocess == 'zca':
        preprocess_func = preprocessing.zca
    else:
        raise ValueError (f'{preprocess} is not supported version of preprocessing')
    copy(path, orig_path)
    copy(path, modified_path)
    looking(modified_path)
    if preprocess_func != preprocessing.zca:
        for root, dirs, files in os.walk(modified_path):
            for file in files:
                img = Image.open(os.path.join(root, file))
                resized_img = resize_func(img, *resize)
                preprocess_img = preprocess_func(resized_img)
                preprocess_img.save(os.path.join(root, file.split('.')[0]), format=extension)
                os.remove(os.path.join(root, file))
    else:
        all_images, root_list, files_list = [], [], []
        for root, dirs, files in os.walk(modified_path):
            for file in files:
                img = Image.open(os.path.join(root, file))
                resized_img = resize_func(img, *resize)
                img_np = np.asarray(resized_img)
                all_images.append(img_np)
                os.remove(os.path.join(root, file))
                root_list.append(root)
                files_list.append(file)
        all_images = np.asarray(all_images)
        X_ZCA = preprocess_func(all_images, EPSILON)
        X_ZCA_rescaled = (X_ZCA - X_ZCA.min()) / (X_ZCA.max() - X_ZCA.min())
        X_ZCA_rescaled = X_ZCA_rescaled.reshape(all_images.shape[0], all_images.shape[1], all_images.shape[2], all_images.shape[3])
        for i in range(X_ZCA_rescaled.shape[0]):
            pil_image = Image.fromarray((X_ZCA_rescaled[i] * 255).astype(np.uint8))
            pil_image.save(os.path.join(root_list[i], files_list[i].split('.')[0]), format=extension)

if __name__ == '__main__':
    func(DATA_PATH, (WIDTH, HEIGHT), PREPROCESS_FUNC, EXTENSION)
    print('Done')

