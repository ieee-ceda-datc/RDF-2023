import pandas as pd
import sys
import os
import re
from typing import List, Tuple, Dict, Set, Optional, Union

## Set the PROJ_DIR to the root directory of the project ##
file_path = os.path.abspath(__file__)
proj_dir = re.search(r'/\S+/RDF-2023', file_path).group(0)
PROJ_DIR = os.environ.get('PROJ_DIR', proj_dir)
sys.path.append(f"{PROJ_DIR}/scripts/library_scaling")
from gen_scaled_lib_ng45 import gen_scaled_libs

def generate_job_list(ref_script:str, scaled_lib_dir:str, tcp_list:List[float],
                      util_list:List[float],
                      job_file_dir:Optional[str]=None) -> str:
    if job_file_dir is None:
        job_file_dir = os.getcwd()
    
    ## pid 
    pid = os.getpid()
    
    ## job file name
    job_file_name = f"{job_file_dir}/job_list_{pid}"
    
    ## generate job list
    with open(job_file_name, "w") as fp:
        for i, tcp in enumerate(tcp_list):
            fp.write(f"{ref_script} {scaled_lib_dir} {tcp} "
                     f"{util_list[i]}\n")

    return job_file_name

def run_gnu_paralled(job_file, node_file = None):
    gnu_parallel_script = f"{PROJ_DIR}/scripts/util/run_gnu_parallel.csh"
    if node_file is None:
        os.system(f"tcsh {gnu_parallel_script} {job_file}")
    else:
        os.system(f"tcsh {gnu_parallel_script} {job_file} {node_file}")

def extract_loss(ref_df:pd.DataFrame, scaled_df:pd.DataFrame) -> Tuple[float, float, float]:
    columns = ['testcase', 'target_util', 'tcp']
    ref_df['effective_clock_frequency'] = 1e6/ref_df['effective_clock_period']
    scaled_df['effective_clock_frequency'] = 1e6/scaled_df['effective_clock_period']
    df = scaled_df.merge(ref_df, on = columns, suffixes=('_ng45', '_gold'),
                         how = 'left')
    # print(df.columns)
    df['loss_c1'] = (df['effective_clock_frequency_ng45'] - df['effective_clock_frequency_gold'])
    df['loss_c2'] = (df['total_power_ng45'] - df['total_power_gold'])
    # Loss is root mean square of loss_c1 and loss_c2
    df['loss'] = (df['loss_c1']**2 + df['loss_c2']**2)**0.5
    loss = df['loss'].mean()
    loss_max = df['loss'].max()
    loss_std = df['loss'].std()
    return loss, loss_max, loss_std

def gen_df_files(ref_csv:str, scale_prefix:str, run_dir:str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    ref_df = pd.read_csv(ref_csv)
    df_list = []
    for row in ref_df.iterrows():
        tcp = row[1]['tcp']
        util = row[1]['target_util']
        scale_file = f"{run_dir}/{scale_prefix}_{tcp}_{util}/scaled_pnr_data.csv"
        df = pd.read_csv(scale_file)
        df_list.append(df)
    scaled_df = pd.concat(df_list, ignore_index=True)
    return ref_df, scaled_df

def extract_mape_loss(ref_df:pd.DataFrame, scaled_df:pd.DataFrame) -> Tuple[float, float, float]:
    columns = ['testcase', 'target_util', 'tcp']
    ref_df['effective_clock_frequency'] = 1e6/ref_df['effective_clock_period']
    scaled_df['effective_clock_frequency'] = 1e6/scaled_df['effective_clock_period']
    
    df = scaled_df.merge(ref_df, on = columns, suffixes=('_ng45', '_gold'),
                         how = 'left')
    # print(df.columns)
    df['loss_c1'] = abs(df['effective_clock_frequency_ng45'] - df['effective_clock_frequency_gold'])/df['effective_clock_frequency_gold']
    df['loss_c2'] = abs(df['total_power_ng45'] - df['total_power_gold'])/df['total_power_gold']
    
    # Loss is root mean square of loss_c1 and loss_c2
    df['loss'] = (df['loss_c1']**2 + df['loss_c2']**2)**0.5
    loss = df['loss'].mean()
    loss_max = df['loss'].max()
    loss_std = df['loss'].std()
    return loss, loss_max, loss_std

def extract_scale_loss(scaling_factor:List[float], tcp_list:List[float],
                       util_list:List[float], ref_dir:str,
                       ref_csv:str) -> Tuple[float, float, float]:
    '''
    ref_dir: is the project direcotry
    ref_csv: Golden result
    '''
    design_name = "ng45_jpeg"
    scaling_ref_script = f"{ref_dir}/scripts/library_scaling/scaled_lib_ref_ng45"
    library_directory = f"{ref_dir}/run/library"
    
    if not os.path.exists(library_directory):
        os.makedirs(library_directory)
    
    scaled_lib_dir = gen_scaled_libs(scaling_ref_script, library_directory,
                                     scaling_factor)
    spnr_ref_script = f"{ref_dir}/scripts/util/run_scaled_spnr_ng45.sh"
    
    job_file_dir = f"{ref_dir}/run/job_directory"
    if not os.path.exists(job_file_dir):
        os.makedirs(job_file_dir)
    
    job_file = generate_job_list(spnr_ref_script, scaled_lib_dir, tcp_list,
                                 util_list, job_file_dir)
    
    node_file = f"{ref_dir}/scripts/util/node"
    # node_file = None
    run_gnu_paralled(job_file, node_file)
    
    ## Extract the scaled SPNR results
    scaling_factors_str = "_".join([str(x) for x in scaling_factor])
    sprn_run_dir = f"{ref_dir}/run/{design_name}_{scaling_factors_str}"
    df_list = []
    for i, tcp in enumerate(tcp_list):
        util = util_list[i]
        spnr_result_dir = f"{sprn_run_dir}_{tcp}_{util}"
        spnr_result_file = f"{spnr_result_dir}/scaled_pnr_data.csv"
        df = pd.read_csv(spnr_result_file)
        df_list.append(df)
    
    ref_df = pd.read_csv(ref_csv)
    
    # Concatenate the dataframes
    scaled_df = pd.concat(df_list, ignore_index=True)
    
    loss, max_loss, std_loss = extract_mape_loss(ref_df, scaled_df)
    return loss, max_loss, std_loss

if __name__ == '__main__':
    scaling_factors = [-0.2, -0.2, -0.2]
    tcp_list = [667.0, 556.0, 476.0, 417.0, 370.0, 333.0, 300.0, 256.0,
                238.0, 222.0]
    util = [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]
    
    ref_dir = PROJ_DIR
    
    ## Provide the CSV file of the Golden data ##
    ref_csv = f"{PROJ_DIR}/benchmarks/jpeg_encoder/golden_sample_a7.csv"
    loss, max_loss, std_loss = extract_scale_loss(scaling_factors, tcp_list,
                                                  util, ref_dir, ref_csv)
    print(f"Loss: {loss} Max Loss: {max_loss} Std Loss: {std_loss}")
