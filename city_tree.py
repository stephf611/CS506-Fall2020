#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:00:22 2020

@author: stephanieforbes
"""

def tree():
   print "T" , 

def forest(x,y):
    """ input number of rows and columns of trees in the forest"""
    for a in range (0, y):
        for b in range (0,x):
            tree()
        print "\n"
        