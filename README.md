# usg

## Overview

This project uses unsupervised learning to infer identify hidden patterns in the kaggle_steam dataset.  
 [Kaggle](https://www.kaggle.com/datasets/nikdavis/steam-store-games) | [Permalink](https://github.com/rxEckT/usg/blob/9d5377ae47314128a050e9b257ea01c5a4eb3575/data/01_raw/kaggle_steam.csv)

Our clustering method of choice is [KPrototypes](https://github.com/nicodv/kmodes).

 All analyses were done in .ipynb in the [notebooks](/notebooks) subdirectory.

| |File|Description|
|-|----|-----------|
|1|[00_exploratory_data_analysis.ipynb](/notebooks/00_exploratory_data_analysis.ipynb)|We perform some preliminary investigations on our dataset to split them into categorical and numerical variables.|
|2|[01_categorical_analysis.ipynb](/notebooks/01_categorical_analysis.ipynb)|We analyse categorical variables in detail and used MultiLabelBinarizer to select some features for use in clustering.|
|3|[02_numerical_analysis.ipynb](/notebooks/02_numerical_analysis.ipynb)|We analyse numerical features in detail, explored PowerTransformer to scale our data and performed Principal Component Analysis to project our data.|
|4|[10_feature_normalisation.ipynb](/notebooks/10_feature_normalisation.ipynb)|After some feature engineering, we used StandardScaler and PowerTransformer to normalise our data, followed up with PCA.|
|5|[20_kprototypes.ipynb](/notebooks/20_kprototypes.ipynb)|We use elbow method and silhouette score to find the optimal number of clusters.|
|6|[21_kprototypes(k=4).ipynb](/notebooks/21_kprototypes(k%3D4).ipynb)|We present our findings with k=4. We also used treemaps to visualise our findings.|
|7|[22_kprototypes(k=24).ipynb](/notebooks/22_kprototypes(k%3D24).ipynb)|We compared our findings on k=24 to k=4.|

## How to reproduce

1. Install dependencies listed in `Pipfile` within your python environment.
2. Run all notebook .ipynb files in sequence.
3. For `20_kprototypes.ipynb`, only running the last cell is necessary. The other cells make take hours to days to complete.
