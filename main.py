from pyspark import SparkContext

sc = SparkContext("local", "Exemple RDD")
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
rdd_squared = rdd.map(lambda x: x ** 2)
print(rdd_squared.collect())  # Résultat : [1, 4, 9, 16, 25]

# Arrêter proprement SparkContext
sc.stop()