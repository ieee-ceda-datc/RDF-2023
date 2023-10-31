#!/bin/bash
scaled_lib_direcoty=$1
tcp=$2
util=$3

proj_dir=`pwd | grep -o "/\S*/RDF-2023"`
## Chaneg the design name accordingly
design_name="ng45_jpeg"

suffix=`basename ${scaled_lib_direcoty} | sed 's@scaled_lib@@'`
ref_script="${proj_dir}/scripts/spnr_ng45"

run_dir="${proj_dir}/run/${design_name}${suffix}_${tcp}_${util}"
cp -rf ${ref_script} ${run_dir}
cd ${run_dir}
./run.sh ${tcp} ${util} ${scaled_lib_direcoty}

## Add data extraction part
echo "testcase,target_util,delayDown,pwrDown_int,pwrDown_sw,tcp,tcf,core_area,std_cell_area,worst_neg_slack,effective_clock_period,effective_clock_frequency,internal_power,switching_power,leakage_power,total_power,drc_count" > ${run_dir}/scaled_pnr_data.csv
python3 ${proj_dir}/scripts/util/extract_pnr_metrics_ng45.py ${run_dir} >> ${run_dir}/scaled_pnr_data.csv

