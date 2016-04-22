import unittest
from createjson import MboxParser

class test_mbox_mails(unittest.TestCase):

	def setUp(self):
		ob=MboxParser()
		a=ob.getmbox('test_mbox_file')
		print(a)


if __name__ == '__main__':
	unittest.main()


