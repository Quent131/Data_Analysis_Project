# Python for Data Analysis Project :

As my dataset was not available online anymore, I asked M. BEJNBAUM that told me to choose whatever dataset that would please me. So after a few research I decided to take [this one](https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29). It's a dataset that represents drug consumption and quantifies it.

The first thing you should do is take a look at the Jupyter Notebook `Python_Project.ipynb`. It is well commented and is about the data visualization and the modelisation part.
Here are the packages that are necessary to run this notebook :
- `numpy`
- `pandas`
- `searborn`
- `sk-learn`
- `pickle`
- `flask`
- `requests`
- `json`

At the end of the notebook, we generate 3 pickle file that are included in this folder. It is recommemded to run the notebook so that the files may update themselves if needed.

Then to run the API, you have to open a console and run the `app.py` file. It loads the model we choose to save from the notebook.

And then run the `request.py` file. The console in which you run this file will show the response of the model to the input data. There are two type of input data : one in the `API_data_example.pickle` that contains value that have been arbitrary choosen and another one `API_data_random.pickle` where the input values have been choosen randomly. To change from one to another, open the `request.py` file and change (in line 8):

```python
data = pickle.load(open('API_data_example.pickle', 'rb'))
```

to

```python
data = pickle.load(open('API_data_random.pickle', 'rb'))
```
