#solving the first order differential equation via Runge-Kutta 4th order method
import numpy as np
import matplotlib.pyplot as plt

p = float(input('Enter the number at which the value of y is to be determined : '))

#defining the step height for the method
h = 0.05

#defining the no. points need to be evaluated for given h
n = int(10/h)

#defining the function which needs to be solved i.e. f(x,y) part of dy/dx = f(x,y)
def f(x,y):
    '''
    returns the function f(x,y)
    '''
    return (3*np.exp(-x))-0.4*y

#definig the rungi-kutta 4th range method 
def Rungi_Kutta_4th_Runge(xi,yi):
    '''
    returns the y[i+1] value satisfying the equation dy/dx = f(x,y) for a x[i+1]
    '''
    k1 = f(xi,yi)
    k2 = f(xi+h/2,yi+k1*h/2)
    k3 = f(xi+h/2,yi+k2*h/2)
    k4 = f(xi+h,yi+k3*h)
    return yi + (k1 + 2*k2 + 2*k3 + k4)*h*(1/6.0)

#generating the arrays required to store the x and y values
x = np.zeros(n)
y = np.zeros(n)
y[0] = 5

#calculating the values of elements in x and y array and storing it
for i in range(1,n):
    x[i] = x[i-1] + h
    y[i] = Rungi_Kutta_4th_Runge(x[i-1],y[i-1])

for i in range(len(x)):
    if abs(x[i]-p) <= h:
        print y[i]
        break

plt.figure(1)
plt.plot(x,y)
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.show()



    
    

