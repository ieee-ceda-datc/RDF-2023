# DATC Emerging Foundations in IC Physical Design
In this repository, we provide the source code and flow scripts for the newly
introduced elements presented in the ICCAD 2023 invited paper titled 'IEEE CEDA
DATC Emerging Foundations in IC Physical Design and MLCAD Research.' The 
included elements are:
1. [SpecPart](https://github.com/TILOS-AI-Institute/HypergraphPartitioning), [TritonPart](https://github.com/The-OpenROAD-Project/OpenROAD/tree/master/src/par): State-of-the-art circuit/hypergraph partitioners for
the 21st century.
2. [AutoDMP](https://github.com/NVlabs/AutoDMP): A DREAMPlace-based macro placement engine.
3. [DPO](https://github.com/The-OpenROAD-Project/OpenROAD/tree/master/src/dpo): A detailed placement optimization engine in OpenROAD.
4. [PROBE3.0](https://github.com/ABKGroup/PROBE3.0): A Design-technology co-optimization (DTCO) pathfinding framework.
5. Proxy Enablements: An auto-tuning based library scaling flow.

In this repository, our primary focus is on Proxy Enablements. For the other elements, please refer to their respective repositories.

## Directory Structure
1. [benchmarks](./benchmarks/): Contains the rtl and constraints for the benchmark design used for library scaling.
2. [run](./run): Use this directory to run the library scaling flow.
3. [scripts](./scripts): Provides the library scaling and autotuning flow required to generate proxy enablements. It also includes the scripts to run synthesis, placement, and routing flow using Cadence Genus and Innovus.
4. [techlibs](./techlibs/): Contains the technology files such as LEF, LIB, QRC for the 7nm PDK [asap7](https://github.com/The-OpenROAD-Project/asap7).

## Proxy Enablements
Please install the following python packages to run the library scaling flow:
1. liberty parser: `pip install liberty-parser`
2. ray: `pip install ray[tune]`
  

To run the library scaling flow, please follow the steps below:
1. First update the range of different scaling parameters [here](./scripts/autotune_scaling_factor/raytuner.py#L52-L61).
2. Provide the PPA number of the benchmark design on the target library [here](./scripts/autotune_scaling_factor/raytuner.py#L48).
3. Update total number of samples and number of parallel jobs to use for the autotuning job [here](./scripts/autotune_scaling_factor/raytuner.py#L97-L98).
4. Add the target clock periods and utilization list based on the golden data [here](./scripts/autotune_scaling_factor/raytuner.py#L44-L46).
5. Additionally, if you plan to use multiple servers to run SP&R jobs in parallel using [GNU parallel](https://www.gnu.org/software/parallel/), please update the [node](./scripts/util/node) file and its path [here](./scripts/autotune_scaling_factor/extract_scaled_loss.py#L113).
6. Use the following command in your python environment to run the autotuning flow:
```
export PROJ_DIR=<path to the root directory of this repository>
python ./scripts/autotune_scaling_factor/raytuner.py

# For NG45 tuning
python ./scripts/autotune_scaling_factor/raytuner_ng45.py
```


At the end of the run you will get the best scaling parameters for the given benchmark design that minimizes the PPA difference with the target library. You can find all the scaled libraries in the following path:
```
./run/libraries/scaled_lib_<scaling_factor>
```

## References
1. J. Jung, A. B. Kahng, S. Kundu, Z. Wang and D. Yoon, "IEEE CEDA DATC Emerging Foundations in IC Physical Design and MLCAD Research", ([.pdf](https://vlsicad.ucsd.edu/Publications/Conferences/400/c400.pdf)), *Proc. ACM/IEEE International Conference on Computer-Aided Design*, 2023
