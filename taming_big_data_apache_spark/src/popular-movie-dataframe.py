from pyspark.sql import SparkSession
from pyspark.sql import Row

# Helper functions ...
def load_movie_names():
    movie_dict = {}
    with open("C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.item") as file:
        for line in file:
            fields = line.split("|")
            movie_id = int(fields[0])
            movie_name = str(fields[1].encode("utf-8","ignore"))
            movie_dict[movie_id] = movie_name
    
    return movie_dict


# Boilerplate code
spark = SparkSession.builder.master("local[*]").config("spark.sql.warehouse.dir", "file:///C:/temp").appName("MostpopularMovie").getOrCreate()

# Loading movie names for lookup
movie_dict = load_movie_names()

# Loading movie ratings dataset
movie_ratings_dataset = spark.sparkContext.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.data")
movie_ratings_rdd = movie_ratings_dataset.map(lambda x: Row(movie_id = x.split()[1]))

movie_ratings_df = spark.createDataFrame(movie_ratings_rdd)
movie_ratings_df.createOrReplaceTempView("movies")

# Debugging purpose ...
# movies = spark.sql("select * from movies")
# for movie in movies.collect():
#     print(movie)

# popular_movies = movie_ratings_df.groupBy("movie_id").count().orderBy("count", ascending = False).show(10)
popular_movies = movie_ratings_df.groupBy("movie_id").count().orderBy("count", ascending = False).take(10)

for movie in popular_movies:
    print(movie_dict[int(movie["movie_id"])][1:], movie["count"])

spark.stop()    