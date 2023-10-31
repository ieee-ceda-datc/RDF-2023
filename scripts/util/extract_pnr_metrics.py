#!/bin/python
'''
Input: Provide the run dir full path
'''
import os
import sys
import re

run_dir = sys.argv[1]
TOP_MODULE = 'accelerator'
# util = os.getenv('UTIL')

base_name = os.path.basename(run_dir)
base_dir = os.path.dirname(run_dir)
run_type = os.path.basename(base_dir)
design_details = base_name.split('_')
benchmark = design_details[0]

testcase = str(design_details[1])
delayDown_RVT = str(design_details[2])
delayDown_LVT = str(design_details[3])
delayDown_SLVT = str(design_details[4])
pwrDown_int_RVT = str(design_details[5])
pwrDown_int_LVT = str(design_details[6])
pwrDown_int_SLVT = str(design_details[7])
pwrDown_sw_RVT = str(design_details[8])
pwrDown_sw_LVT = str(design_details[9])
pwrDown_sw_SLVT = str(design_details[10])

timing_file_gz = run_dir + "/timingReports/postRouteOpt.summary.gz"
timing_file = run_dir + "/timingReports/postRouteOpt.summary"

if os.path.exists(timing_file_gz):
    cmd = "gunzip" + " " + timing_file_gz
    os.system(cmd)
elif os.path.exists(timing_file):
    pass
    #print(f"timing file is already unzipped")
else:
    print(f"No timing file. Exit.")
    exit()

if testcase == 'vga':
    detail_file = run_dir + "/vga_enh_top_DETAILS.rpt"
elif testcase == 'netcard':
    detail_file = run_dir + "/netcard_DETAILS.rpt"
elif testcase == 'jpeg':
    detail_file = run_dir + "/jpeg_encoder_DETAILS.rpt"
else:
    print(f"No detail file. Exit.")
    exit()

power_rpt = run_dir + "/power_postRouteOpt.rpt"
#file_summary = run_dir + "/timingReports/invs_summary.rpt"
#file_sdc = run_dir + "/rpt/" + TOP_MODULE + "_updated.sdc"
#file_power = run_dir + "/rpt/invs_ff_power_updated.rpt"
cmd_file = run_dir + "/log/innovus.cmd"
log_file = run_dir + "/log/innovus.log"
libSetup_file = run_dir + "/lib_setup.tcl"

#dc_power_rpt_file  = f"{run_dir}/rpt/{TOP_MODULE}_power_updated.rep"
#dc_qor_rpt_file = f"{run_dir}/rpt/{TOP_MODULE}_qor_updated.rep"

flag = os.path.exists(timing_file)
#print(f"result flag is {flag}")
flag = flag and os.path.exists(power_rpt)
#print(f"result flag is {flag}")
flag = flag and os.path.exists(detail_file)
#print(f"result flag is {flag}")
flag = flag and os.path.exists(cmd_file)
#print(f"result flag is {flag}")
flag = flag and os.path.exists(log_file)
flag = flag and os.path.exists(libSetup_file)
#print(f"result flag is {flag}")

#num_macro = -1
#num_std_cell = -1
std_cell_area = -1
#macro_area = -1
core_area = -1

internal_power = -1
switching_power = -1
leakage_power = -1
total_power = -1
drc_count = -1

if flag:
    with open(detail_file) as f:
        contents = f.read().splitlines()
    f.close()

    # Design Details
    for line in contents:
        items = line.split(',')
        if (items[0] == 'postRouteOpt'):
            core_area = round(float(items[1]),2)
            std_cell_area = round(float(items[2]),2)
            worst_neg_slack = round(float(items[-4]),3)
        else:
            pass

    #Power
    with open(power_rpt) as f:
        contents = f.read().splitlines()
    f.close()

    for line in contents:
        items = line.split()
        if(len(items) == 6 and items[0] == "Total" and items[5] == "100"):
            internal_power = round(float(items[1]), 3)
            switching_power = round(float(items[2]), 3)
            leakage_power = round(float(items[3]), 3)
            total_power = round(float(items[4]), 3)
        else:
            pass

# Target Utilization
    with open(cmd_file) as f:
        contents = f.read().splitlines()
    f.close()

    for line in contents:
        items = line.split()
        if(len(items) == 8 and items[0] == "floorPlan"):
            target_util = round(float(items[3]), 2)
            #print(f"Target util is {target_util}")
        else:
            pass

# Effective Timing Calculation
    with open(log_file) as f:
        contents = f.read().splitlines()
    f.close()

    for line in contents:
        items = line.split()
        if(len(items) > 2 and items[0] == "Clock" and items[1] == "Period:"):
            if (items[3] == 'usec'):
                tcp_usec = round(float(items[2]), 6)
                tcp = tcp_usec * 1000000
                #tcp = round(float(items[2]*1000000), 1)
            else:
                print(f"Clock period is not usec. Please check. Exit.")
                exit()
        else:
            pass

    tcf = round(1000/tcp,6)
    effective_clock_period = float(tcp - worst_neg_slack)
    effective_clock_frequency = round(1000 / effective_clock_period, 6)

if os.path.exists(log_file):
    with open(log_file) as f:
        contents = f.read().splitlines()
    f.close()

    for line in contents:
        items = line.split()
        if (len(items) == 5 and items[0] == "Verification" and
            items[1] == "Complete" and items[4] == "Viols."):
            drc_count = int(items[3])
        else:
           pass 

umap = {
    'mW':1e-3,
    'uW':1e-6,
    'nW':1e-9,
    'pW':1e-12,
    'W':1
}

print(f"{testcase},"
        f"{target_util},"
        f"{delayDown_RVT},"
        f"{delayDown_LVT},"
        f"{delayDown_SLVT},"
        f"{pwrDown_int_RVT},"
        f"{pwrDown_int_LVT},"
        f"{pwrDown_int_SLVT},"
        f"{pwrDown_sw_RVT},"
        f"{pwrDown_sw_LVT},"
        f"{pwrDown_sw_SLVT},"
        f"{tcp},"
        f"{tcf},"
        f"{core_area},"
        f"{std_cell_area},"
        f"{worst_neg_slack},"
        f"{effective_clock_period},"
        f"{effective_clock_frequency},"
        f"{internal_power},"
        f"{switching_power},"
        f"{leakage_power},"
        f"{total_power},"
        f"{drc_count}"
        )
