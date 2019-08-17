# Summary of codebase -
# spark sql queries ...

from pyspark.sql import SparkSession
from pyspark.sql import Row

import collections

spark = SparkSession.builder.master("local[*]").config("spark.sql.warehouse.dir", "file:///C:/temp").appName("SparkSQL").getOrCreate()

def mapper(line):
    fields = line.split(",")

    return Row(ID = int(fields[0]), name = str(fields[1].encode("utf-8")), age = int(fields[2]), num_friends = int(fields[3]))

lines = spark.sparkContext.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/fakefriends.csv")
people = lines.map(mapper)

# First step infers schema of spark dataframe and second step creates temporary view to query data
schema_people = spark.createDataFrame(people).cache()
schema_people.createOrReplaceTempView("people")

# Firing basic SQL queries on Spark dataframe
teenagers = spark.sql("select * from people where age >= 13 and age <= 25")
# for teen in teenagers.collect():
#     print(teen)

# Applying some functions on Spark dataframe
grouped_people = schema_people.groupBy("age").count().orderBy("age").show()

