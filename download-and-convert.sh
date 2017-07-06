#!/usr/bin/env bash

# Download the dataset

python download-dataset.py train-input temp
python download-dataset.py train-labels temp
python download-dataset.py test-input temp

# Convert multi-tiff to a series of single png

python convert-dataset.py \
  --input temp/train-input.tif \
  --output stack1/raw/
python convert-dataset.py \
  --input temp/train-labels.tif \
  --output stack1/regions/
python convert-dataset.py \
  --input temp/train-input.tif \
  --output stack2/raw/

# rm -rf temp

