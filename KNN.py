import operator
import numpy as np
import random as rand
from scipy.spatial import distance


class KNN:

    def read_data(self, filepath, delimiter):
        initial_data = np.genfromtxt(filepath, delimiter=delimiter)
        dataset_list = initial_data.tolist()
        rand.shuffle(dataset_list)

        self.train = []
        self.validation = []
        self.test = []

        for eachData in dataset_list:
            randNum = rand.random()
            if randNum >= 0 and randNum <= 0.7:
                self.train.append(eachData)
            elif randNum >= 0.7 and randNum <= 0.85:
                self.validation.append(eachData)
            else:
                self.test.append(eachData)

    def KNN_Classification(self, k):
        correct = 0
        L = {}
        for v in self.validation:
            major_class = {}
            L = {}
            for t in self.train:
                e_distance = distance.euclidean(
                    v[0:(len(v)-1)], t[0:(len(t)-1)])
                L[e_distance] = t
            sort_L = sorted(L.keys())
            count = 1
            major_class = {}
            for x in sort_L:
                if int(L[x][-1]) in major_class.keys():
                    major_class[int(L[x][-1])] = major_class[int(L[x][-1])]+1
                else:
                    major_class[int(L[x][-1])] = 0
                    major_class[int(L[x][-1])] = major_class[int(L[x][-1])]+1
                count = count + 1
                if(count > k):
                    break
            val = max(major_class.items(), key=operator.itemgetter(1))[0]
            if(int(v[-1]) == val):
                correct = correct + 1           
        print((correct/len(self.validation))*100)

    def KNN_Regression(self, k):
        L = {}
        correct = 0
        error = 0
        for v in self.validation:
            L = {}
            for t in self.train:
                e_distance = distance.euclidean(v[0:(len(v)-1)], t[0:(len(t)-1)])
                L[e_distance] = t[-1]
            sort_L = sorted(L.keys())

            count = 1
            total = 0.0
            for each in sort_L:
                total = total + L[each]
                count = count + 1
                if(count > k):
                    break
            value = total/k
            error = error + (v[-1]-value)**2
            if(int(v[-1]) == value):
                correct = correct + 1
        error_r = (error/len(self.validation))**(1/2)
        print(error_r)


object = KNN()
object.read_data('iris.csv', ",")
object.KNN_Classification(1)
object.KNN_Classification(3)
object.KNN_Classification(5)
object.KNN_Classification(10)
object.KNN_Classification(15)

object3 = KNN()
object3.read_data('diabetes.csv',",")
object3.KNN_Regression(1)
object3.KNN_Regression(3)
object3.KNN_Regression(5)
object3.KNN_Regression(10)
object3.KNN_Regression(15)
