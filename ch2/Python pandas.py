# conda install pandas
from pandas import *

def main():
	training_set = read_csv('~/Documents/book2/chapter2/train.csv')
	training_set.head()
	male = training_set[training_set.Sex == 'male']
	female = training_set[training_set.Sex =='female']
	womens_survival_rate = float(sum(female.Survived))/len(female)
	mens_survival_rate = float(sum(male.Survived))/len(male)
	print(womens_survival_rate, mens_survival_rate)

if __name__ == "__main__":
    main()