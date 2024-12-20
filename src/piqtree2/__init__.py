"""piqtree2 - access the power of IQ-TREE within Python."""

from piqtree2._data import dataset_names, download_dataset
from piqtree2.iqtree import (
    TreeGenMode,
    build_tree,
    fit_tree,
    jc_distances,
    model_finder,
    nj_tree,
    random_trees,
    robinson_foulds,
)
from piqtree2.model import (
    Model,
    available_freq_type,
    available_models,
    available_rate_type,
)

__version__ = "0.3.2"

__all__ = [
    "Model",
    "TreeGenMode",
    "available_freq_type",
    "available_models",
    "available_rate_type",
    "build_tree",
    "dataset_names",
    "download_dataset",
    "fit_tree",
    "jc_distances",
    "model_finder",
    "nj_tree",
    "random_trees",
    "robinson_foulds",
]
