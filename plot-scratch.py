import numpy
import matplotlib.pyplot as plt
a = numpy.loadtxt('samples/0.raw',skiprows=1,delimiter=',')
plt.plot(a[:,0],a[:,1])
plt.show()
print(len(a))

#I want to get the slopes of the initial linear parts (that's the Young's modulus)
	#Find initial linear part (these have different numbers of points in them!)
	#We can use stuff from notebook4? 3? to get the linear regression of that inital part


#I want to average that over all of the samples



