#********************************************************************************************
#This exercise is to improve the knowledge of classes and inheritance in the python language
#********************************************************************************************

"""We will define some classes, using inheritance and composition.
1. Classes: 
- Base Class: Car
- Brands Classes: Ford, Honda, Hyundai, Volkswagen, Nissan, Toyota, Tesla
- Models Classes: 
                Ford: Ranger, Maverick, Bronco, Territory 
                Honda: Hrv, City, Civic
                Hyundai: Creta, HB20, Azera
                Volkswagen: Gol, Voyage, Polo, Jetta
                Nissa: 
                Toyota:
                Tesla: 
"""



# class Animal:
#     name = ""
#     category = ""
    
#     def __init__(self, name):
#         self.name = name
    
#     def set_category(self, category):
#         self.category = category



# class Zoo:
#     def __init__(self):
#         self.current_animals = {}
    
#     def add_animal(self, animal):
#         self.current_animals[animal.name] = animal.category
    
#     def total_of_category(self, category):
#         result = 0
#         for a in self.current_animals.values():
#             if a == category:
#                 result += 1
#         return result

# zoo = Zoo()




# #Begin Portion 1#
# import random

# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}

#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random()*10+1
#         # Add the connection to the dictionary with the calculated load
#         self.connections[connection_id] = connection_load

#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary
#         del self.connections[connection_id]

#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         # Add up the load for each of the connections
#         for t in self.connections.values():
#             total += t
        
#         return total

#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())
    
# #End Portion 1#