# Summary of example
# Main attractions -
# Key, Value RDDs - An RDD can have data in the form of key, value pair
# mapValues() - If the intent is only to make computation with value and not key, use this function
# reduceByKey - Aggregate all values based on given Key

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

# Function to convert line in input RDD to key, value pair
# example
# ID, name, age, friends_count
def parseLine(line):
    field = line.split(",")
    age = int(field[2])
    friends_count = int(field[3])
    return (age, friends_count)

lines = sc.textFile("file:////C:/my_workspace/taming_big_data_apache_spark/data/fakefriends.csv")
rdd = lines.map(parseLine)
# Output of above line ...
# 33, 385
# 33, 2

# Calculating total friend count for every unique age
totalsByAge = rdd.mapValues(lambda x: (x, 1)) \
                .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Output of map ...
# (33, 385) - ((33, 385), 1)
# (26, 2) - ((26, 2), 1)

# Output of mapValues ...
# (33, 385) - (33, (385, 1))
# (33, 2) - (33, (2, 1))

# Output of reduceByKey ...
# (33, (387, 2))

# Averaging out friends per age group
avgFriendsByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])
# Output of mapValues()
# (33, (387, 2)) - (33, 193.5)

# Kick-off spark job
results = avgFriendsByAge.collect()
for result in results:
    print(result)
