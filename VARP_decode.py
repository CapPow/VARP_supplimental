#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:28:41 2020
@author: Caleb Powell
@email: CalebAdamPowell@gmail.com

A simple command line interface for testing the VARP method on single images

Note: This interface is provided as an easy to use proof of concept.
Instantiating these methods on a per-image basis is expected to slow the 
process somewhat as dependencies must be imported for each image. During speed
testing, all methods were instantiated beforehand on the expectation that 
decoding methods would typically be instantiated on start up and used across
multiple images. 

To minimize dependencies the input image file (--in_img) is expected to be a
common derivative image format (e.g., jpg, png). An example of implimenting 
VARP with a RAW image format, see HerbASAP at https://github.com/CapPow/HerbASAP

"""
import argparse
import cv2
import os
# import the modified pyzbar library
from deps.bcRead import *

# set up argparsing
parser = argparse.ArgumentParser(description="A simple command line interface "
                                "for testing the VARP method on single images")

parser.add_argument('in_img', type=str,
                    help='required path to the input image file. Note: expects'
                    ' a common derivative image format (e.g., jpg, png)')

parser.add_argument('--keep_annotations', type=str,
                    default="True",
                    help='optional bool, whether to save annotated images'
                    'which illustrate the VARP process (default: True)')

parser.add_argument('--save_by_bc', type=str,
                    default="False",
                    help='optional bool, whether to save a copy of the input '
                    'image file named according to the decoded barcode '
                    'value(s) (default: False)')

parser.add_argument('--regex_pattern', type=str,
                    default="",
                    help='optional string representing a python regex pattern '
                    'if provided, will only return decoded values which match '
                    'the regex pattern. If not provided, will return all '
                    'decoded values (default: "" empty string, no pattern '
                    'matching)')

parser.add_argument('--extension_value', type=int,
                    default=6,
                    help='optional integer representing vector extension '
                    'factor. Calculated as the smaller image dimension divided'
                    ' by the extension_value. Vector extensions are aplied on '
                    'each side of every identified rectangle. (default:6)')

parser.add_argument('--use_fallbacks', type=str,
                    default="True",
                    help='optional bool, whether to use fallback methods if '
                    'initially no barcode(s) are found (default: True)')

# parse user arguments
args = parser.parse_args()

# adapt to goofy argparsing's handling of bool
def str_to_bool(value):
    """ convert the boolean inputs to actual bool objects"""
    if value.lower() in {'false', 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
        return True
    raise ValueError(f'{value} is not a valid boolean value')

args.keep_annotations = str_to_bool(args.keep_annotations)
args.save_by_bc = str_to_bool(args.save_by_bc)
args.use_fallbacks = str_to_bool(args.use_fallbacks)

# load the input image file as an openCV array
in_img = cv2.imread(args.in_img)
# instantiate the VARP_reader class imported from bcRead
VARP_reader = bcRead(patterns=args.regex_pattern)

# attempt to retrieve barcode values
# if seperate images should be saved which illustrate the VARP process
if args.keep_annotations:
    codes = VARP_reader.extract_by_squares_with_annotation(in_img,
                                                args.in_img,
                                                retry=args.use_fallbacks,
                                                extension=args.extension_value)
else:
    codes = VARP_reader.extract_by_squares(in_img,
                                           retry=args.use_fallbacks,
                                           extension=args.extension_value)

# decode each code found from bytes to utf-8
bc_values = [x.data.decode('utf-8') for x in codes]
# optionally filter the results by regex pattern
if args.regex_pattern != "":
    bc_values = [x for x in bc_values if VARP_reader.rePattern.match(x)]

# container to store the file paths of any written images
written_images = []

if args.keep_annotations:
    base_fn = args.in_img.rsplit(".", 1)[0]
    # for each possible annotation file
    for fn in [base_fn + "_squares.jpg",
               base_fn + "_vectors.jpg",
               base_fn + "_composite.jpg"]:
        # if it exists
        if os.path.isfile(fn):
            # append it to the written_images list
            written_images.append(fn)

if args.save_by_bc:
    img_folder = os.path.dirname(os.path.abspath(args.in_img))
    for bc_value in bc_values:
        fpath = os.path.join(img_folder, bc_value +'.jpg')
        cv2.imwrite(fpath, in_img)
        written_images .append(fpath)

# print the results
print("") #empty line for neat output formatting
for written_image in written_images:
    print("File Written: ", written_image)

print("") #empty line for neat output formatting

if len(bc_values) > 0:
    print("Decoded barcode values: ", ", ".join(bc_values))
else:
    print("No barcode values decoded!")

print("") #empty line for neat output formatting