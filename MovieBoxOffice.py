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
class BoxOffice:
    # Initializion function
    def __init__(self, w, n):
        self.n = n
        self.w = w
        self.queues = [[None for i in range(n)] for j in range(w)]
        self.starts = [0 for i in range(w)]
        self.ends = [0 for i in range(w)]
        self.open= [False for i in range(w)]
        self.open[0] = True
    # This function returns if a window is open by its id
    def isOpen(self,windowid):
        return self.open[windowid]
    #This function gets a window by its id
    def getWindow(self, windowid):
        if self.isOpen(windowid):
            return [x for x in self.queues[windowid] if x is not None] 
        else:
            return []
    # This function issues a single ticket across all open windows where atleast one person is present
    def giveTicket(self):
        ticketgiven=0
        for j in range(len(self.open)): 
            if(self.open[j]):
                queueWithNoNone = [x for x in self.queues[j] if x is not None]
                if (len(queueWithNoNone)!=0):
                    self.queues[j].remove(queueWithNoNone[0])
                    self.queues[j].append(None)
                    ticketgiven+=1   
        return ticketgiven
    # This is a recurring function which adds a person to the given queue index
    def recurr(self,index,personid):
        self.queues[index].pop(0)
        self.queues[index].append(personid)
        return index
    # This function gives the smallest Queue available in the given list 
    def smallestOpenQueue (self):
        count = sum(1 for i in self.queues[0] if i != None)
        smallestQueueIndex=0 
        for j in range(len(self.open)): 
            if (sum(1 for i in self.queues[j] if i != None) < count and self.open[j]):  
                count = sum(1 for i in self.queues[j] if i != None)
                smallestQueueIndex = j
        return smallestQueueIndex       
    # This function adds a person to the smallest queue available.
    def addPerson(self, personid):
        small = self.smallestOpenQueue()
        if (sum(1 for i in self.queues[small] if i != None)!=n):
            return self.recurr(small,personid)
        else:
            try:
                index_pos = self.open.index(False)
                self.open[index_pos] = True
                return self.recurr(index_pos,personid) 
            except ValueError:
                print("all queues are full")
                return -1             

if __name__ == '__main__':
    boxoffice = None
    inputs = open('inputPS1.txt','r')
    output = open('outputPS1.txt', 'w')
    STRING_CONCAT = "%s >> %s\n"
    for i in inputs:
        if "ticketSystem" in i:
            itype, w, n = i.split(':')
            w = int(w)
            n = int(n)
            boxoffice = BoxOffice(w,n)
        if 'isOpen' in i:
            itype , id = i.split(':')
            isBoxOfficeOpen = boxoffice.isOpen(int(id))
            output.write(STRING_CONCAT % (i, isBoxOfficeOpen))
        if 'getWindow' in i:
            itype , id = i.split(':')
            waiting_list = boxoffice.getWindow(int(id))
            output.write(STRING_CONCAT % (i, waiting_list))
        if 'addPerson' in i:
            itype , id = i.split(':')
            addperson = boxoffice.addPerson(int(id))
            if(addperson == -1):
                output.write("all queues are full")
            else:    
                output.write(STRING_CONCAT % (i, addperson))
        if 'giveTicket' in i:
            tickets = boxoffice.giveTicket()
            output.write(STRING_CONCAT % (i, tickets))
    print('Completed')
