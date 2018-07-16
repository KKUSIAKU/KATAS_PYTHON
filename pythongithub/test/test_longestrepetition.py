#from src.longestrepetition import longestrepetition

from __future__ import absolute_import

import unittest

import sys
import os 
sys.path.append('C:\\Users\\Admin\\Documents\\PROGRAMMATION\\PYTHON\\codewars\\pythongithub')
print(sys.path)

#import  src.longestrepetition
# try:
#   from .. import src
# except Exception as e:
#   print(e)

import one

import mytest
import lib.longestrepetition as longestrepetition

class Test(unittest.TestCase):

  def test_function(self):
    print(mytest.cooltest())
    print(longestrepetition.longest_repetition(''))
    #print(' testing start')

    pass


if __name__ == "__main__":
  #replacenth.replace("testing nothing",0,'c','a')
  print(' ok ok ')
  unittest.main()
