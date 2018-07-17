
import sys



import unittest
import script.locationrgx as rgx


class Test_locationrgx(unittest.TestCase):
  def test_simpleExpression(self):
    self.assertEqual(rgx.location('La tour Eiffel sur Paris.'),'Paris')
    self.assertEqual(rgx.location('La tour Eiffel sur paris.'),'paris')

    # self.assertEqual(rgx.location('La tour Eiffel à Paris.'),'Paris')
    # self.assertEqual(rgx.location('La tour Eiffel à Paris.'),'paris')

    # self.assertEqual(rgx.location('La tour Eiffel dans Paris.'),'Paris')
    # self.assertEqual(rgx.location('La tour Eiffel dans paris.'),'paris')





if __name__ == "__main__":
  print(" Testing loncationrgx function start ")
  unittest.main()
  print(" Testing loncationrgx function end")