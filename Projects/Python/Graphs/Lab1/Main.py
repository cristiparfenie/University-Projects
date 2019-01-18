class Cost:
    def __init__(self):
        self._cost = {}

    def addCostToEdge(self, vertice1, vertice2, c):
        try:
            self._cost[(vertice1, vertice2)] = c
        except ValueError:
            print("No edge! " + str(vertice1) + " " + str(vertice2) + "\n")

    def getCostFromEdge(self, vertice1, vertice2):
        try:
            return self._cost[(vertice1, vertice2)]
        except ValueError:
            print("No edge! " + str(vertice1) + " " + str(vertice2) + "\n")

    def setCostOfEdge(self, vertice1, vertice2, newCost):
        try:
            self._cost[(vertice1, vertice2)] = newCost
        except ValueError:
            print("No edge! " + str(vertice1) + " " + str(vertice2) + "\n")

class DirectGraph:
    def __init__(self, n):
        self._verticeIn = {}
        self._verticeOut = {}
        for i in range(n):
            self._verticeIn[i] = []
            self._verticeOut[i] = []

    def parseDict(self):
        return self._verticeOut.keys()

    def length(self):
        return len(self._verticeOut.keys())

    def parseVerticeOut(self, vertice):
        if vertice in self._verticeOut.keys():
            return self._verticeOut[vertice]
        else:
            print(str(vertice) + " is not a vertex")

    def parseVerticeIn(self, vertice):
        if vertice in self._verticeIn.keys():
            return self._verticeIn[vertice]
        else:
            print(str(vertice) + " is not a vertex")

    def isEdge(self, vertice1, vertice2):
        if vertice1 in self._verticeOut.keys():
            return vertice2 in self._verticeOut[vertice1]
        else:
            print("No edge! " + str(vertice1) + " " + str(vertice2) + "\n")

    def addEdge(self, vertice1, vertice2):
        if not self.isEdge(vertice1, vertice2):
            self._verticeOut[vertice1].append(vertice2)
            self._verticeIn[vertice2].append(vertice1)
        else:
            print("Edge already there!\n")

    def inDegree(self, vertice):
        return len(self._verticeIn[vertice])

    def outDegree(self, vertice):
        return len(self._verticeOut[vertice])

def initGraph(DirectGraph):

    f = open("input", "r")

    Line = f.readline().strip()

    Line = Line.split(" ")
    n = int(Line[0])
    m = int(Line[1])

    graph = DirectGraph(n)
    cost = Cost()
    lines = f.readline().strip()

    while m > 0:
        lines = lines.split(" ")

        vertice1 = int(lines[0])
        vertice2 = int(lines[1])
        c = int(lines[2])

        graph.addEdge(vertice1, vertice2)
        cost.addCostToEdge(vertice1, vertice2, c)

        lines = f.readline().strip()

        m -= 1
    f.close()
    return graph, cost

def menu():
    print("1. Print the graph")
    print("2. Get the number of vertices")
    print("3. Given two vertices, find out whether there is an edge from the first one to the second one, and retrieve ")
    print("   the Edge_id if there is an edge (the latter is not required if an edge is represented simply as a pair of vertex identifiers)")
    print("4. Get the in degree and the out degree of a specified vertex")
    print("5. iterate through the set of outbound edges of a specified vertex (that is, provide an iterator). For each outbound edge,")
    print("   the iterator shall provide the Edge_id of the curren edge (or the target vertex, if no Edge_id is used)")
    print("6. Iterate through the set of inbound edges of a specified vertex (as above)")
    print("7. Get the endpoints of an edge specified by an Edge_id (if applicable)")
    print("8. Retrieve or modify the information (the integer) attached to a specified edge")
    print("0. Exit")

def start():
    graph, cost = initGraph(DirectGraph)

    while True:
        menu()
        option = int(input("Choose: "))
        if option < 0 or option > 8:
            print("Invalid command!\n")
        elif option == 0:
            break
        elif option == 1:
            for vertice1 in graph.parseDict():
                for vertice2 in graph.parseVerticeOut(vertice1):
                    print("[" + str(vertice1) + " , " + str(vertice2) + "]" + " -> " + str(cost.getCostFromEdge(vertice1, vertice2)))
        elif option == 2:
            vertices = graph.length()
            print("There are " + str(vertices) + " vertices!\n")
        elif option == 3:
            vertice1 = int(input("First vertex: "))
            vertice2 = int(input("Second vertex: "))
            if graph.isEdge(vertice1, vertice2) == 1:
                print("There's an edge from " + str(vertice1) + " to " + str(vertice2))
            else:
                print("There's no edge from " + str(vertice1) + " to " + str(vertice2))
        elif option == 4:
            vertice1 = int(input("Vertex: "))
            if vertice1 in graph.parseDict():
                print(graph.inDegree(vertice1))
                print(graph.outDegree(vertice1))
            else:
                print("Invalid vertex! ")
        elif option == 5:
            ok = 1
            vertice1 = int(input("Vertex: "))
            if vertice1 in graph.parseDict():
                for vertice2 in graph.parseVerticeOut(vertice1):
                    print("[" + str(vertice1) + " , " + str(vertice2) + "]")
                    ok = 0
                if ok == 1:
                    print("There are no outbound edges!\n")
            else:
                print("Invalid vertex! ")
        elif option == 6:
            ok = 1
            vertice1 = int(input("Vertex: "))
            if vertice1 in graph.parseDict():
                for vertice2 in graph.parseVerticeIn(vertice1):
                    print("[" + str(vertice2) + " , " + str(vertice1) + "]")
                    ok = 0
                if ok == 1:
                    print("There are no inbound edges!\n")
            else:
                print("Invalid vertex! ")
        elif option == 7:
            vertice1 = int(input("First vertex: "))
            vertice2 = int(input("Second vertex: "))
            if vertice1 in graph.parseDict() and vertice2 in graph.parseDict():
                print("The cost is: " + str(cost.getCostFromEdge(vertice1, vertice2)))
            else:
                print("Invalid vertexes! ")
        elif option == 8:
            vertice1 = int(input("First vertex: "))
            vertice2 = int(input("Second vertex: "))
            if vertice1 in graph.parseDict() and vertice2 in graph.parseDict():
                newCost = int(input("The new cost: "))
                cost.setCostOfEdge(vertice1, vertice2, newCost)
            else:
                print("Invalid vertexes! ")

start()
