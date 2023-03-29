#!/usr/bin/python3

""" Defines class Node"""


class Node:
    """ Instantiating..."""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    """ Method that retrieves data """
    @property
    def data(self):
        return self.__data

    """ Method that sets the data attribute """
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    """ Retrieving Next_node"""
    @property
    def next_node(self):
        return self.__next_node

    """ Method that sets the next_node attribute """
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" Defines a SinglyLinkedClass"""


class SinglyLinkedList:
    """ Instantiating... """
    def __init__(self):
        self.head = None

    """ Method the prints the objects """
    def __str__(self):
        all_node = ""
        pos = self.head
        while pos:
            all_node += str(pos.data) + "\n"
            pos = pos.next_node
        return all_node[:-1]

    """ Method that inserts node into the list"""
    def sorted_insert(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
