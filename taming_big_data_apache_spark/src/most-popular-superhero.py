# Summary of codebase
# max() - find out row with maximum key value, lookup() - search for a specific key in RDD

from pyspark import SparkConf, SparkContext

def count_occurences(line):
    fields = line.split()

    return (fields[0], len(fields) - 1)

def get_superhero_details(line):
    fields = line.split("\"")

    return(int(fields[0]), fields[1].encode("utf-8"))

conf = SparkConf().setMaster("local").setAppName("Most Popular Super Hero")
spark_context = SparkContext(conf = conf)

# Loading marvel graph file
marvel_graph = spark_context.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/Marvel-Graph.txt")
occurences_rdd = marvel_graph.map(count_occurences)

# Aggregating total occurrences of superheros
occurences_aggregated_rdd = occurences_rdd.reduceByKey(lambda x,y: x + y)
occurences_flipped_rdd = occurences_aggregated_rdd.map(lambda x: (x[1], x[0]))

# Finding out superhero who made maximum appearance
max_occurence = occurences_flipped_rdd.max()
print(max_occurence)

# Loading details of superheros
marvel_superheros = spark_context.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/Marvel-Names.txt")
marvel_superheros_rdd = marvel_superheros.map(get_superhero_details)

most_popular_superhero = str(marvel_superheros_rdd.lookup(int(max_occurence[1]))[0])
print(most_popular_superhero)



