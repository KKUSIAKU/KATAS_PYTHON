import unittest
import replacenth


class ReplaceTest(unittest.TestCase):
  
  def test_replace(self):
    self.assertEqual(replacenth.replace("Vader said: No, I am your father!",2,"a","o"),"Vader soid: No, I am your fother!")


if __name__ == "__main__":
  #replacenth.replace("testing nothing",0,'c','a')
  unittest.main()
  