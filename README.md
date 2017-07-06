# Segmented anisotropic ssSEM dataset of neural tissue

![animation](http://brainiac2.mit.edu/SNEMI3D/sites/default/files/training-data-animation.gif)

This datasets are two stacks of 100 sections from a serial section Scanning Electron Microscopy (ssSEM) data set of the Mouse neocortex, stained with reduced osmium tetroxide-thiocarbohydrazide (TCH)-osmium (“ROTO”).

The microcube measures 6 x 6 x 3 microns approx., with a resolution of 6 x 6 nm/pixel and section thickness of 30 nm.


The image data used in the SNEMI3D challenge was produced by Lichtman Lab at Harvard University (Daniel R. Berger, Richard Schalek, Narayanan "Bobby" Kasthuri, Juan-Carlos Tapia, Kenneth Hayworth, Jeff W. Lichtman) and manually annotated by Daniel R. Berger. If any scientific publications derive from the usage of this data set, you should cite the following publication:

```bibtex
@article{kasthuri2015saturated,
  title={Saturated reconstruction of a volume of neocortex},
  author={Kasthuri, Narayanan and Hayworth, Kenneth Jeffrey and Berger, Daniel Raimund and Schalek, Richard Lee and Conchello, Jos{\'e} Angel and Knowles-Barley, Seymour and Lee, Dongil and V{\'a}zquez-Reina, Amelio and Kaynig, Verena and Jones, Thouis Raymond and others},
  journal={Cell},
  volume={162},
  number={3},
  pages={648--661},
  year={2015},
  publisher={Elsevier}
}
```


### Content
  
```
├── stack1
│   ├── raw: The raw 8-bit greyscale images (1)
│   ├── regions: Three-dimensional segmentation into neurons/regions (1)
│   ├── membranes: Series of binary images of segmented membranes (2)
│   └── overlap: Series of binary images of overlap between adjacent regions (2)
└── stack2
    └── raw: The raw 8-bit greyscale images (1)
```

Notes:
1. downloaded and converted from SNEMI3D dataset
2. generated


## Requirements

- Python 2 or 3
- Tifffile
- Skimage

## How to use

Run the bash script ```download-and-convert.sh``` inside the folder or:

### Download the dataset

```bash
python download-dataset.py train-input datasets/snemi3d
python download-dataset.py train-labels datasets/snemi3d
python download-dataset.py test-input datasets/snemi3d
```

Convert multi-tiff to a series of single png

```bash
python convert-dataset.py \
  --input datasets/snemi3d/train-input.tif \
  --output datasets/snemi3d/train_input/
python convert-dataset.py \
  --input datasets/snemi3d/train-labels.tif \
  --output datasets/snemi3d/train_labels/
```

### TODO

Conversion of region segmentation into membrane labels and overlap labels.

### Modifications

The following conversions/modifications have been applied to the orginal SNEMI3D dataset:
- All images are converted to portable network graphics (png) format
- Organization of dataset similar to the [Segmented anisotropic ssTEM dataset of neural tissue](https://github.com/tbullmann/groundtruth-drosophila-vnc) from the Drosophila ventral nerve cord.

## Original

Website: [ISBI 2013 challenge: 3D segmentation of neurites in EM images](http://brainiac2.mit.edu/SNEMI3D/)

Contact: [Daniel Berger](https://lichtmanlab.fas.harvard.edu/people/daniel-berger)

