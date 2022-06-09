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

Creating the first commit

```bash
git add .
```
```bash
git commit -m "First commit"
```
Adding a remote origin for git

```bash
git remote add origin github_link_here
```

Switching the branch to main

```bash
git branch -M main
```

Pushing the changes to the git

```bash
git push origin main
```

Use following command to run the stages in dvc.yaml file

```bash
dvc repro
```

After the training and evaluation step, change the values of alpha and l1_ratio and run the stages from dvc.yaml file. dvc will remember all the
changes made and it will show those using following commands.

Checking current metrics
```bash 
dvc metrics show
```
Checking the changes in metrics
```bash
dvc metrics diff
```