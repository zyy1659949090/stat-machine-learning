from numpy import *
from pylab import *

data = loadtxt('prostate_train.txt')
data = data.reshape(-1,9)

## reformat data as X and Y
y = data[:,8]
X = data[:,0:8]

def linregp(X,y):
    # takes N x p matrix X and a N x 1 vector y, and fits  
    # linear regression y = X*beta. NOTE indenting
    
    X1 = concatenate((ones((shape(X)[0],1)),X),axis=1)
    print shape(X1)
    
    print shape(y)
    betahat = linalg.inv(transpose(X1)*X1)*transpose(X1)*y
    yhat = X1*betahat
    RSS = transpose(y - yhat)*(y - yhat)
    return betahat,yhat,RSS

X = matrix(X)
y = transpose(matrix(y))

# do linear regression
temp = linregp(X,y)
betahat = temp[0]
yhat = temp[1]

# estimate covariance matrix
sigmahat2 = float((1.0/(len(y) - len(betahat)))*sum((yhat - y)**2))
print 'sigmahat2 = ',sigmahat2
X1 = concatenate((ones((shape(X)[0],1)),X),axis=1)
varbeta = linalg.inv(transpose(X1)*X1)*sigmahat2

# calculate Z-statistics
z = beta/diag(sqrt(varbeta))
# and print
print 'beta, z = ',concatenate((beta,z),axis=1)
