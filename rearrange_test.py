#!/Users/clifforddelacruz/opt/Anaconda3/bin/python3
from rearrange import rearrange_name
import unittest
#create a class to use unittest.TestCase
class TestRearrange(unittest.TestCase):
  #this function is to test if value will be same once processed
  def test_basic(self):
    testcase="Lovelace, Ada"
    expected="Ada Lovelace"
    #compare the testcase and expected
    self.assertEqual(rearrange_name(testcase),expected)

  #this function is to test if the entry is blank
  def test_empty(self):
    testcase=""
    expected=""
    #compare the testcase and expected
    self.assertEqual(rearrange_name(testcase),expected)

  #this function is to test if name will be rearrange correctly if there is middle initial
  def test_double_name(self):
    testcase="Hooper, Grace M."
    expected="Grace M. Hooper"
    #compare the testcase and expected
    self.assertEqual(rearrange_name(testcase),expected)

  #this is to test if name input is only one name
  def test_one_name(self):
    testcase="Voltaire"
    expected="Voltaire"
    #compare the testcase and expected
    self.assertEqual(rearrange_name(testcase),expected)

#run in main
unittest.main()