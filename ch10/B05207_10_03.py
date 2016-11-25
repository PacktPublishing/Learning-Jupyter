#sorted word count
import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()
    
text_file = sc.textFile("Spark File Words.ipynb")
sorted_counts = text_file.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .sortByKey()
for x in sorted_counts.collect():
    print x