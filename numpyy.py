# starting one dimensional array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("NumPy successfully installed!")
print("Array:", arr)


# 2 dimensional array
import numpy as np

arr2=np.array([[6,5],[3,6],[8,9]])
print(arr2)


# a matrix with all zeros
import numpy as np

array_zeros=np.zeros([3,3])
print(array_zeros)


#populate arrays with random numbers
import numpy as np

random_create_array_to_50_to_100=np.random.randint(low=50,high=101,size=6)
print(random_create_array_to_50_to_100)


# create a linear dataset
import numpy as np

feature=np.arange(6,21)
print(feature)
label=3*feature+4
print(label)


# add some noise to the Dataset
import numpy as np

noise=np.random.random(15)*4-2
print(noise)
label=label+noise
print(label)