from dijkstar import Graph, find_path
from latlongDist import calcDist
import webbrowser

coords = {}
myMode = 1
graph = Graph()

fObj = open("data.txt", "r+")
dataDump = fObj.readlines()
fObj.close() # be done with this

for dataLine in dataDump:

    if (dataLine[:-1] == "CONNECTIONS"):
        myMode = 2 # start reading file into the 
        continue

    if (myMode == 1):
        values = dataLine[:-1].split("*")
        coords[values[0]] = (values[1]) # index into -> lat long strings
    else:
        values = dataLine[:-1].split(" ")
        distValue = calcDist(coords[values[0]], coords[values[1]])
        graph.add_edge(values[0], values[1], distValue)

print ("Data read complete -> files loaded into graph matrix")

# take user input -> which two end node are we working with 
A = input("Enter start point -> ")
B = input("Enter target node -> ")

finalObj = find_path(graph, A, B)
print("Approx Walk Distance: ", finalObj.total_cost)

mapApiUrl = "https://www.google.com/maps/dir/" 

for nd in finalObj.nodes:
    temp = coords[nd].split(",")
    mapApiUrl = mapApiUrl + "/" + temp[0] + "," + temp[1]

webbrowser.open(mapApiUrl)