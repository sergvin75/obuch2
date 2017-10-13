from urllib.request import urlopen
import numpy as np

filename = input()
f = urlopen(filename)
sbux = np.loadtxt('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')

print(sbux)

