# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:27:40 2017

@author: Mitsakos
"""
# base classes
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)

# my classes

class ArrogantProfessor1(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):         
        return 'It is obvious that ' + Person.say(self, stuff)
    
class ArrogantProfessor2(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that I believe that ' + Person.say(self, stuff)
    def lecture(self, stuff):         
        return 'It is obvious that I believe that ' + Person.say(self, stuff)

class Professor1(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)