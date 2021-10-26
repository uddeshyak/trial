#1st see student.py...then class and objects.....then chef..then chinesechef..


#INHERITANCE:-
from chef import chef

class chinesechef(chef): #this chinese chef can do whatever a normal chef can do..so we inherited normal chef talents..
    def make_fried_rice(self): #this is extra talent..
        print("the chef make fried rice")