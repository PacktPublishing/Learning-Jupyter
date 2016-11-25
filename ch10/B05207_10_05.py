#log file examination
import pyspark
if not 'sc' in globals():
    sc = pyspark.SparkContext()

textFile = sc.textFile("access_log")
print(textFile.count(),"access records")

gets = textFile.filter(lambda line: "GET" in line)
print(gets.count(),"GETs")

posts = textFile.filter(lambda line: "POST" in line)
print(posts.count(),"POSTs")

other = textFile.subtract(gets).subtract(posts)
print(other.count(),"Other")
for x in other.collect():
    print x