import pandas
# conda install matplotlib
import matplotlib
#Enable inline plotting
%matplotlib inline

def main():	
	baby_name = ['Alice','Charles','Diane','Edward']
	number_births = [96, 155, 66, 272]
	dataset = list(zip(baby_name,number_births))
	df = pandas.DataFrame(data = dataset, columns=['Name', 'Number'])
	df['Number'].plot()

if __name__ == "__main__":
    main()