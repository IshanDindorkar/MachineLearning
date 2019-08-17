# Summary of code ...
# Calculate total amount spent by each customer 
# and sort the results by total amount

# Basic imports ...
from pyspark import SparkConf, SparkContext

# Helper functions ....
def parse_customer_record(line):
    ''' Parse every line in dataset and spit out essential data points
        like customer ID and amount spent '''
    fields = line.split(",")
    customer_ID = fields[0]
    amount = float(fields[2])

    return (customer_ID, amount)

# Boilerplate code
conf = SparkConf().setMaster("local").setAppName("Total-Amount-By-Customer Job")
sc = SparkContext(conf = conf)

# Reading dataset and transforming to extract essential items
dataset_RDD = sc.textFile("file:///C:/my_workspace/taming_big_data_apache_spark/data/customer-orders.csv")
customer_amount_RDD = dataset_RDD.map(parse_customer_record)

# Aggregating money spent by customers
customer_amount_agg_RDD = customer_amount_RDD.reduceByKey(lambda x, y: x + y)

# Sort results by amount spent by customer
customer_amount_swapped_RDD = customer_amount_agg_RDD.map(lambda x: (x[1], x[0]))
customer_amount_sorted_RDD = customer_amount_swapped_RDD.sortByKey(False)
results = customer_amount_sorted_RDD.collect()

# Printing results
for key, value in results:
    print(value + "\t{:.2f}".format(key))