# FIJI_Scripts
FIJI/ImageJ Scripts for post hoc processing of worm tracking image sequences

These scripts convert an image sequence of .bmp files collected from a CMOS camera (e.g. Mightex) into a processed .tif file suitable for post hoc manual worm tracking.

Repository includes scripts for a single camera Chemotaxis Tracking setup, and for a dual camera Thermotaxis Tracking setup. 

## Chemotaxis Image Import Scripts
Includes versions for two lighting conditions:
* Raw camera image shows a light worm against a dark background (e.g. dark field illumination)
* Raw camera image shows a dark worm against a light background (e.g. bright field illumination)

## Thermotaxis Image Import Scripts
Assumes a camera configuration where the two cameras tile the width of a thermotaxis plate. Also assumes data were collected using dark field illumination.
Two versions are included: one written in the ImageJ Macro language, and one written using Python that is generally equivalent. The .ijm version is the primary version.
