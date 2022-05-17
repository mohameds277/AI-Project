#!/usr/bin/env python3

######GRAPH of palestine map 
from calendar import c
from cmath import cos
from itertools import count
from pickle import NONE
from turtle import done
import numpy as np 



from collections import namedtuple




global start_point
global goal

counter = 0  


cites = []
costs = []
areal_distance_h1 = []
walking_distance_h2 = []

graphs={}



#reading the cities files and appending them into a list 
with open("cities.txt", "r") as cities_file:
    for city in cities_file:
        trimed_line = city.strip()
        cites.append(trimed_line)



# store the lists of cities names into dictionary as keys 
for i in cites:
    graphs[i] = []


# printing the dictionary that contains keys only (cities names )
print(graphs)


# DEBUGGIN : testing the list of cities readbilty 
# for city in cites:
#     print(city)


with open("costs.txt", "r") as costs_file:
    for cost in costs_file:
        trimed_costs = cost.split(",")
        costs.append(trimed_costs)

#debugging to check the readbility of costs file 
# for cost in costs:
#   #  print(cost)


# print("\n")
# print("\n")



 
#reading Herustic1 (ArealDistance)
with open("ArealDistance_h1.txt" , "r") as areal_file:
    for areal in areal_file:
        trimed_areal = areal.split()
        areal_distance_h1.append(trimed_areal)

#debugging : testing readblity of arealDistance file 
# for areal in areal_distance_h1:
#     print(areal)


#reading walkingDistance Herustic 2 file 
with open("walkingDistance_h2.txt","r") as walking_file:
    for walking in walking_file:
        trimed_walking = walking.split()
        walking_distance_h2.append(trimed_walking)

# print("\n")
# print("\n")

#debugging : testing readbilty of walking file herustics2 
# for walking in walking_distance_h2:
#  #   print(walking)



# print(cites[0])
# print(costs[0])
# print(areal_distance_h1[0])
# print(walking_distance_h2[0])


print("\n\n\n\n")


for i in cites:
    print("creating Graph for city {}".format(i))
    for j in range(len(costs)):
         if (int(costs[counter][j]) > 0 ):
             print("city {} connected with city {}".format(i  , cites[j]))
    counter = counter + 1 
             



 

# counter = 0 
# for i in costs:
#     city_cost = i.split(",")
#     print(city_cost)
 
#     counter = counter + 1 
# print(counter)



# creating graph map of the cities


    # for city in cites:
    #     trimed_line = city.split()
    #     cites.append(trimed_line)
    #     print(trimed_line)
    #     for cost in costs_file:
    #         trimed_costs = cost.split()
    #         print(trimed_costs)
    #     # for cost in costs_file:
    #     #     if ( cost > '0'  ):
    #     #         trimed_costs = cost.()
    #     #         graphs.update({city , cites[counter]})
    #     #         counter = counter + 1 
    #     #     counter = counter + 1 











 
#####################################################################################################



# graph = {'Saffad': set(['Akka', 'Tabaria']),
#          'Akka': set([ 'Haifa','Nasrah', 'Tabaria','Saffad']),
#          'Tabaria': set(['Bisan','Nasrah','Akka', 'Saffad']),
#          'Bisan': set(['Nablus','Jenin','Nasrah','Tabaria','Nasrah']),
#          'Nasrah': set(['Bisan','Jenin','Haifa','Akka', 'Tabaria']),
#          'Haifa': set(['Tulkarm','Jenin','Nasrah','Akka']),
#          'Jenin': set(['Bisan', 'Nasrah','Haifa','Tulkarm','Nablus']), 
#          'Nablus': set(['Bisan','Jenin','Tulkarm','Yaffa','Ramla','Ramallah','Jericho']),
#          'Yaffa' :set(['Tulkarm','Ramla','Nablus']),
#          'Ramla' :set(['Yaffa','Gaza','Hebron','Bethlehem','Jerusalem','Ramallah','Nablus']),
#          'Ramallah':set(['Nablus','Ramla','Jerusalem','Jericho']),
#          'Jericho': set(['Nablus','Ramallah','Jerusalem','Bethlehem']),
#          'Bethlehem': set(['Jericho','Jerusalem','Ramla','Hebron']),
#          'Hebron': set(['Bethlehem','Ramla','Gaza','Saba']),
#          'Gaza': set(['Ramla','Saba','Hebron']),
#          'Saba': set(['Hebron','Gaza']),
#          'Tulkarm':set(['Haifa','Yaffa','Nablus','Jenin']),
#          'Jerusalem':set(['Jericho','Ramallah','Ramla','Bethlehem'])   
#         }


 


# #Depth-first algorthm
# def dfs_paths(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         for next in graph[vertex] - set(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 stack.append((next, path + [next]))
#     print("this are results for dfs")            
#     print(path)
#     print(goal)
# list(dfs_paths(graph, 'Saffad', 'Nablus')) 


# #Bredth first algrothim
# def bfs_paths(graph, start1, goal1):
#     queue1 = [(start1, [start1])]
#     while queue1:
#         (vertex1, path1) = queue1.pop(0)
#         for next in graph[vertex1] - set(path1):
#             if next == goal1:
#                 yield path1 + [next]
#             else:
#                 queue1.append((next, path1 + [next]))
#     print("this is for bfs")
#     print(path1)
#     print(goal1)
# list(bfs_paths(graph, 'Saffad', 'Nablus')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]



# def greedy_path(graph , start1 , goal1):

#     done

