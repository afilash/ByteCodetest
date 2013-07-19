'''
Created on 16-Jul-2013
@author: AppleCart
'''

import sys
sys.dont_write_bytecode = True
from Helperclass import ElementPackage
from Helperclass import MemberPackage


def caller():
    #===========================================================================
    # Failed method , this is not correct
    #===========================================================================
    
    #---------------------------------------------------------- primary instance
    elm = ElementPackage()          
    #------------------------------------------- setting instance variable to 78
    elm.setElements(78)
    #--------------------------------------- getting back that instance variable
    print "elm.get   :" , elm.getElements()
    

    #----------------------------------------------------------- another instace
    elm_2 = ElementPackage()
    #-------------------------------------- this is just a local variable , how?
    elm_2.Elements = 23
    #------------------------------ by printing this we get two different things
    print "elm_2.Ele :" , elm_2.Elements
    print "elm_2.get :" , elm_2.getElements()
    #-------------------------------------- but this will retrive our orginal 78
    print "elm.get   :" , elm.getElements()                 
    #--------------------- printing this will give error, we ill not get 78 back
    #print "elm.Ele   :" , elm.Elements
    
    
    
    #===========================================================================
    # Correct method
    #===========================================================================
    mem1 = MemberPackage()
    mem1.member = 22
    print "mem1.member :" ,mem1.member
    
    mem2 = MemberPackage()
    mem2.member = 54
    print "mem2.member :" ,mem2.member
    
    print "mem1.member :" ,mem1.member
    
    #===========================================================================
    # Finished.
    #===========================================================================

if __name__ == '__main__':
    caller()
