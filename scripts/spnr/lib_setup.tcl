# This script was written and developed by ABKGroup students at UCSD. However, the underlying commands and reports are copyrighted by Cadence. 
# We thank Cadence for granting permission to share our research to help promote and foster the next generation of innovators.
# lib and lef, RC setup

set libdir "$::env(lib_directory)"
set lefdir "${proj_dir}/techlibs/asap7/lef"
set qrcdir "${proj_dir}/techlibs/asap7/qrc"

set_db init_lib_search_path { \
  ${libdir} \
  ${lefdir} \
}

set libworst [glob ${libdir}/*.lib]
set libbest $libworst

set lefs "  
  ${lefdir}/asap7_tech_1x_201209.lef \
  ${lefdir}/asap7sc7p5t_27_R_1x_201211.lef \
  ${lefdir}/asap7sc7p5t_27_L_1x_201211.lef \
  ${lefdir}/asap7sc7p5t_27_SL_1x_201211.lef \
  "

set qrc_max "${qrcdir}/ASAP7_1x.tch"
set qrc_min "${qrcdir}/ASAP7_1x.tch"

# Ensures proper and consistent library handling between Genus and Innovus
setDesignMode -process 7
