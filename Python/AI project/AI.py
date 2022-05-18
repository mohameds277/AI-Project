#!/usr/bin/env python3

######GRAPH of palestine map 
from calendar import c
from cmath import cos
from email.policy import default
from hashlib import algorithms_available
from itertools import count
from ntpath import join
from pickle import NONE
from turtle import done
import numpy as np 
from collections import deque
from collections import namedtuple
from sympy import true
import os



##########################################################################################
cites = []
costs = []
areal_distance_h1 = []
walking_distance_h2 = []



graphs={}

graphs_h = {}


def files_readers():

    #reading the cities files and appending them into a list 
    with open("cities.txt", "r") as cities_file:
        for city in cities_file:
            trimed_line = city.strip()
            cites.append(trimed_line)



    # store the lists of cities names into dictionary as keys 
    for i in cites:
        graphs[i] = []



    for i in cites:
        graphs_h[i] = [[]]


    # printing the dictionary that contains keys only (cities names )
    print(graphs)


    with open("costs.txt", "r") as costs_file:
        for cost in costs_file:
            trimed_costs = cost.split(",")
            costs.append(trimed_costs)


    #reading Herustic1 (ArealDistance)
    with open("ArealDistance_h1.txt" , "r") as areal_file:
        for areal in areal_file:
            trimed_areal = areal.split()
            areal_distance_h1.append(trimed_areal)


    #reading walkingDistance Herustic 2 file 
    with open("walkingDistance_h2.txt","r") as walking_file:
        for walking in walking_file:
            trimed_walking = walking.split(",")
            walking_distance_h2.append(trimed_walking)


    print("\n\n\n\n")

#building graph map using the cost 
def graph_cost():
    counter = 0 
    for i in cites:
        print("creating Graph for city {}".format(i))
        for j in range(len(costs)):
            if (int(costs[counter][j]) > 0 ):
                print("city ->({})<- connected with city {}".format(i  , cites[j]))
                graphs[i].append(cites[j])

        counter = counter + 1 
    print(graphs)

# building graph map using walkingDistance heurstic
def graph_h():
    space = "-"
    joined_list  = []
    for i in cites:
        print("creating Graph for city {}".format(i))
        for j in range(len(costs)):
            if (int(costs[counter][j]) > 0 ):
                print("city ->({})<- connected with city {}".format(i  , cites[j]))
                joined_list = cites[j] + space + walking_distance_h2[counter][j]
                my_result = tuple((joined_list.split('-')))
                graphs[i].append(my_result)



        counter = counter + 1 

 

 
numbers_list = []
def gready_path(graphs , start , end ):
    open_list = set([start])
    close_list=set([])

    g = {}

    g[start] = 0


    while len (open_list> 0 ):
         n = None
         for h in open_list:
             pass

             
        

         for i in graphs:
            for j in range (len(graphs[i])):
            # numbers_list.clear
                for k in range(len(graphs[i][j])):
                 if(graphs[i][j][k].isnumeric()):
                    #print(graphs[i][j][k])
                    print(numbers_list.append(graphs[i][j][k]))


##############################################################################################3

graph = {'Saffad': set(['Akka', 'Tabaria']),
         'Akka': set([ 'Haifa','Nasrah', 'Tabaria','Saffad']),
         'Tabaria': set(['Bisan','Nasrah','Akka', 'Saffad']),
         'Bisan': set(['Nablus','Jenin','Nasrah','Tabaria','Nasrah']),
         'Nasrah': set(['Bisan','Jenin','Haifa','Akka', 'Tabaria']),
         'Haifa': set(['Tulkarm','Jenin','Nasrah','Akka']),
         'Jenin': set(['Bisan', 'Nasrah','Haifa','Tulkarm','Nablus']), 
         'Nablus': set(['Bisan','Jenin','Tulkarm','Yaffa','Ramla','Ramallah','Jericho']),
         'Yaffa' :set(['Tulkarm','Ramla','Nablus']),
         'Ramla' :set(['Yaffa','Gaza','Hebron','Bethlehem','Jerusalem','Ramallah','Nablus']),
         'Ramallah':set(['Nablus','Ramla','Jerusalem','Jericho']),
         'Jericho': set(['Nablus','Ramallah','Jerusalem','Bethlehem']),
         'Bethlehem': set(['Jericho','Jerusalem','Ramla','Hebron']),
         'Hebron': set(['Bethlehem','Ramla','Gaza','Saba']),
         'Gaza': set(['Ramla','Saba','Hebron']),
         'Saba': set(['Hebron','Gaza']),
         'Tulkarm':set(['Haifa','Yaffa','Nablus','Jenin']),
         'Jerusalem':set(['Jericho','Ramallah','Ramla','Bethlehem'])   
        }


 


