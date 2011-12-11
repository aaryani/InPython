from django.test import TestCase
import sys

class Def_test(TestCase):
    def setUp(self):
	import numpy as np
        from tempfile import mkdtemp
	from os import path, mkdir

	call_m = np.array([[0 for col in range(14)] for row in range(14)])
	def_m = np.array([[0 for col in range(14)] for row in range(6)])
	dc_m = np.array([[0 for col in range(14)] for row in range(6)])
	call_m[1][2] = 5
	call_m[1][3] = 5
	call_m[3][8] = 5
	call_m[9][12] = 1	
	def_m[0][0] = 1
	def_m[0][1] = 1
	def_m[1][2] = 1
	def_m[1][3] = 1
	def_m[2][4] = 1
	def_m[2][5] = 1
	def_m[3][6] = 1
	def_m[3][7] = 1
	def_m[4][9] = 1
	def_m[4][10] = 1
	def_m[4][11] = 1
	def_m[5][12] = 1
	def_m[5][13] = 1
	dc_m[0][2] = 5
	dc_m[0][3] = 5
	dc_m[1][8] = 5
	dc_m[4][12] = 1

	self.test_dir = path.abspath(path.join(path.dirname(__file__), '../')).replace('\\', '/')
	self.test_dir += '/DEF_CALL/OutputFiles/new/'
	mkdir(self.test_dir)
        self.call_r_f = open(path.join(self.test_dir, 'call_right.txt'), 'w')
        self.def_r_f = open(path.join(self.test_dir, 'def_right.txt'), 'w')
        self.dc_r_f = open(path.join(self.test_dir, 'dc_right.txt'), 'w')
	for i in range(0,len(call_m)):
	    self.call_r_f.writelines("%s \n" % call_m[i])
	for i in range(0,len(def_m)):
	    self.def_r_f.writelines("%s \n" % def_m[i])
	for i in range(0,len(dc_m)):
	    self.dc_r_f.writelines("%s \n" % dc_m[i])
        self.call_r_f.close()
        self.def_r_f.close()
        self.dc_r_f.close()
        self.call_r_f = open(path.join(self.test_dir, 'call_right.txt'), 'r')
        self.def_r_f = open(path.join(self.test_dir, 'def_right.txt'), 'r')
        self.dc_r_f = open(path.join(self.test_dir, 'dc_right.txt'), 'r')

    def tearDown(self):
	import os
        from shutil import rmtree

        self.call_r_f.close()
        self.def_r_f.close()
        self.dc_r_f.close()
	
	os.remove(os.path.join(self.test_dir, 'call_right.txt'))
        rmtree(self.test_dir)

    def test_def(self):
	from tardis.DEF_CALL import metamodelling
	from os import path	
	call_m_f = file('tardis/DEF_CALL/OutputFiles/call.txt')
	def_m_f = file('tardis/DEF_CALL/OutputFiles/def.txt')
	dc_m_f = file('tardis/DEF_CALL/OutputFiles/dc.txt')
	call_m = call_m_f.read()
	def_m = def_m_f.read()
	dc_m = dc_m_f.read()
	call_r = self.call_r_f.read()
	def_r = self.def_r_f.read()
	dc_r = self.dc_r_f.read()
	self.assertEquals(call_r, call_m )
	self.assertEquals(def_r, def_m)
	self.assertEquals(dc_r, dc_m)
