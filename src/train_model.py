import pandas as pd, os, numpy as np, pickle
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
import bentoml



def train_forest(data_path, *args, **kwargs):
    
    X_train = pd.read_parquet(data_path).drop("date", axis=1)
    y_train = X_train.pop('rented_bike_count')
    
    rf = RandomForestRegressor(*args, **kwargs, n_jobs=-1, oob_score=True)
    rf.fit(X_train, y_train)
    
    return rf


def save_model(model, model_path, model_name):
    if not model_path.exists(): model_path.mkdir(parents=True)
    with open(model_path.joinpath(model_name), "wb") as fd:
        pickle.dump(model, fd)
    bentoml.sklearn.save_model("bikes_model", model)


if __name__ == "__main__":
    
    # the paths we need
    path = Path().cwd()
    train_data_path = path.joinpath("data", 'processed', 'train.parquet')
    model_path = path.joinpath('models')
    model_name = 'bikes_model.pkl'
    
    # for our model
    parameters = dict(n_estimators=400, max_features=0.2, min_samples_leaf=1, verbose=1, random_state=42)
    
    # training process
    model = train_forest(data_path=train_data_path, **parameters)
    
    # the model we need :)
    save_model(model, model_path, model_name)
    print("File Trained Successfully!")