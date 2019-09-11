# Crux of the codebase -
# Use Spark MLLib and Spark Dataframe API

from pyspark import SparkConf, SparkContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession

def load_regression_dataset(line):
    fields = line.split(",")
    return (float(fields[0]), Vectors.dense(float(fields[1])))

# Create a Spark session ...
spark = SparkSession.builder.master("local[*]").config("spark.sql.warehouse.dir", "file:///C:/temp").appName("LinearRegression").getOrCreate()

# Loading dataset for Linear regression experiment
dataset = spark.sparkContext.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/regression.txt")
reg_dataset_rdd = dataset.map(load_regression_dataset)

# Converted RDD to Spark Dataframe
col_names = ["label", "features"]
reg_dataset_df = reg_dataset_rdd.toDF(col_names)

# Prepare test and train datasets
train_test_df = reg_dataset_df.randomSplit([0.5, 0.5])
train_df = train_test_df[0]
test_df = train_test_df[1]

# Create Linear Regression model
lr_model = LinearRegression(maxIter = 10, regParam = 0.3, elasticNetParam = 0.8)

# Training our model
lr_trained_model = lr_model.fit(train_df)

# Predictions
predictions = lr_trained_model.transform(test_df).cache()

# Printing predictions and labels / actuals
predictions.createOrReplaceTempView("results")
spark.sql("select label, prediction from results").show()

spark.stop()
