#!/bin/bash
export delayScale_RVT=$1
export delayScale_LVT=$2
export delayScale_SLVT=$3
export project_dir=`pwd | grep -o '/\S*RDF-2023'`
mkdir -p delay_scaled
python liberty_tbl_scale_delay.py $delayScale_LVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_AO_LVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_AO_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_RVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_AO_RVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_AO_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_SLVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_AO_SLVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_AO_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_LVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_INVBUF_LVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_INVBUF_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_RVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_INVBUF_RVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_INVBUF_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_SLVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_INVBUF_SLVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_INVBUF_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_LVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_OA_LVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_OA_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_RVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_OA_RVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_OA_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_SLVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_OA_SLVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_OA_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_LVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SEQ_LVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SEQ_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_RVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SEQ_RVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SEQ_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_SLVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SEQ_SLVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SEQ_SLVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_LVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SIMPLE_LVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SIMPLE_LVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_RVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SIMPLE_RVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SIMPLE_RVT_TT_nldm_201020.lib
python liberty_tbl_scale_delay.py $delayScale_SLVT $project_dir/techlibs/asap7/lib/asap7sc7p5t_SIMPLE_SLVT_TT_nldm_201020.lib > ./delay_scaled/asap7sc7p5t_SIMPLE_SLVT_TT_nldm_201020.lib
