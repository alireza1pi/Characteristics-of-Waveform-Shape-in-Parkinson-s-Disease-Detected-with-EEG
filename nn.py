import numpy as np
def isin(element, test_elements, assume_unique=False, invert=False):
    "..."
    element = np.asarray(element)
    return np.in1d(element, test_elements, assume_unique=assume_unique,
                invert=invert).reshape(element.shape)