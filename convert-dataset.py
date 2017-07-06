from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings
import argparse
import os
import tifffile
from skimage.io import imsave


parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="input path/files")
parser.add_argument("--output", required=True, help="output path/files")
a = parser.parse_args()


def main():
    # converting multi-tiff to a series of png

    input_filename = a.input
    output_dir = a.output

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    stack = tifffile.imread(input_filename)
    for index, image in enumerate(stack):
        output_filename = output_dir + "%d.png" % index
        with warnings.catch_warnings():  # suppress "low contrast image" warning while saving 16bit png with labels
            warnings.simplefilter("ignore")
            imsave(output_filename, image)

    print ("Saved %d images to %s." % (index+1, output_dir))


main()
