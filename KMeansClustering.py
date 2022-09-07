import numpy as np
import matplotlib.pyplot as plt
import random as rand

class KMC:

    def __init__(self,k) :
        self.k = k

    def read_data(self,file,dlmtr):
        self.data = np.genfromtxt(file,delimiter=dlmtr)

    def plot_Data(self):
        x_axis = self.data[:,0]
        y_axis = self.data[:,1]
        # cx = center_points[:,0]
        # cy = center_points[:,1]
        plt.scatter(x_axis,y_axis,s=0.5,marker="*",label="Initial Data")
        # plt.scatter(cx,cy,color="r",marker="^",label="Center Data")
        plt.xlabel("X value")
        plt.ylabel("Y value")
        plt.title("Initial Data Points")
        plt.legend()
        plt.show()

    def initial_center(self):
        center = rand.sample(self.data.tolist(),self.k)
        return np.array(center)


obj = KMC(6)
obj.read_data('jain_feats.txt'," ")
obj.plot_Data()
initial_values = obj.initial_center()
print(initial_values)
