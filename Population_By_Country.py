import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('C:\\Users\Monster\Desktop\python_projeler\population_by_country_2020.csv', delimiter=',', dtype="str", skiprows=1, max_rows=10)


# #Settings
plt.title('Country Populations')
plt.xlabel('Countries', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.yticks(range(0, 2000000000, 100000000))

#Creating b ndarray for converting datas str to the float
b = np.zeros_like(a, dtype='float32')
b[:, 0] = a[:, 1].astype('float32')

plt.bar(a[:, 0], b[:, 0], color='yellow', edgecolor='blue', width=0.1, align='center', linewidth=1)
plt.show()


###########################################################################

# # #Alternative Code is below
# import numpy as np
# import matplotlib.pyplot as plt
#
# a = np.loadtxt('C:\\Users\Monster\Desktop\python_projeler\population_by_country_2020.csv', delimiter=',', dtype="str", skiprows=1)
#
# plt.pie(a[:, 1], labels=a[:, 0], colors=['red', 'green', 'blue', 'yellow', 'magenta'] * 47, explode=[0]* 235, autopct='%.2f')
# plt.show()

