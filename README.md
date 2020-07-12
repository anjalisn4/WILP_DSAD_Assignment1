# WILP_DSAD_Assignment1
Assignment 1 – PS1 - [Box Office]
## 1. Problem Statement
A movie theatre manager needs your help to implement a ticketing system for the box office. He has a list of specific asks in how the ticketing system should work. Below are the asks:

 - There are only ‘w’ number of box office windows in the theatre. Each window can have at max ‘n’ number of people waiting in line.
 - To start with, only one window is opened. If the number of people waiting in line in that window exceeds n, then the next window is opened and people can join the line in that window. Likewise, if both the first and second windows have n number of people waiting in each queue, then a third window is opened. This can go on until the maximum number of windows w is reached. Let us assume that once a window is opened it never closes. A new window is only opened if all open windows are full.
 - Each person can buy only one ticket. So, the system should not allot more than one ticket per person. Let us assume that the system issues one ticket each across all open windows. When a ticket is issued, the count of the number of people in each open queue is reduced by 1.
 - When a new person has to join the queue, the system has to prompt him to join a queue such that they are issued a ticket as fast as possible. The system prompts the person based on these factors:
   - First it looks for an open window with the least number of people and prompts that window number. If more than one window has the least number of people, then the system can prompt the person to join the first window (smaller window Id) it encounters with the least number of people.
   - If the queues of all open windows are full and a new window can be opened, then the new person is prompted to join the new queue for the new box office window.
   - If all queues for all windows are full, a corresponding message is displayed. That person need not be considered in the next iteration.
 - After a queue is prompted to a person, the person or system cannot change the queue.

 ## How to run the program?
 Open terminal in the root folder and run the below code
 ```
 py ./MovieBoxOffice.py
 ```
The results for the given inputPS1.txt will be available in outputPS1.txt file.

## Files in this repository

-  inputPS1.txt file used for testing
-  promptsPS1.txt file used for testing
-  outputPS1.txt file generated while testing
-  analysisPS1.txt file with answers on the running times (ask number 2)
 
