# -*- coding: utf-8 -*-
"""
Created on Sat July 11 2020
@author: DSAD Group 37
@contribution:
    Team Member     Roll Number
    ===========================
    Amit Kumar     2019HC04174
    Pranesh P	2019HC04175
    Anjali Sunder Naik	2019HC04178
"""
class BoxOffice:
    def __init__(self, w, n):
        self.n = n
        self.w = w
        self.queues = [[None for i in range(n)] for j in range(w)]
        self.starts = [-1 for i in range(w)]
        self.ends = [-1 for i in range(w)]
        self.open = [False for i in range(w)]
        self.open[0] = True
        self.currlen =[0 for i in range(w)]

    # returns True if the box office window is open and False if it is yet to be opened (closed).
    def isOpen(self, windowid):
        return self.open[windowid]  

    # returns the queue (number of people waiting) in front of the window.
    def getWindow(self, windowid):
        if self.isOpen(windowid):
            return [x for x in self.queues[windowid] if x is not None]
        else:
            return [] 

    def size(self, index):
        return self.currlen[index]

    # returns index of smallest open queue 
    def getSmallestQueueIndex(self):
        qsizes = []
        for j in range(w):
            if self.isOpen(j):
                qsizes.append(self.size(j))
        return qsizes.index(min(qsizes))  

    # This is a recurring function which adds a person to the queue
    def recurr(self, size, index, personid):
        if (size == (self.n)):
            if(index != (self.w-1)):
                new_index = index+1
                self.open[new_index] = True
                size_new = self.size(new_index)
                return self.recurr(size_new,new_index,personid)
            else:
                return -1    
        else:        
            self.enQueue(personid,index)
            return index  

    # Insert an element into the circular queue
    def enQueue(self, personid,index):
        tail = (self.ends[index] + 1) % self.n
        self.queues[index][tail] = personid
        self.ends[index] = tail
        self.currlen[index] += 1
        if self.currlen[index] == 1:
            self.starts[index] = 0

    # Delete an element from the circular queue
    def deQueue(self,index):
        self.queues[index][self.starts[index]]=None
        self.starts[index] = (self.starts[index] + 1) % self.n
        self.currlen[index] -= 1
        if (self.currlen[index] == 0):
            self.starts[index] = -1
            self.ends[index] = -1

    # Add a person to the smallest open queue
    def addPerson(self, personid):
        get_smallest_queue_index = self.getSmallestQueueIndex()
        smallest_queue = self.queues[get_smallest_queue_index]
        size_of_smalles_queue = self.size(get_smallest_queue_index)
        if (size_of_smalles_queue == (self.n)):
            return self.recurr(size_of_smalles_queue,get_smallest_queue_index,personid)
        else:
            self.enQueue(personid,get_smallest_queue_index)
            return get_smallest_queue_index   

    # This function is called to issue a ticket at every open box office window with a queue of at least one person
    def giveTicket(self):
        ticketgiven = 0
        for j in range(w):
            if(self.open[j] and self.currlen[j]!=0):
                self.deQueue(j)
                ticketgiven += 1
        return ticketgiven        

if __name__ == '__main__':
    boxoffice = None
    inputs = open('inputPS1.txt', 'r')
    output = open('outputPS1.txt', 'w')
    STRING_CONCAT = "%s >> %s\n"
    for i in inputs:
        if "ticketSystem" in i:
            itype, w, n = i.split(':')
            w = int(w)
            n = int(n)
            boxoffice = BoxOffice(w, n)
        if 'isOpen' in i:
            itype, id = i.split(':')
            isBoxOfficeOpen = boxoffice.isOpen(int(id))
            output.write(STRING_CONCAT % (i, isBoxOfficeOpen))
        if 'getWindow' in i:
            itype, id = i.split(':')
            waiting_list = boxoffice.getWindow(int(id))
            output.write(STRING_CONCAT % (i, waiting_list))
        if 'addPerson' in i:
            ADD_PERSON_STRING_CONCAT="%s >> w%s\n"
            itype, id = i.split(':')
            addperson = boxoffice.addPerson(int(id))
            if(addperson ==-1):
                output.write(STRING_CONCAT % (i, "all queues are full"))   
            else:                 
                output.write(ADD_PERSON_STRING_CONCAT % (i, addperson))            
        if 'giveTicket' in i:
            tickets = boxoffice.giveTicket()
            output.write(STRING_CONCAT % (i, tickets))
    print('Completed')
