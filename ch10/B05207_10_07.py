#spark text file analysis
import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()
     
sentences = sc.textFile('2600raid.txt') \
    .glom() \
    .map(lambda x: " ".join(x)) \
    .flatMap(lambda x: x.split("."))
print(sentences.count(),"sentences")

bigrams = sentences.map(lambda x:x.split()) \
    .flatMap(lambda x: [((x[i],x[i+1]),1) for i in range(0,len(x)-1)])
print(bigrams.count(),"bigrams")

frequent_bigrams = bigrams.reduceByKey(lambda x,y:x+y) \
    .map(lambda x:(x[1],x[0])) \
    .sortByKey(False)
frequent_bigrams.take(10)