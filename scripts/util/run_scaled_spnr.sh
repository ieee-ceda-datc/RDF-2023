#!/bin/bash
scaled_lib_direcoty=$1
tcp=$2
util=$3

proj_dir=`pwd | grep -o "/\S*/RDF-2023"`
## Chaneg the design name accordingly
design_name="asap7_jpeg"

suffix=`basename ${scaled_lib_direcoty} | sed 's@scaled_lib@@'`
ref_script="${proj_dir}/scripts/spnr"

run_dir="${proj_dir}/run/${design_name}${suffix}_${tcp}_${util}"
cp -rf ${ref_script} ${run_dir}
cd ${run_dir}
./run.sh ${tcp} ${util} ${scaled_lib_direcoty}

## Add data extraction part
echo "testcase,target_util,delayDown_RVT,delayDown_LVT,delayDown_SLVT,pwrDown_int_RVT,pwrDown_int_LVT,pwrDown_int_SLVT,pwrDown_sw_RVT,pwrDown_sw_LVT,pwrDown_sw_SLVT,tcp,tcf,core_area,std_cell_area,worst_neg_slack,effective_clock_period,effective_clock_frequency,internal_power,switching_power,leakage_power,total_power,drc_count" > ${run_dir}/scaled_pnr_data.csv
python3 ${proj_dir}/scripts/util/extract_pnr_metrics.py ${run_dir} >> ${run_dir}/scaled_pnr_data.csv

