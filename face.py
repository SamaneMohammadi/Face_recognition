import glob
import numpy as np
from PIL import Image

#loading image from train and test
test_image = glob.glob('test/*.jpg')
train_image = glob.glob('train/*.jpg')


#convert train_image to array
images_train = [Image.open(i)  for i in train_image]
train_array =  np.array([np.array(Image.open(i).convert('L')).flatten()  for i in train_image ])


#calculate the normal-vector for train_image
avg_vector=[]
for j in range(0,len(train_array[1])):
    avg_normal = []
    for i in range(0,len(train_array)):
        avg_normal.append(train_array[i][j])
    sum_avg_normal = sum(avg_normal)/len(train_array)
    avg_vector.append(sum_avg_normal)


## calculate the diff between train_array and avg_vector and create covareance matrix
train_norm_matrix = np.zeros((len(train_array),len(train_array[1])))
for j in range(0,len(train_array[1])):
    for i in range(0,len(train_array)):
        train_norm_matrix[i][j]=train_array[i][j]- avg_vector[j]



# decrease of demantion of matrix by multiplection matrix.transpose and matrix
train_matrix = np.matmul(train_norm_matrix,train_norm_matrix.transpose())
eign_values,eign_vectors = np.linalg.eig(train_matrix)

#create weight_vector_train
eigen_value_matrix = np.matmul(train_norm_matrix.transpose(),eign_vectors)
weight_vector_train = np.matmul(train_norm_matrix,eigen_value_matrix)


##convert test_image to array
images_test = [Image.open(i)  for i in test_image]
test_array =  np.array([np.array(Image.open(i).convert('L')).flatten()  for i in test_image ])

##normalize the test array
for i in range(0,len(test_array)):
    test_normal=test_array[i]-avg_vector
    weight_vector_test = np.matmul(test_normal.transpose(),eigen_value_matrix)

    diff = []
    for j in range(0,len(train_array)):
        diff_image = sum((1/len(train_array[0]))*abs(weight_vector_test - weight_vector_train[j]))
        if diff_image < 0.5:
            print("image founded and I am happy :)")
            print("the image of {} in test is similar the image {} of train\n---------------------------".format(i,j))
            break








