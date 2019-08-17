# Summary of code -
# broadcast()

import os
from pyspark import SparkConf, SparkContext

# Helper functions ...

# Parse movie ratings dataset and convert to key-value pair
def parse_movie_rating_dataset(line):
    fields = line.split("\t")
    movie_id = fields[1]
    return (movie_id, 1)

def parse_movie_dataset():
    movie_dict = {}
    with open("C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.item") as file:
        for line in file:
            fields = line.split("|")
            movie_dict[int(fields[0])] = fields[1]
    
    return movie_dict

# Boilerplate code ...
conf = SparkConf().setMaster("local").setAppName("Use Broadcast")
spark_context = SparkContext(conf = conf)

# Load movie ratings dataset
movie_ratings_dataset = spark_context.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.data")
movies_rdd = movie_ratings_dataset.map(parse_movie_rating_dataset)

# Load movies dataset
movie_dict = parse_movie_dataset()

# Broadcast movie dictionary for use by executors
movie_dict_broadcasted = spark_context.broadcast(movie_dict)

# Calculate count of movies in dataset
movies_cnt_rdd = movies_rdd.reduceByKey(lambda x, y: x + y)
print(movies_cnt_rdd.take(5))

movies_cnt_swapped_rdd = movies_cnt_rdd.map(lambda x: (x[1], x[0]))
print(movies_cnt_swapped_rdd.take(5))

# Sort by number of occurrences of movies in dataset
movies_cnt_sorted_rdd = movies_cnt_swapped_rdd.sortByKey(False)
print(movies_cnt_sorted_rdd.take(5))

movies_cnt_sorted_swapped_rdd = movies_cnt_sorted_rdd.map(lambda x: (x[1], x[0]))
print(movies_cnt_sorted_swapped_rdd.take(50))

# sorted_movies_with_names = movies_cnt_sorted_swapped_rdd.map(lambda movie : (movie_dict_broadcasted.value[movie[1]], movie[0]))
# results = sorted_movies_with_names.collect()

# for result in results:
#     print (result)