#Depth-first algorthm
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
    print("this are results for dfs")            
    print(path)
    print(goal)



#Bredth first algrothim
def bfs_paths(graph, start1, goal1):
    queue1 = [(start1, [start1])]
    while queue1:
        (vertex1, path1) = queue1.pop(0)
        for next in graph[vertex1] - set(path1):
            if next == goal1:
                yield path1 + [next]
            else:
                queue1.append((next, path1 + [next]))
    print("this is for bfs")
    print(path1)
    print(goal1)

####################################################################################################
class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    

    def a_star_algorithm(self, start_node, stop_node):
 
        open_list = set([start_node])
        closed_list = set([])
 
        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] < g[n] :
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

  
            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
adjacency_list = {
          'Saffad': [('Akka', 94),('Nasrah', 145)],
          'Akka': [ ('Haifa', 55),('Nasrah',41) ,('Saffad',101)],
          'Nasrah': [('Jenin',75),('Haifa',106),('Saffad', 145)],
          'Haifa': [('Jenin',202),('Nasrah',106),('Akka',55)],
          'Jenin': [('Nasrah', 75),('Haifa', 202),('Tubas', 54),('Sabastia',63)],
          'Nablus': [('Qalqilya', 180),('Tubas', 41),('Sabastia',54),('Salfit', 128),('Ramallah',81),('Jericho',217)],
          'Yaffa' :[('Qalqilya',83),('Ramla',40)],
          'Ramla' :[('Yaffa',40),('Jerusalem', 87),('Ramallah', 87)],
          'Ramallah':[('Nablus', 81),('Ramla', 87),('Jerusalem', 42),('Jericho', 90),('Salfit', 66)],
          'Jericho': [('Nablus', 217),('Ramallah', 90),('Bethlehem', 76)],
          'Bethlehem': [('Jericho', 76),('Jerusalem', 17),('Halhoul', 73),('Hebron', 79),],
          'Hebron': [('Bethlehem', 79),('Halhoul', 14),('Dura', 20)],
          'Tulkarm':[('Sabastia',63)],
          'Jerusalem':[('Ramallah', 42),('Ramla', 87),('Bethlehem',17)],
          'Dura': [('Hebron', 20)],
          'Halhoul':[('Bethlehem', 73),('Hebron', 14)],
          'Tubas': [('Jenin', 54),('Nablus', 41)],
          'Qalqilya': [('Nablus', 180),('Yaffa', 83)],
          'Salfit': [('Nablus', 128),('Ramallah', 66)],
          'Sabastia': [('Jenin', 63),('Nablus', 54),('Tulkarm', 63)]
}




####################################################################################################

class Graph1:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]



    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0


        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

  
            for v in open_list:
                if n == None or g[v] < g[n] :
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None


            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path


            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
