## Overview

This project uses unsupervised learning to infer identify hidden patterns in the kaggle_steam dataset.  
 [Kaggle](https://www.kaggle.com/datasets/nikdavis/steam-store-games) | [Permalink](https://github.com/rxEckT/usg/blob/9d5377ae47314128a050e9b257ea01c5a4eb3575/data/01_raw/kaggle_steam.csv)

Our clustering method of choice is [k-prototypes](https://github.com/nicodv/kmodes).

## Aim
How can we help game developers make better games?

To achieve this, we would need to:
- Uncover hidden patterns in player trends
- Identify common features within subgroups
- Understand why players may flock to certain games

## Structure

All analyses were done in .ipynb in the [notebooks](/notebooks) subdirectory.

| |File|Description|
|-|----|-----------|
|1|[00_exploratory_data_analysis.ipynb](/notebooks/00_exploratory_data_analysis.ipynb)|We perform some preliminary investigations on our dataset to split them into categorical and numerical variables.|
|2|[01_categorical_analysis.ipynb](/notebooks/01_categorical_analysis.ipynb)|We analyse categorical variables in detail and used MultiLabelBinarizer to select some features for use in clustering. We also did some feature engineering.|
|3|[02_numerical_analysis.ipynb](/notebooks/02_numerical_analysis.ipynb)|We analyse numerical features in detail, explored PowerTransformer to scale our data and performed Principal Component Analysis to project our data. We also did some feature engineering.|
|4|[10_feature_normalisation.ipynb](/notebooks/10_feature_normalisation.ipynb)|After some feature engineering, we used StandardScaler and PowerTransformer to normalise our data, followed up with PCA.|
|5|[20_kprototypes.ipynb](/notebooks/20_kprototypes.ipynb)|We use elbow method and silhouette score to find the optimal number of clusters.|
|6|[21_kprototypes(k=4).ipynb](/notebooks/21_kprototypes(k%3D4).ipynb)|We present our findings with k=4. We also used treemaps to visualise our findings.|
|7|[22_kprototypes(k=24).ipynb](/notebooks/22_kprototypes(k%3D24).ipynb)|We compared our findings on k=24 to k=4. We also used a sankey diagram to visualise the relationships between k=4 and k=24.|

## Key Findings
**Players tend to be attracted to...**

- Cluster 0: Classic, Timeless Games that have a solid fan base
- Cluster 1: Recent, premium, niche indie games
- Cluster 2: Affordable alternatives to mainstream games
- Cluster 3: Rewarding, low stress, fuss-free games

Find out more: [21_kprototypes(k=4).ipynb](/notebooks/21_kprototypes(k%3D4).ipynb)

**How to prepare a highly skewed dataset like kaggle_steam for clustering?**
- A combination of Power Transformer + Principal Component Analysis worked well to normalise the numeric features for purposes of clustering in k-prototypes

Find out more: [01_categorical_analysis.ipynb](/notebooks/01_categorical_analysis.ipynb) | [02_numerical_analysis.ipynb](/notebooks/02_numerical_analysis.ipynb)

---

## Interactive charts
Thanks to GitHub pages, we have made two of our interactive charts available for viewing.

|Title|Detailed Explanation|Link|
|-----|--------------------|----|
|Treemap of steam games by assigned clusters and number of owners|[21_kprototypes(k=4).ipynb](/notebooks/21_kprototypes(k%3D4).ipynb)|[Link](https://rxeckt.github.io/usg/images/21/1.html)|
|Sankey diagram of k=4 distribution in k=24|[22_kprototypes(k=24).ipynb](/notebooks/22_kprototypes(k%3D24).ipynb)|[Link](https://rxeckt.github.io/usg/images/22/2.html)|

Alternatively, a static image of these charts has also included in the respective notebooks.

---

## Selected resources for further reading
### k-modes & k-prototypes
- https://github.com/nicodv/kmodes
### Scaling, normalizing and standardizing data for machine learning
- https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py
- https://zachary-a-zazueta.medium.com/data-transformation-in-ml-standardization-vs-normalization-70ba26de9060
- https://machinelearningmastery.com/power-transforms-with-scikit-learn/
### Principal Component Analysis
- Data Analysis 6: Principal Component Analysis (PCA) - Computerphile https://www.youtube.com/watch?v=TJdH6rPA-TI
### Clustering
- Data Analysis 7: Clustering - Computerphile
 https://www.youtube.com/watch?v=KtRLF6rAkyo
### Visualisation
- https://www.data-to-viz.com/
- https://plotly.com/python/treemaps/
- https://plotly.com/python/sankey-diagram/

---

## How to reproduce

1. Install dependencies listed in `Pipfile` within your python environment.
2. Run all notebook .ipynb files in sequence.
3. For `20_kprototypes.ipynb`, only running the last cell is necessary. The other cells may take hours to days to complete.
