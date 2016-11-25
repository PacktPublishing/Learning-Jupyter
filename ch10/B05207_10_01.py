#first spark script
import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()

lines = sc.textFile("Spark File Words.ipynb")
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b) 
print(totalLength)