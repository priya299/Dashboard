import unittest
from mboxparser import MboxParser

class test_mbox_mails(unittest.TestCase):

	def setUp(self):
		self.mparser = MboxParser()

	def test(self):
		mbox = self.mparser.mboxparser('xen-devel-2016-03', 'testoutput.json')


	def tearDown(self):
		del self.mparser

if __name__ == '__main__':
	unittest.main()


