# VARP_supplimental
Supplimental information for __Performant Barcode Decoding for Herbarium Specimen Images Using Vector Assisted Region Proposals (VARP)__

__Note:__ All code provided in this repository was written in python 3.8

## Command Line Interface
A simple command line interface is provided for VARP decoding. An example image ([example_img.jpg](https://github.com/CapPow/VARP_supplimental/blob/master/example_img.jpg)) is also provided. Users are encouraged to explore the available optional parameters which are explained in the "--help" documentation. For example, using a too large extension value (e.g., 20) on the example image will reduce the composite image size but produce insufficient vectors and fail to decode. 


Example usage: 
~~~
# clone this repo and navigate to the new directory
git clone https://github.com/CapPow/VARP_supplimental
cd VARP_supplimental

# install dependencies
pip install -r requirements.txt

# check help documentation and decode the example image, using an optional parameter
python VARP_decode.py --help 
python VARP_decode.py "example_img.jpg" --save_by_bc True

~~~
This could be used with simple command line scripting to rename an entire directory.

Bash example:
~~~
# decode all jpg files present in a nested subdirectory named "./imgs/"
$for i in ./imgs/*.jpg;do python VARP_decode.py "$i" --save_by_bc True --keep_annotations False;done

~~~
__Note:__ Due to dependency imports, the command line interface is expected to perform slighly slower than in the evaluations. During evaluations, all methods were instantiated before time tests which represents intended use-case conditions.

## Evaluation Process
Results and source data for each image in the test dataset is documented in [data_set.csv](https://github.com/CapPow/VARP_supplimental/blob/master/data_set.csv).<br />
The evaluation process is documented in [VARP_evaluation.ipynb](https://github.com/CapPow/VARP_supplimental/blob/master/VARP_evaluation.ipynb).
