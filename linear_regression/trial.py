from numpy import loadtxt,ones,zeros,array,linspace ,logspace
from pylab import scatter,xlabel,show,title,ylabel,contour,plot

data=loadtxt('ex1data1.txt',delimiter=',')

scatter(data[:,0],data[:,1],marker='o',c='b')

title('profits distribution')

xlabel('x axis')
ylabel('y axis')
show()
def compute_cost(X,Y,n,theta0,theta1):
    cost=0
    for i in range(0,n):
        cost+=theta0+theta1*X[i]-Y[i]
    cost=cost/(2*n)
    return cost
def theta0derivative(X,Y,n,theta0,theta1):
    d=0
    for i in range(0,n):
        d+=theta0+theta1*X[i]-Y[i]
    d=d/n
    return d
def theta1derivative(X,Y,n,theta0,theta1):
    d=0
    for i in range(0,n):
        d+=(theta0+theta1*X[i]-Y[i])*X[i]
    d=d/n
    return d

def gradientDescent(X,Y,n,alpha):
    theta0=1;
    theta1=1;
    prev_cost=compute_cost(X,Y,n,theta0,theta1)
    cost=prev_cost
    count=0
    while(cost<=prev_cost and count<1500):
        temp1=theta0-alpha*theta0derivative(X,Y,n,theta0,theta1)
        temp2=theta1-alpha*theta1derivative(X,Y,n,theta0,theta1)
        theta0=temp1
        theta1=temp2
        prev_cost=cost
        cost=compute_cost(X,Y,n,theta0,theta1)
        print(cost)
        count+=1
    return theta0,theta1
X=data[:,0]
Y=data[:,1]
n=X.size
alpha=0.01
theta0,theta1=gradientDescent(X,Y,n,alpha)
print(theta0)
print(theta1)
