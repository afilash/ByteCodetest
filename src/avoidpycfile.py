'''
Created on 16-Jul-2013
@author: AppleCart
'''

import sys
sys.dont_write_bytecode = True

from Helperclass import ElementPackage


def caller():
    elm = ElementPackage()
    elm.setElements(78)
    print elm.Elements()
    

if __name__ == '__main__':
    caller()
