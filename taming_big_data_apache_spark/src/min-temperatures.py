# Summary
# Main attraction is filter()

from pyspark import SparkConf, SparkContext
import time

# Function to convert line in raw dataset to extract key fields
# StationID, Timestamp, Property, Value .....
def parseData(line):
    fields = line.split(",")
    station = fields[0]
    weather_prop = fields[2]
    weather_prop_value = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    
    return (station, weather_prop, weather_prop_value)

start_time = time.time()
# Boiler plate code for setting up spark job confib
conf = SparkConf().setMaster("local").setAppName("MinTemperatureByStation")
sc = SparkContext(conf = conf)
after_config = time.time()
print("Time taken for setting up Spark job config ", after_config - start_time)

# Reading dataset with temperatures
dataset = sc.textFile("file:////C:/my_workspace/taming_big_data_apache_spark/data/1800.csv")
dataset_rdd = dataset.map(parseData)
after_read_data = time.time()
# Output is
# ("station", "weather_prop", "weather_prop_value")
print("Time taken for reading dataset ", after_read_data - after_config)

# Filter out only records having weather property - TMIN
weather_tmin_rdd = dataset_rdd.filter(lambda x: "TMIN" in x[1])
after_filter = time.time()
print("Time taken for filtering out MIN temperature related records ", after_filter - after_read_data)

# Find minimum temperature per station
weather_tmin_striped_rdd = weather_tmin_rdd.map(lambda x: (x[0], x[2]))
min_temp_per_station_rdd = weather_tmin_striped_rdd.reduceByKey(lambda x,y: min(x,y))
results = min_temp_per_station_rdd.collect()
after_finding_min_temp = time.time()
print("Time taken for finding minimum temperature ", after_finding_min_temp - after_filter)

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))

