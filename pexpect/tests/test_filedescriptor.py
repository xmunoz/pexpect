#!/usr/bin/env python
import pexpect
import unittest
import PexpectTestCase
import sys
import os

class ExpectTestCase(PexpectTestCase.PexpectTestCase):
    def test_fd (self):
	fd = os.open ('TESTDATA.txt', os.O_RDONLY)
	s = pexpect.spawn (fd)
	s.expect ('This is the end of test data:')
	s.expect (pexpect.EOF)
	assert s.before == ' END\n'

    def test_fd_isalive (self):
	fd = os.open ('TESTDATA.txt', os.O_RDONLY)
	s = pexpect.spawn (fd)
	assert s.isalive()
	os.close (fd)
	assert not s.isalive()

    def test_fd_isatty (self):
	fd = os.open ('TESTDATA.txt', os.O_RDONLY)
	s = pexpect.spawn (fd)
	assert not s.isatty()
	os.close(fd)

    def test_close_does_not_close_fd (self):
	"""Calling close() on a pexpect.spawn object should not
		close the underlying file descriptor.
	"""
	fd = os.open ('TESTDATA.txt', os.O_RDONLY)
	s = pexpect.spawn (fd)
	try:
		s.close()
		self.fail('Expected an Exception.')
	except pexpect.ExceptionPexpect, e:
		pass

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(ExpectTestCase, 'test')

#fout = open('delete_me_1','wb')
#fout.write(the_old_way)
#fout.close
#fout = open('delete_me_2', 'wb')
#fout.write(the_new_way)
#fout.close
