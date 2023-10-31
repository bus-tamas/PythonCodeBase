class Graph(object):
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        edges=[]
        for vertex in self.graph:
            for neighbours in self.graph[vertex]:
                edges.append((vertex,neighbours))
        return edges
    
class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

madrid = City('Madrid','Spain' ,'3.2M')
budapest = City('Budapest','Hungary' ,'1.7M')
berlin = City('Berlin','Germany' ,'3.6M')
cairo = City('Cairo','Egypt' ,'9.6M')
    
g = Graph()
g.add_vertex(berlin)
g.add_vertex(budapest)
g.add_vertex(madrid)
g.add_vertex(cairo)

g.add_edge(berlin,budapest)
g.add_edge(madrid,cairo)
g.add_edge(cairo,budapest)

for city in g.get_vertices():
    print(city.name)

for edge in g.get_edges():
    city1, city2 = edge
    print(f"{city1.name} <--> {city2.name}")