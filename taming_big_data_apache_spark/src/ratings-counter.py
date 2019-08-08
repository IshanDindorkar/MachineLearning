# Summary of example
# Main attraction is countByValue() action in SparkConf
# We are finding count of every unique movie rating given by users

from pyspark import SparkConf, SparkContext
import collections

# Setting up configs for Spark job, master is set to "local" as it is running on local machine
conf = SparkConf().setMaster("local").setAppName("RatingsCount")
sc = SparkContext(conf = conf)

# Reading user ratings data
lines = sc.textFile("file:////C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])
# print(ratings.take(5)) # for debugging purpose

# Count occurrence of each unique rating
result = ratings.countByValue()

# Sorting ratings by the key which is rating itself
sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print((key, value))