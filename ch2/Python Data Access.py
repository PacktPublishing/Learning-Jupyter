# import the datasets package
# conda install scikit-learn
from sklearn import datasets

def main():
	# pull in the iris data
	iris_dataset = datasets.load_iris()
	# grab the first two columns of data
	X = iris_dataset.data[:, :2]

	# calculate some basic statistics
	x_count = len(X.flat)
	x_min = X[:, 0].min() - .5
	x_max = X[:, 0].max() + .5
	x_mean = X[:, 0].mean()

	# display our results
	print(x_count, x_min, x_max, x_mean)

if __name__ == "__main__":
    main()