# This script was written and developed by ABKGroup students at UCSD. However, the underlying commands and reports are copyrighted by Cadence. 
# We thank Cadence for granting permission to share our research to help promote and foster the next generation of innovators.
# lib and lef, RC setup

set libdir "$::env(lib_directory)"
set lefdir "${proj_dir}/techlibs/ng45/lef"
set qrcdir "${proj_dir}/techlibs/ng45/qrc"

set_db init_lib_search_path { \
  ${libdir} \
  ${lefdir} \
}

set libworst [glob ${libdir}/*.lib]
set libbest $libworst

set lefs "  
  ${lefdir}/NangateOpenCellLibrary.tech.lef \
  ${lefdir}/NangateOpenCellLibrary.macro.mod.lef \
  "

set qrc_max "${qrcdir}/NG45.tch"
set qrc_min "${qrcdir}/NG45.tch"

# Ensures proper and consistent library handling between Genus and Innovus
setDesignMode -process 45
