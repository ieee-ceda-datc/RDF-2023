#!/bin/bash
export powerIntScale_RVT=$1
export powerIntScale_LVT=$2
export powerIntScale_SLVT=$3
export powerSwScale_RVT=$4
export powerSwScale_LVT=$5
export powerSwScale_SLVT=$6
python liberty_tbl_scale_power.py $powerIntScale_LVT  $powerSwScale_LVT  ./delay_scaled/asap7sc7p5t_AO_LVT_TT_nldm_201020.lib > asap7sc7p5t_AO_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_RVT  $powerSwScale_RVT  ./delay_scaled/asap7sc7p5t_AO_RVT_TT_nldm_201020.lib > asap7sc7p5t_AO_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_SLVT $powerSwScale_SLVT ./delay_scaled/asap7sc7p5t_AO_SLVT_TT_nldm_201020.lib > asap7sc7p5t_AO_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_LVT  $powerSwScale_LVT  ./delay_scaled/asap7sc7p5t_INVBUF_LVT_TT_nldm_201020.lib > asap7sc7p5t_INVBUF_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_RVT  $powerSwScale_RVT  ./delay_scaled/asap7sc7p5t_INVBUF_RVT_TT_nldm_201020.lib > asap7sc7p5t_INVBUF_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_SLVT $powerSwScale_SLVT ./delay_scaled/asap7sc7p5t_INVBUF_SLVT_TT_nldm_201020.lib > asap7sc7p5t_INVBUF_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_LVT  $powerSwScale_LVT  ./delay_scaled/asap7sc7p5t_OA_LVT_TT_nldm_201020.lib > asap7sc7p5t_OA_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_RVT  $powerSwScale_RVT  ./delay_scaled/asap7sc7p5t_OA_RVT_TT_nldm_201020.lib > asap7sc7p5t_OA_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_SLVT $powerSwScale_SLVT ./delay_scaled/asap7sc7p5t_OA_SLVT_TT_nldm_201020.lib > asap7sc7p5t_OA_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_LVT  $powerSwScale_LVT  ./delay_scaled/asap7sc7p5t_SEQ_LVT_TT_nldm_201020.lib > asap7sc7p5t_SEQ_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_RVT  $powerSwScale_RVT  ./delay_scaled/asap7sc7p5t_SEQ_RVT_TT_nldm_201020.lib > asap7sc7p5t_SEQ_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_SLVT $powerSwScale_SLVT ./delay_scaled/asap7sc7p5t_SEQ_SLVT_TT_nldm_201020.lib > asap7sc7p5t_SEQ_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_LVT  $powerSwScale_LVT  ./delay_scaled/asap7sc7p5t_SIMPLE_LVT_TT_nldm_201020.lib > asap7sc7p5t_SIMPLE_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_RVT  $powerSwScale_RVT  ./delay_scaled/asap7sc7p5t_SIMPLE_RVT_TT_nldm_201020.lib > asap7sc7p5t_SIMPLE_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_power.py $powerIntScale_SLVT $powerSwScale_SLVT ./delay_scaled/asap7sc7p5t_SIMPLE_SLVT_TT_nldm_201020.lib > asap7sc7p5t_SIMPLE_SLVT_TT_nldm_201020.lib
