import random
import statistics as s
x=[1,-1,0.5,0.5,-0.5,-0.5]#possible changes in x in one step
y=[0,0,0.75,-0.75,0.75,-0.75]#possible changes in y in one step
xavg=0
yavg=0
avg_distdev=0
avg_dispdev=0
testcases=10
t=int(input('Enter number of steps\n'))
avg_distance=0
def dist(x,y):#Calculates minimum number of hops required from origin to hexagon at (x,y) 
	if x<0:#make x positive
		x*=-1
	if y<0:#make y positive
		y*=-1
	verticalsteps=y/0.75
	if x>0.5*verticalsteps:
		return verticalsteps+(x-0.5*verticalsteps)
	else:
		return verticalsteps
print('T=',t)		
for i in range(0,testcases):#run given testcases for a fixed value of t
	xcord=0
	ycord=0
	displacement=0
	distance=0
	distarray=[]#records distance from origin after each move of bee
	displacementarray=[]#records displacement from origin after each move of bee
	for j in range(0,t):#calculate situation after t steps
		r=random.randrange(0,6,1)
		xcord+=x[r]
		ycord+=y[r]
		displacement=pow(pow(xcord,2)+pow(ycord,2),0.5)
		distance=dist(xcord,ycord)
		distarray.append(distance)
		displacementarray.append(displacement)
	xavg+=xcord
	yavg+=ycord
	avg_distdev+=s.stdev(distarray)
	avg_dispdev+=s.stdev(displacementarray)
	print('testcase:',i+1,'\nx=',xcord,'y=',ycord,'distance=',distance,'displacement',displacement)
	print('distancedeviation=',s.stdev(distarray),'displacementdeviation=',s.stdev(displacementarray))
	avg_distance+=dist(xcord,ycord)
xavg/=testcases
yavg/=testcases
avg_distance/=testcases
avg_distdev/=testcases
avg_dispdev/=testcases
print('AVERAGE: x=',xavg,'y=',yavg,'distance=',avg_distance,'distancedeviation',avg_distdev,'displacementdeviation',avg_dispdev)
#code above this line
input('')