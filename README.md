# Titanic Project 🚢
A machine learning app to determine the chance of survival on the Titanic based on various features. Try it live at https://share.streamlit.io/sleepypioneer/titanic_survival_model/main/src/app.py

## Development 🖥️

This app has been developed with Python 3.8.5 and [streamlit](https://www.streamlit.io/) using [Jupyter notebooks](https://jupyter.org/) to explore the data and build the model.

### Download the data 💾

The data for this project has not been checked into Github, so you will need to download it locally first. You can download the data from Kaggle [here](https://www.kaggle.com/c/titanic/data) (you will need both the test.csv and train.csv) save these files in the directory: `/model_in_notebook/data/`

### Create and activate a virtual environment 🌐

```sh
# create the environment
python3.8.5 -m venv venv

# activate it on linux or Mac from this repository
source ../venv/bin/activate

# activate it on windows
venv\Scripts\activate.bat
```

### Install dependencies 🧰

You can install all the necessary dependencies, listed in `requirements.txt` by running the following command:

```sh
pip install -r requirements.txt
```

### Running the app locally 🧊

Now that the virtual environment  activated run the following command to run the streamlit app with live reload on save.

```sh
# This command needs to be run inside the src/ directory
# To change into the src/ directory
cd src
streamlit run --server.runOnSave=True app.py
```

This will run the app locally at `http://localhost:8501/`

To stop the service running use `Ctrl c`

### Exploring the notebooks locally 📘

You can also open the notebooks exploring the data and building the model. To do this follow the instructions in this [README](./model_in_notebook/README.md)

### Tests

### Deployment

Currently, this app is deployed with Streamlit sharing :heart:
