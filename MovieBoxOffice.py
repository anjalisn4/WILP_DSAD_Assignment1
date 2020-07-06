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

    def isOpen(self,windowid):
        if i is self.open[windowid]:
            return True
        return False
    
    def getWindow(self, windowid):
        queue = self.queues[windowid]
        if len(queue)>0:
            return queue
        else:
            return queue

    def addPerson(self, personid):
        for open in self.open:
            if open:
                index = self.open.index(open)
                queue = self.queues[index]
                if None not in queue and len(queue) == self.n:
                    return "all queues are full"
                if None in queue:
                    insert_index = queue.index(None)
                    self.queues[index][insert_index] = personid
                    return index

    def giveTicket(self):
        ticketgiven=0
        for open in self.open:
            if open:
                index_open = self.open.index(open)
                queue = self.queues[index_open]
                for i in queue:
                    if i is not None:
                        adding_index = queue.index(i)
                        self.queues[index_open][adding_index]= None
                        ticketgiven += 1
        return ticketgiven
                

if __name__ == '__main__':
    boxoffice = None
    inputs = open('inputPS1.txt','r')
    output = open('outputPS1.txt', 'w')
    for i in inputs:
        if "ticketSystem" in i:
            itype, w, n = i.split(':')
            w = int(w)
            n = int(n)
            boxoffice = MovieBoxOffice(w,n)
        if 'isOpen:1' in i:
            itype , id = i.split(':')
            if boxoffice.isOpen(int(id)):
                output.write("isOpen:1 >> True\n")
            else:
                output.write("isOpen:1 >> False\n")
        if 'getWindow' in i:
            itype , id = i.split(':')
            waiting_list = boxoffice.getWindow(int(id))
            output.write("getWindow:1 >> "+str(waiting_list)+"\n")
        if 'addPerson:' in i:
            itype , id = i.split(':')
            addperson = boxoffice.addPerson(int(id))
            output.write("addPerson:"+str(id)+">>"+str(addperson)+"\n")
        if 'giveTicket:' in i:
            tickets = boxoffice.giveTicket()
            output.write("giveTicket: >>"+str(tickets)+"\n")
    print('Completed')
