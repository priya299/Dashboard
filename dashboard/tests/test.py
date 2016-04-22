import unittest
from createjson import MboxParser

class test_mbox_mails(unittest.TestCase):

	def setUp(self):
		self.mparser = MboxParser()

	def test(self):
		mbox = self.mparser.create_json('xen-devel-2016-03', 'testoutput.json')


	def tearDown(self):
		del self.mparser

if __name__ == '__main__':
	unittest.main()


