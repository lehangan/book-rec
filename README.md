# Book Recommending System 
A book Book Recommendation System which recommends the users a selection of books. Using memory-based collaborative filtering to offer relevant items (books) to the users based on their taste or previous choices.

## Environment
- Anaconda : (link download https://www.anaconda.com/ )
- Jupyter Notebook
- Python: 3.10.8
- Pandas: 1.5.2

Installing required packages with `conda` (recommended):
```
conda env create -f environment.yml
conda activate book_rec_env
conda update --all
```

If you're not using `conda` (surprise package may not install):
```
pip install notebook
pip install -r requirements.txt
```
file `requirements.txt` was created with [`pipreqs`](https://anaconda.org/conda-forge/pipreqs) package
conda install -c conda-forge pipreqs


To start Jupyter Notebook:
```
jupyter notebook
```

## The dataset 
http://www2.informatik.uni-freiburg.de/~cziegler/BX/
Dataset contains 278,858 users (anonymized but with demographic information) providing 1,149,780 ratings (explicit & implicit) about 271,379 books.
The Book-Crossing dataset comprises 3 tables.
- BX-Users : Contains the users.
- BX-Books : Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (`Book-Title`, `Book-Author`, `Year-Of-Publication`, `Publisher`),URLs linking to cover images are also given, appearing in three different sizes (`Image-URL-S`, `Image-URL-M`, `Image-URL-L`),
- BX-Book-Ratings : Contains the book rating information. Ratings (`Book-Rating`) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.

## Libraries 
### Import libraries for dataset 
- numpy 
- seaborn
- pandas
- matplotlib (installed by seaborn)

conda update --all
conda install notebook
conda install numpy
conda install pandas
conda install seaborn
conda install scipy
conda install -c conda-forge scikit-learn
conda install -c conda-forge scikit-surprise

```python
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
```
### Import libraries for building system and evaluation 
- sklearn
- surprise 
```python
from sklearn.model_selection import train_test_split
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split, cross_validate, GridSearchCV
from surprise import KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline
from surprise import accuracy
import random
```

## Load Data
While importing libraries and load datasets. while loading the file we have some problems like:
- The values in the CSV file are separated by semicolons, not by a comma.
- There are some lines which not work like we cannot import it with pandas and It throws an error because python is Interpreted language

So while loading data we have to handle these exceptions and after running the below code you will get some warning and it will show which lines have an error that we have skipped while loading.
```python
import warnings 
warnings.filterwarnings("ignore")
```

Need to know the path of data to use and load
```python
def loaddata(filename):
    df = pd.read_csv(f'{filename}.csv',sep=';',error_bad_lines=False,warn_bad_lines=False,encoding='latin-1')
    return df

book   = loaddata("../../BX-Books")
user   = loaddata("../../BX-Users")
rating = loaddata("../../BX-Book-Ratings")
```

## User-Guide using Surprise 
You just need to pass a sim_options argument at the creation of an algorithm. This argument is a dictionary with the following (all optional) keys:
- 'name': The name of the similarity to use, as defined in the similarities module. Default is 'MSD'. ['cosine' , 'pearson', 'pearson_baseline', 'msd']
- 'min-support' : [1,5]
- 'user_based' : [True,False]


