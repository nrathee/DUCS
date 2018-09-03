import random
x=[1,-1,0.5,0.5,-0.5,-0.5]
y=[0,0,1,-1,1,-1]
xavg=0
yavg=0
t=16
for i in range(0,testcases):
	xcord=0
	ycord=0
	for j in range(0,t):
		r=random.randrange(0,6,1)
		xcord+=x[r]
		ycord+=y[r]
	xavg+=xcord
	yavg+=ycord
xavg/=testcases
yavg/=testcases
print(xavg,yavg)
#code above this line
a=input()