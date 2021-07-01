import numpy as np
import datetime

a = np.loadtxt('C:\\Users\Monster\Desktop\population_by_country_2020.csv', delimiter=',', dtype="str", skiprows=1)


for i in range(len(a)):
    print(a[i])