adjacency_list = {
          'Saffad': [('Akka', 87),('Nasrah', 95)],
          'Akka': [ ('Haifa', 40),('Nasrah',74) ,('Saffad',87)],
          'Nasrah': [('Jenin',61),('Haifa',78),('Saffad', 95)],
          'Haifa': [('Jenin',97),('Nasrah',78),('Akka',40)],
          'Jenin': [('Nasrah', 61),('Sabastia', 52),('Haifa', 133),('Tubas',41)],
          'Nablus': [('Qalqilya', 96),('Tubas', 34),('Sabastia',29),('Salfit', 64),('Ramallah',67),('Jericho',131)],
          'Yaffa' :[('Qalqilya',57),('Ramla',39)],
          'Ramla' :[('Yaffa',39),('Jerusalem', 80),('Ramallah', 81)],
          'Ramallah':[('Nablus', 67),('Ramla', 81),('Jerusalem', 42),('Jericho', 57),('Salfit', 46)],
          'Jericho': [('Nablus', 131),('Ramallah', 57),('Bethlehem', 64)],
          'Bethlehem': [('Jericho', 64),('Jerusalem', 16),('Halhoul', 47),('Hebron', 56),],
          'Hebron': [('Bethlehem', 56),('Halhoul', 11),('Dura', 16)],
          'Tulkarm':[('Sabastia', 44)],
          'Jerusalem':[('Ramallah', 42),('Ramla', 80),('Bethlehem',16)],
          'Dura': [('Hebron', 16)],
          'Halhoul':[('Bethlehem', 47),('Hebron', 11)],
          'Tubas': [('Jenin', 41),('Nablus', 34)],
          'Qalqilya': [('Nablus', 96),('Yaffa', 57)],
          'Salfit': [('Nablus', 64),('Ramallah', 46)],
          'Sabastia': [('Jenin', 52),('Nablus', 29),('Tulkarm', 44)]
}





if __name__ == "__main__":
    while true:
        print("AI project for Path algorthims")
        print("please Choose the Path Algorthim")
        print("1-Algorthm #1 Depth search First")
        print("2-Algorthm #2 Breadthsearch First")
        print("3-Algorthm #3 Greedy Search ")
        print("4-Algorthim #4 A* search")
        print("5-Terminate Program")
        print("6-creating graph from Cities costs h1 and h2 txt files")

        choice = int(input('Enter your choice: ')) 
        match choice:
            case 1: 
                os.system('clear')
                print("Depth Search Algorthm ")
                start = str(input('Enter Starting point: ')) 
                ending = str(input('Enter ending point: ')) 
                list(dfs_paths(graph, start, ending)) 
                print("\n\n\n")

                pass

            case 2:
                os.system('clear')
                print("BreadthSearch Algorthm ")
                start = str(input('Enter Starting point: ')) 
                ending = str(input('Enter ending point: ')) 
                list(bfs_paths(graph, start, ending))
                print("\n\n\n")
                pass
                
                
            case 3:
                os.system('clear')          #this is a work in progress 
                print("Greedy algorithms search ")
                start = str(input('Enter Starting point: ')) 
                ending = str(input('Enter ending point: ')) 
                print("\n\n\n")
                pass
                
            case 4:
                os.system('clear')
                print("A* Algorthm search ")
                h_choice = int(input("Please choose the Herustic data 1->H1 , 2->H2  "))
                match h_choice:
                    case 1 : 
                        print("Using H1")
                        start = str(input('Enter Starting point: ')) 
                        ending = str(input('Enter ending point: ')) 
                        graph1 = Graph(adjacency_list)
                        graph1.a_star_algorithm( start , ending )
                        print("\n\n\n")
                        pass
                    case 2 :
                        print("Using H2")
                        start = str(input('Enter Starting point: ')) 
                        ending = str(input('Enter ending point: ')) 
                        graph1 = Graph1(adjacency_list)
                        graph1.a_star_algorithm(start, ending)
                        print("\n\n\n")
                        pass
                    case default : 
                        print("Wrong Entry ")
                        pass
            
            case 5:
                print("TERMINATING program......")
                exit(1)
            case 6 : 
                print("reading data from file and creating graph \n")
              
                files_readers()
                print("\n\n\n")
                graph_cost()
                print("\n\n\n")

            case default:
                print("Enrty Error")
                pass
 

        













 