import sys
from pyspark import SparkConf, SparkContext
from math import sqrt

def load_movie_names():
    movie_names = {}
    with open("C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.item", encoding = "ascii", errors = "ignore") as file:
        for line in file:
            fields = line.split("|")
            movie_names[int(fields[0])] = fields[1]
        
    return movie_names

def load_user_ratings(line):
    fields = line.split()

    return (int(fields[0]), (int(fields[1]), float(fields[2])))

def filter_duplicates(user_ratings):
    ratings = user_ratings[1]
    (movie_1, rating_1) = ratings[0]
    (movie_2, rating_2) = ratings[1]

    return movie_1 < movie_2

def make_pairs(user_ratings):
    ratings = user_ratings[1]
    (movie_1, rating_1) = ratings[0]
    (movie_2, rating_2) = ratings[1]

    return ((movie_1, movie_2), (rating_1, rating_2))

def compute_cosine_similarity(ratingPairs):
    numPairs = 0
    sum_xx = sum_yy = sum_xy = 0
    for ratingX, ratingY in ratingPairs:
        sum_xx += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        numPairs += 1

    numerator = sum_xy
    denominator = sqrt(sum_xx) * sqrt(sum_yy)

    score = 0
    if (denominator):
        score = (numerator / (float(denominator)))

    return (score, numPairs)

conf = SparkConf().setMaster("local[*]").setAppName("MovieSimilarities")
sc = SparkContext(conf = conf)

print("\nLoading movie names ...")
name_dict = load_movie_names()

# Loading movie ratings dataset
movie_ratings = sc.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/ml-100k/u.data")
movie_ratings_rdd = movie_ratings.map(load_user_ratings)

# Collecting all movies rated by the same user
joined_movie_ratings_rdd = movie_ratings_rdd.join(movie_ratings_rdd)

# Filter out duplicate pairs
filtered_movie_ratings_rdd = joined_movie_ratings_rdd.filter(filter_duplicates)

# Make movie pairs
paired_movies_rdd = filtered_movie_ratings_rdd.map(make_pairs)

# Group by pair of movies
grouped_movies_rdd = paired_movies_rdd.groupByKey()

# Calculate similarity between movies in a pair
movie_pair_similarities_rdd = grouped_movies_rdd.mapValues(compute_cosine_similarity).cache()

if (len(sys.argv) > 1):

    score_threshhold = 0.97
    co_occurrence_threshhold = 50

    # Taking movie id as input from user
    movie_id = int(sys.argv[1])

    filtered_results = movie_pair_similarities_rdd.filter(lambda pair_sim: \
        pair_sim[0][0] == movie_id or pair_sim[0][1] == movie_id \
            and pair_sim[1][0] > score_threshhold \
                and pair_sim[1][1] > co_occurrence_threshhold)
    
    results = filtered_results.map(lambda pairSim: (pairSim[1], pairSim[0])).sortByKey(ascending = False).take(10)
    for result in results:
        (sim, pair) = result
        # Display the similarity result that isn't the movie we're looking at
        similarMovieID = pair[0]
        if (similarMovieID == movie_id):
            similarMovieID = pair[1]
        print(name_dict[similarMovieID] + "\tscore: " + str(sim[0]) + "\tstrength: " + str(sim[1]))




