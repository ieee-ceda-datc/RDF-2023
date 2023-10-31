#!/bin/bash
export powerIntScale=$1
export powerSwScale=$2
python liberty_tbl_scale_power.py $powerIntScale  $powerSwScale  ./delay_scaled/NangateOpenCellLibrary_typical.lib > NangateOpenCellLibrary_typical.lib
