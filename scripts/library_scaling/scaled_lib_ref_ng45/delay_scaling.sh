#!/bin/bash
export delayScale=$1
export project_dir=`pwd | grep -o '/\S*RDF-2023'`
mkdir -p delay_scaled
python liberty_tbl_scale_delay.py $delayScale $project_dir/techlibs/ng45/lib/NangateOpenCellLibrary_typical.lib > ./delay_scaled/NangateOpenCellLibrary_typical.lib
