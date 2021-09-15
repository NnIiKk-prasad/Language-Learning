# -----Pickling Iris-----
import requests
import pickle

if __name__ == '__main__':
    try:
        iris_file = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text
        pkl_lst = [item.split(",") for item in iris_file.split("\n") if len(item) != 0]

        with open('iris.pkl', 'wb') as file:
            pickle.dump(pkl_lst, file)

        with open('iris.pkl', 'rb') as file:
            # print(pickle.load(file))
            unpickle_lst = pickle.load(file)
        for line in unpickle_lst:
            print(",".join(line))
    except Exception as e:
        print("Something Went Wrong!!!\n", e)
