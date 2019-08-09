# Summary of code -
# Find the most popular movie in the MovieLens dataset

# Basic imports ...
from pyspark import SparkConf, SparkContext
import collections

def parse_movie_rating_record(line):
    fields = line.split("\t")
    movie_id = int(fields[0])

    return (movie_id, 1)

# Boilerplate code
conf = SparkConf().setMaster("local").setAppName("Most Popular Movie Job")
sc = SparkContext(conf = conf)

movie_dataset = sc.textFile("file:////C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.data")
movie_ids_RDD = movie_dataset.map(parse_movie_rating_record)
movie_ids_cnt_RDD = movie_ids_RDD.reduceByKey(lambda x, y: x + y)

# Sorting ratings by the key which is rating itself
movie_ids_cnt_swapped_RDD = movie_ids_cnt_RDD.map(lambda x: (x[1], x[0]))
results = movie_ids_cnt_swapped_RDD.sortByKey().collect()

# Printing results
for key, value in results:
    print(str(value) + "\t" + str(key))