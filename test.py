import math

def function(x):
    y = (x/5) - 5
    y = 2 * y
    y = -1 * (y/5)
    return y

def scalMult(c, a):
    v = len(a) * [0]
    for i in range(len(a)):
        v[i] = c*a[i]
    return v

def vecAdd(a,b):
    if(len(a) == len(b)):
        v = len(a)*[0]
        for i in range(len(a)):
            v[i] = a[i] + b[i]
    return v

def dot(a,b):
    return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])

def cross(a,b):
    v = [(a[1]*b[2]) - (a[2]*b[1]), (a[2]*b[0]) - (a[0]*b[2]), (a[0]*b[1]) - (a[1]*b[0])]
    return v

def rodRot(v, k, theta):
    secOne = scalMult(math.cos(theta), v)
    secTwo = scalMult(math.sin(theta), cross(k,v))
    secThree = scalMult(dot(k, v) * (1 - math.cos(theta)), k)
    return  vecAdd(vecAdd(secOne, secTwo), secThree)

testVec = [10,54,26]
othTestVec = [4,2,5]
normVecY = [math.cos(math.radians(34)),math.sin(math.radians(34)),0]

#print(testVec)
#print(normVecY)
#print(scalMult(math.sin(math.pi * .5), testVec))
for i in range(200):
    testVec = rodRot(testVec,normVecY, math.radians(1))
    print(testVec)

#print(dot(testVec,normVec))