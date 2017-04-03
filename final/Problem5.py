# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:38:24 2017

@author: Mitsakos
"""
class Person(object):
    def __init__(self, name):
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0        
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        stata = ["citizen", "legal_resident", "illegal_resident"]
        
        if status in stata:
            Person.__init__(self, name)
            self.status = status
        else: 
            raise ValueError
            
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
    
        
        
        
        
        
        
        
        
        
        
