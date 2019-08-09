# Summary of code: Counting words in a Book
# Main attraction - flatMap(), sortByKey()
# map v/s flatMap - 
# map transforms RDD into new one such that new RDD contains an element for every element in old one
# flatMap transforms RDD in a way that every row in old RDD is blown out into multiple rows in new RDD.
  
import re
from pyspark import SparkConf, SparkContext

def normalize_word(line):
    return re.compile(r"\W+", re.UNICODE).split(line.lower())

conf = SparkConf().setMaster("local").setAppName("Word-Count App")
sc = SparkContext(conf = conf)

# Reading dataset(book written by Frank Kane)
book = sc.textFile("file:////C:/my_workspace/taming_big_data_apache_spark/data/Book.txt")
words = book.flatMap(normalize_word) # Output -> ['self', 'employment', 'building', 'an', 'internet']
# words = book.map(normalize_word) # Output -> [['self', 'employment', 'building', 'an', 'internet', 'business', 'of', 'one']]

# Counting total occurrence of every word
word_cnt_RDD = words.map(lambda x: (x, 1))
word_cnt_agg_RDD = word_cnt_RDD.reduceByKey(lambda x, y: x + y)

# Sort words in the order of word count
word_cnt_swapped_RDD = word_cnt_agg_RDD.map(lambda x: (x[1], x[0]))
word_cnt_sorted_RDD = word_cnt_swapped_RDD.sortByKey()
results = word_cnt_sorted_RDD.collect()

# Printing results
for result in results:
    count = str(result[0])
    word = result[1].encode('ascii', 'ignore')
    if (word):
        print(word.decode() + ":\t\t" + count)


