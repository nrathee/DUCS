------------------
Problem Statement
------------------
A bee walks around on a honeycomb,an infinite tesselating hexagonal grid, starting at a fixed hexagon. At each step the bee moves to one of the six adjacent hexagon with
equal probability. If the adjacent hexagons are exactly 1 unit away from each other, then after T steps calculate
1.expected value of the bee's distance from starting hexagon
2.expected value of deviation of bee's distance from starting hexagon
--------------------------------
Using program from command line
--------------------------------
Assuming hexgrid.py is located in present working directory, type
	python hexgrid.py
You'll be prompted to enter number of steps that bee is allowed to take
	Enter number of steps
10 testcases will be run, displaying result of each testcase, and a final result that takes average of all testcases

---------------------------
Descisions and Assumptions
---------------------------
1. Displacement vs Distance
	-We couldn't decide which one to consider, so we included both.
	-Displacement is manhattan distance between origin and bee's final position
	-Distance is minimum number of hexagon hops required between orign and bee's final postion
2. Output too big?
	-We've decided to output results of each testcase instead of just average/expected values
	-In case you want just average/expeceted values, skip to last line of output
3. for sake of simplicity(and a smaller output size), number of testcases is fixed at 10
	-to change this, change value of 'testcases' variable in code 
4. Deviation of Distance
	-if bee moves 10 steps, then after each step, its distance is calculated from startpoint
	-then the standard deviation of these distances is calcualted.
5. Startpoint is always origin
	-because we have to calculate distance between two points only, it doesn't matter where those two points are.
	-because it keeps things simple
----------
Algorithm
----------
Following are the possible changes in x,y coordinates of bee after 1 step
x	| y
+1	| +0
-1	| +0
+0.5	| +0.75
+0.5	| -0.75
-0.5	| +0.75
-0.5	| -0.75	
Just pick one of them randomly and add to starting point.

To calculate distance from origin, given bee's final coordinates
1. calculate minimum number of vertical steps required to reach final coordinates
2. each vertical step can increment xcoordinates by 0.5, if final xcoordinate is reachable within these steps, then 'these steps' is the answer
3. else take some more horizontal steps, as required.