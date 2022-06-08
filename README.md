Create a conda environment

```bash
conda create -n wine_quality python=3.10 -y
```

Activate created conda environment

```bash
conda activate wine_quality
```

Install the requirements

```bash
pip install -r requirements.txt
```

Download the data from the following link:  https://www.kaggle.com/datasets/yasserh/wine-quality-dataset

Initializing git

```bash
git init
```

Initializing dvc

```bash
dvc init
```

Adding the data to the dvc

```bash
dvc add data_given\WineQT.csv
```