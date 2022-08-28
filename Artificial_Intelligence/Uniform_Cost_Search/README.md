# Uniform Cost Search
In this project i tried to find shortest path possible between two city, using ucs implementaion.

## What is Uniform-Cost Search ?
Uniform-Cost Search is an uniformed search algorithm that uses the lowest cost to find a path from the sources to the destination and mainly used in Artificial Intelligence. In this algorithm from the starting state we will visit the neighbour states and will choose the lowest cost state then we will choose the next lowest cost state from the all unvisited and neighbour states of the visited states, in this way we will try to reach the destination state but we wont continue the path through a goal state, even if we reach the goal state we will continue searching for other possible paths if there are multiple goals.

In this project we will try to find shortest path possible between two city, using ucs implementaion.

## About implementaion and efforts :
Firstly i define my graph with the build graph function. In build graph function, i used the dataset path as a paramater and read the data as dictionary reader. I define a default dictionary list variable and wrote the data to this list with for loop. In for loop it takes the data values as a column and for first column(city1) it appends the second(city2) and third cloumn(distance) as a value. And this function give me a graph like this:
 
* { ‘Balıkesir’: [ (‘Çanakkale’, ‘95’), (‘İstanbul’, ’155’), … ]
* ‘Çanakkale’: […] 
* … }

I used try-except blocks for this line so if data file does not exist or path is wrong it will print ‘File does not exist or path is wrong check your data’ and implementaion won’t crash. 

In the implementaion Uniform cost search function has three paramaters, graph, starting city and destination or goal city. Firstly i define visited array to look the nodes which i visited so the function won’t enter the infinite loop.

I define queue which is taking the values starting city and 0 (as a cost) at the 
beginning. After that, function entering the while loop when queue is not 
empty. In the loop firstly it sorts the queue with using the path cost function. 
Path cost function calculates the costs and then sort method sorting the queue 
by order first node of queue lowest cost, last node highest cost. After popping 
the first node of queue, function adds the node to visited if it’s not in visited. It 
checks the node if it is goal or not(It breaks and return path if node is goal and 
shortest cost). If node isn’t goal, function gets the neighbours of the nodes and
contiunes until find the goal with shortest path.

I define “run” function. Run function is like my main. After we run the program 
it calls the run functions(if dataset path is true) and it asks to user to get the 
starting city and destination city. When user entered* the one of the cities 
does_exist function works and looks for “input city” exists in the dataset or not. 
If city does not exist it print the ‘ “input city” does not exist’ message and exit. 
And does exist function saves the implementaion and program won’t crash. If 
everything is well, program works and find the shortest path and cost between 
giving cities.

*I used title method when reading the data and getting the inputs but there 
are different i’s in the dataset. First letters of İstanbul and İzmir are turkish i 
letter(uppercase İ and lowercase i) but second i letter of İzmir is english letter.
(The other cities letters “i” also english letter when used uppercase, letters are 
being I ) So my program sensitive to I, İ, ı, i. And python uppercase method 
doing all i to I so when we wrote istanbul converting is like Istanbul or 
ISTANBUL but data has İstanbul and program giving the statement: city does 
not exist. So we should use capital i for First letter of İstanbul and İzmir.

## Test Samples and outcomes:
1. İstanbul – Kayseri :
Shortest Path : - İstanbul – Eskişehir – Konya – Kayseri
- Distance : 435
2. Trabzon – İzmir :
- Shortest Path : Trabzon – Samsun – Ankara – Eskişehir – İzmir 
- Distance : 525
3. Çanakkale – Konya :
- Shortest Path : Çanakkale – İstanbul – Eskişehir – Konya 
- Distance : 375
4. Balıkesir – Adana :
- Shortest Path : Balıkesir – İzmir – Muğla – Antalya – Adana 
- Distance : 490
5. İstanbul – Paris :
- “Paris does not exist”
