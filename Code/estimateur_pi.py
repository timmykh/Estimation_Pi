#### Estimation de Pi ##  M2 SEP  ####
#### Timmy KHIEV # Leon BOUR ####

 
## 0 - Importation de SparkConf/SparkContext

from pyspark import SparkConf, SparkContext
import pandas as pd
import numpy as np
import math
import random
import time


## 1 - Instanciation de Spark

if __name__ == "__main__":
    conf = SparkConf().setAppName('estimateur_pi').setMaster("local")
    sc = SparkContext(conf = conf)
    sc.setLogLevel("ERROR")

## 2 - Simulation d'un point dans le cercle unite

def cercle_unite(p):
    x, y = random.random(), random.random()   
    return 1 if x*x + y*y < 1 else 0 

print(cercle_unite(3))

## 3 - Estimateur avec Spark

def spark_estim(n):
    count = sc.parallelize(range(0, n))
    k = count.map(cercle_unite)
    ins = k.filter(lambda x: x==1).count()
    estimateur_pi = 4 * ins/n
    return  estimateur_pi

tps1 = time.time()
pi_spark = spark_estim(100000)
tps2 = time.time()
Temps_spark = tps2 - tps1

## 4 - Estimateur avec numpy

def numpy_estim(n):
    count = np.array(range(0, n))
    cercle = np.array([cercle_unite(i) for i in count])
    ins = len(cercle[cercle == 1])
    estimateur_pi = 4*ins/n
    return estimateur_pi

tps_1 = time.time()
pi_numpy = numpy_estim(100000)
tps_2 = time.time()
Temps_numpy = tps_2 - tps_1

## 5 - Validation du programme/affichage des resultats

print("n = 100.000")
arr = np.array([[Temps_spark, Temps_numpy], [pi_spark, pi_numpy], [math.pi-pi_spark, math.pi-pi_numpy]])
tab = pd.DataFrame(arr, index=["Chrono", "Estimation", "Ecart"], columns=["Spark", "numpy"])
print(tab)

#Pour n = 1.000.000
tps_1 = time.time()
pi_numpy = numpy_estim(1000000)
tps_2 = time.time()
Temps_numpy = tps_2 - tps_1

tps1 = time.time()
pi_spark = spark_estim(1000000)
tps2 = time.time()
Temps_spark = tps2 - tps1

print("n = 1.000.000")
arr = np.array([[Temps_spark, Temps_numpy], [pi_spark, pi_numpy], [math.pi-pi_spark, math.pi-pi_numpy]])
tab2 = pd.DataFrame(arr, index=["Chrono", "Estimation", "Ecart"], columns=["Spark", "numpy"])
print(tab2)

 
sc.stop()