# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:06:31 2019
@author: DSAD Group 37
@contribution:
    Team Member     Roll Number
    ===========================
    Amit Kumar     2019HC04174
    Pranesh P	2019HC04175
    Anjali Sunder Naik	2019HC04178
"""
"""
w: Number of box offices --> 3
n : max length of each queue --> 5
"""
class MovieBoxOffice:
    def __init__(self, w, n):
            self.n = n
            self.w = w
            self.queues = [[None for i in range(n)] for j in range(w)]
            self.starts = [0 for i in range(w)]
            self.ends = [0 for i in range(w)]
            self.open= [False for i in range(w)]
            self.open[0] = True
   def isOpen (self, windowId):  
