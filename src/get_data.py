import urllib.request
from pathlib import Path


def get_bikes_data(url, path, file_name):

    if not path.exists():
        path.mkdir(parents=True)
    urllib.request.urlretrieve(url, path.joinpath(file_name))


if __name__ == "__main__":
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00560/SeoulBikeData.csv'
    path = Path().cwd().joinpath('data', "raw")
    file_name = 'SeoulBikeData.csv'
    get_bikes_data(url, path, file_name)
    print("File Downloaded Successfully!")