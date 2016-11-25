import pylab
import random

def main():
	random.seed(113)
	samples = 1000
	dice = []
	for i in range(samples):
		total = random.randint(1,6) + random.randint(1,6)
		dice.append(total)
	pylab.hist(dice, bins= pylab.arange(1.5,12.6,1.0))
	pylab.show()

if __name__ == "__main__":
    main()