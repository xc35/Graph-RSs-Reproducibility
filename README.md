# Graph-RSs-Reproducibility

This is the official repository for the paper "_Challenging the Myth of Graph Collaborative Filtering: a Reasoned and
Reproducibility-driven Analysis_", under review at RecSys 2023 (Reproducibility Track).

This repository is heavily dependent on the framework **Elliot**, so we suggest you refer to the official GitHub [page](https://github.com/sisinflab/elliot) and [documentation](https://elliot.readthedocs.io/en/latest/).

## Pre-requisites

We implemented and tested our models in `PyTorch==1.12.0`, with CUDA `10.2` and cuDNN `8.0`. Additionally, some of graph-based models require `PyTorch Geometric`, which is compatible with the versions of CUDA and `PyTorch` we indicated above.

### Installation guidelines: scenario #1
If you have the possibility to install CUDA on your workstation (i.e., `10.2`), you may create the virtual environment with the requirement files we included in the repository, as follows:

```
# PYTORCH ENVIRONMENT (CUDA 10.2, cuDNN 8.0)

$ python3.8 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ pip install -r requirements_torch_geometric.txt
```

### Installation guidelines: scenario #2
A more convenient way of running experiments is to instantiate a docker container having CUDA `10.2` already installed. Make sure you have Docker and NVIDIA Container Toolkit installed on your machine (you may refer to this [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)). Then, you may use the following Docker image to instantiate the container equipped with CUDA `10.2` and cuDNN `8.0`: [link](https://hub.docker.com/layers/nvidia/cuda/10.2-cudnn8-devel-ubuntu18.04/images/sha256-3d1aefa978b106e8cbe50743bba8c4ddadacf13fe3165dd67a35e4d904f3aabe?context=explore).

## Datasets

### Reproducibility datasets
We used Gowalla, Yelp 2018, and Amazon Book datasets. The original links may be found here, where the train/test splitting has already been provided:

- Gowalla: https://github.com/xiangwang1223/neural_graph_collaborative_filtering/tree/master/Data/gowalla
- Yelp 2018: https://github.com/kuandeng/LightGCN/tree/master/Data/yelp2018
- Amazon Book: https://github.com/xiangwang1223/neural_graph_collaborative_filtering/tree/master/Data/amazon-book

After downloading, create three folders ```./data/{dataset_name}```, one for each dataset. Then, run the script ```./map_dataset.py```, by changing the name of the dataset within the script itself. It will generate the train/test files for each dataset in a format compatible for Elliot (i.e., tsv file with three columns referring to user/item).


### Additional datasets
We directly provide the train/validation/test splittings for Allrecipes and BookCrossing. As already stated for Gowalla, Yelp 2018, and Amazon Book, create one folder for each dataset in ```./data/{dataset_name}```:

- Allrecipes: 
- BookCrossing: 
