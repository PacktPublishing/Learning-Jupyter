#spark primes
import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()
    
def is_it_prime(number):
    # make sure n is a positive integer
    number = abs(int(number))
    
    # simple tests
    if number < 2:
        return False
    
    # 2 is prime
    if number == 2:
        return True
    # other even numbers aren't
    if not number & 1:
        return False
    
    # check whether number is divisible into it's square root
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            return False
        
    #if we get this far we are good
    return True

# create a set of numbers to 100,000
numbers = sc.parallelize(xrange(100000))

# count out the number of primes we found
print numbers.filter(is_it_prime).count()