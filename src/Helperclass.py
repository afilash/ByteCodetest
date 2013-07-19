'''
Created on 16-Jul-2013
@author: AppleCart
'''

class ElementPackage():    
    _Elements = None
    
    def __init__(self ):
        self._Elements = None
    
    def getElements(self):
        return self._Elements
        
    def setElements(self, elementid):
        self._Elements=elementid
