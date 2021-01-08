import unittest
from quick_tools import verify_room_name
from quick_tools import verify_room_type
from quick_tools import verify_password_length
from quick_tools import verify_password_digit
from quick_tools import verify_password_letter



import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verify_room_name(self):

		self.assertFalse(verify_room_name('whatever')) # Doesn't start with ROOM_
		self.assertFalse(verify_room_name('ROOM_')) # starts with ROOM_ but isn't long enough

		# kindly stolen and adapted from : https://pynative.com/python-generate-random-string/
		random_str_len = random.randint(3,20)
		correct_room = 'ROOM_'
		correct_room += ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))

		self.assertTrue(verify_room_name(correct_room))

	def test_verify_room_type(self):

		self.assertFalse(verify_room_type('chat'))
		self.assertTrue(verify_room_type('private'))

		self.assertFalse(verify_room_type('publi c'))
		self.assertTrue(verify_room_type('public'))

		self.assertFalse(verify_room_type('PUBLIC'))
		self.assertFalse(verify_room_type('public '))

	def test_verify_password_length(self):

		self.assertFalse(verify_password_length('un'))
		self.assertTrue(verify_password_length('testtest1'))

		self.assertFalse(verify_password_length('publi c'))
		self.assertTrue(verify_password_length('abc12345'))

		self.assertFalse(verify_password_length('1234567'))
		self.assertFalse(verify_password_length('public '))

	def test_verify_password_digit(self):

		self.assertFalse(verify_password_digit('abcdefgh'))
		self.assertFalse(verify_password_digit('abcdefgh_-'))
		self.assertFalse(verify_password_digit('abcd efgh'))

		self.assertTrue(verify_password_digit('abcdefg1'))
		self.assertTrue(verify_password_digit('abc9defg'))
		self.assertTrue(verify_password_digit('111111111a'))


	def test_verify_password_letter(self):

		self.assertFalse(verify_password_letter('12352355'))
		self.assertFalse(verify_password_letter('&-(§-!+_)-'))
		self.assertFalse(verify_password_letter('     12£^`$*'))

		self.assertTrue(verify_password_letter('abcabc1234'))
		self.assertTrue(verify_password_letter('1a2b3c45fs'))
		self.assertTrue(verify_password_letter('azeù=+:124(4)'))
