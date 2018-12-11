#!/home/simon/anaconda3/bin/python
"""
    author  :
    E-Mail  :
    Date    :
"""

import os
import scipy.ndimage as ndim
import scipy.misc

TMP_FOLDER = "/home/simon/.config/scripts/tmp/"


def main():
    '''
        Main Functon
    '''

    print("HALLO")
    arg = TMP_FOLDER + "i3lock.png"
    os.system("scrot " + arg)
    img = ndim.imread(arg)
    img = scipy.misc.imresize(img, size=5)
    img = scipy.misc.imresize(img, (1440, 5120))
    scipy.misc.imsave(arg, img)
    os.system("i3lock -i "+arg)


if __name__ == "__main__":
    main()
