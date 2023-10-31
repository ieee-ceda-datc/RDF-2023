import sys
import os
import re
from typing import List, Dict, Tuple

file_path = os.path.abspath(__file__)
proj_dir = re.search(r'/\S+/RDF-2023', file_path).group(0)
PROJ_DIR = os.environ.get('PROJ_DIR', proj_dir)

def gen_scaled_libs(ref_libs:str, lib_directory:str,
                    scaling_factors:List[float]) -> str:
    """
    Generate a set of scaled libraries from a reference library.
    ref_libs: Path to the reference scripts --> Path to scaled_lib_ref
    lib_directory: Path to where we save the scaled libraries
    We save the scaled libraries in the following direcotry:
    {PROJ_DIR}/run/libraries
    """
    
    ## Create a string where the list items are separate by _
    scaling_factors_str = "_".join([str(x) for x in scaling_factors])
    scaled_lib_direcotry = os.path.join(lib_directory,
                                        f"scaled_lib_{scaling_factors_str}")
    
    ## If the lib_directory does not exist, create it
    if not os.path.exists(lib_directory):
        os.makedirs(lib_directory)
    
    ## Check if the scaled library directory exists
    if os.path.exists(scaled_lib_direcotry):
        print(f"Directory {scaled_lib_direcotry} already exists")
        print(f"If the scaled lib generation is inclomplete "
              f"delete the {scaled_lib_direcotry} and run this script again")
        return scaled_lib_direcotry
    
    # Copy the reference library to the new directory
    os.system(f"cp -r {ref_libs} {scaled_lib_direcotry}")
    
    # Change current working directory to the new directory
    current_dir = os.getcwd()
    os.chdir(scaled_lib_direcotry)
    
    # Execude the following shell command
    
    # Delay factors are the first three elements of the scaling factors
    # separated by space
    delay_factors = " ".join([str(x) for x in scaling_factors[:3]])
    cmd = f"./delay_scaling.sh {delay_factors}"
    os.system(f"{cmd}")
    
    # Power factos are the next 6 elements of the scaling factors
    # separated by space
    power_factors = " ".join([str(x) for x in scaling_factors[3:9]])
    cmd = f"./power_scaling.sh {power_factors}"
    os.system(f"{cmd}")
    
    # Remove ORG, delay_scaled and intPower_scaled directories
    os.system("rm -rf delay_scaled")
    
    # Go back to the original directory
    os.chdir(current_dir)
    return scaled_lib_direcotry

if __name__ == '__main__':
    ref_dir = f"{PROJ_DIR}/run/library"
    ref_lib = f"{PROJ_DIR}/scripts/library_scaling/scaled_lib_ref"
    # example input scaling factor for asap7
    # -0.2 -0.2 -0.2 -0.2 -0.2 -0.2 -0.2 -0.2 -0.2
    scaling_factors = sys.argv[1:]
    scaled_lib_dir = gen_scaled_libs(ref_lib, ref_dir, scaling_factors)
    print(f"Generated scaled library at {scaled_lib_dir}")
