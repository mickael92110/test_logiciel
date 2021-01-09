import unittest
from quick_tools import verify_room_name
from quick_tools import verify_room_type
from quick_tools import verify_password_length
from quick_tools import verify_password_digit
from quick_tools import verify_password_letter
from quick_tools import verify_password_char_spec
from quick_tools import verify_password_general

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
		self.assertFalse(verify_room_type('publi c'))
		self.assertFalse(verify_room_type('PUbLIC'))
		self.assertFalse(verify_room_type('public '))


		self.assertTrue(verify_room_type('private'))
		self.assertTrue(verify_room_type('public'))
		self.assertTrue(verify_room_type('PRIVATE'))
		self.assertTrue(verify_room_type('PUBLIC'))




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


	def test_verify_password_char_spec(self):

		self.assertFalse(verify_password_char_spec('abcdefghi'))
		self.assertFalse(verify_password_char_spec('1234567890'))
		self.assertFalse(verify_password_char_spec('abc123def456'))

		self.assertTrue(verify_password_char_spec('abc-def-ghij'))
		self.assertTrue(verify_password_char_spec('abc=abcdef!=fed'))
		self.assertTrue(verify_password_char_spec('%$*ab.c1234'))


	def test_verify_password_general(self):

		self.assertFalse(verify_password_general('abcdefghi'))
		self.assertFalse(verify_password_general('1234567890'))
		self.assertFalse(verify_password_general('abc123def456'))
		self.assertFalse(verify_password_general('.:;123&§!456'))
		self.assertFalse(verify_password_general('              '))


		self.assertTrue(verify_password_general('abc-def-ghij1'))
		self.assertTrue(verify_password_general('abc=ab9cdef!=fed'))
		self.assertTrue(verify_password_general('%$*ab.c1234'))
		self.assertTrue(verify_password_general('534SEFSF,;::,'))
