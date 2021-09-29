import numpy as np
from PIL import Image


def global_centering(img: Image.Image) -> Image.Image:
    '''
    Perform Global Centering.
    Parameters
    ----------
    img: An instance of the Image class from PIL library.
    Returns
    -------
    Image.Image:
                An instance of the Image class from PIL library.
    '''
    img_np = np.asarray(img)
    img_np = img_np.astype('float64')
    mean = img_np.mean()
    img_np -= mean
    return Image.fromarray(img_np.astype(np.uint8))


def local_centering(img: Image.Image) -> Image.Image:
    '''
    Perform Local Centering.
    Parameters
    ----------
    img: An instance of the Image class from PIL library.
    Returns
    -------
    Image.Image: 
                An instance of the Image class from PIL library.
    '''
    img_np = np.asarray(img)
    img_np = img_np.astype('float64')
    mean = img_np.mean(axis=(0,1), dtype='float64')
    img_np -= mean
    return Image.fromarray(img_np.astype(np.uint8))


def global_standarization(img: Image.Image) -> Image.Image:
    '''
    Perform Global Standarization.
    Parameters
    ----------
    img: An instance of the Image class from PIL library.
    Returns
    -------
    Image.Image:
                An instance of the Image class from PIL library.
    '''
    img_np = np.asarray(img)
    img_np = img_np.astype('float64')
    mean, std = img_np.mean(), img_np.std()
    img_np = (img_np - mean)/std
    return Image.fromarray(img_np.astype(np.uint8))


def local_standarization(img: Image.Image) -> Image.Image:
    '''
    Perform Local Standarization.
    Parameters
    ----------
    img: An instance of the Image class from PIL library.
    Returns
    -------
    Image.Image: 
                An instance of the Image class from PIL library.
    '''
    img_np = np.asarray(img)
    img_np = img_np.astype('float64')
    mean = img_np.mean(axis=(0,1), dtype='float64')
    std = img_np.std(axis=(0,1), dtype='float64')
    img_np = (img_np - mean)/std
    return Image.fromarray(img_np.astype(np.uint8))

def zca(images: Image.Image, epsilon: float) -> np.ndarray:
    '''
    Perform ZCA Whitening (https://ieeexplore.ieee.org/document/7808140).
    Parameters
    ----------
    images: An instance of the Image class from PIL library.
    epsilon: Effet of whitening
    Returns
    -------
    np.ndarray: 
                Numpy array that consits all images after ZCA.
    '''

    img_np = images.reshape(images.shape[0], images.shape[1] * images.shape[2] * images.shape[3])
    img_centered = img_np / 255
    img_centered = img_centered - img_centered.mean(axis=0)
    cov = np.cov(img_centered, rowvar=False)
    U, S, V = np.linalg.svd(cov)
    X_ZCA = U.dot(np.diag(1.0/np.sqrt(S + epsilon))).dot(U.T).dot(img_centered.T).T
    return X_ZCA