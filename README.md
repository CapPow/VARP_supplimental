# VARP_supplimental
Supplimental information for __Performant Barcode Decoding for Herbarium Specimen Images Using Vector Assisted Region Proposals (VARP)__

## Command Line Interface
A simple command line interface is provided for VARP decoding. An example image ([example_img.jpg](https://github.com/CapPow/VARP_supplimental/blob/master/example_img.jpg)) is also provided. Users are encouraged to explore the available optional parameters which are explained in the "--help" documentation.


Example usage: 
~~~
# clone this repo and navigate to the new directory
git clone https://github.com/CapPow/VARP_supplimental/edit/master/README.md
cd VARP_supplimental

# check help documentation and decode the example image, using some optional parameters
python VARP_decode.py --help 
python VARP_decode.py "example_img.jpg" --keep_annotations True, --save_by_bc True
~~~
__Note:__ Due to dependency imports, the command line interface is expected to perform slighly slower than in the evaluations. During evaluations, all methods were instantiated before time tests since processing multiple images is intended use-case.

## Evaluation Process
Results and source data for each image in the test dataset is documented in [data_set.csv](https://github.com/CapPow/VARP_supplimental/blob/master/data_set.csv).<br />
The evaluation process is documented in [VARP_evaluation.ipynb](https://github.com/CapPow/VARP_supplimental/blob/master/VARP_evaluation.ipynb).
