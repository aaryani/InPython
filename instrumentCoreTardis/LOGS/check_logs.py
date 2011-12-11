from django.test import TestCase
import sys

class Def_test(TestCase):
    def setUp(self):
        from tempfile import mkdtemp
	from os import path, mkdir

	self.test_dir = path.abspath(path.join(path.dirname(__file__), '../')).replace('\\', '/')


	logs_r = []
	logs_r.append(' start')
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/mod1/__init__.class1.__init__' % self.test_dir)
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/mod1/__init__.class1.show' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.show' % self.test_dir)
	logs_r.append('+++ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.show' % self.test_dir)
	logs_r.append('+++ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.show' % self.test_dir)
	logs_r.append('+++ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.show' % self.test_dir)
	logs_r.append('+++ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/mod1/__init__.class5.show' % self.test_dir)
	logs_r.append('+++ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/B.function_b' % self.test_dir)
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/Private_mod.Bar.__init__' % self.test_dir)
	logs_r.append('++ %s/counting_t/Private_mod.Foo.__init__' % self.test_dir)
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/Private_mod.Bar.foo' % self.test_dir)
	logs_r.append(' start')
	logs_r.append('+ %s/counting_t/Private_mod.Bar.bar' % self.test_dir)

	self.test_dir += '/LOGS/OutputFiles/1/'
	mkdir(self.test_dir)
        self.logs_r_f = open(path.join(self.test_dir, 'logs_right.txt'), 'w')
	for i in range(0,len(logs_r)):
	    self.logs_r_f.writelines("%s \n" % logs_r[i])
        self.logs_r_f.close()
        self.logs_r_f = open(path.join(self.test_dir, 'logs_right.txt'), 'r')
    def tearDown(self):
	import os
        from shutil import rmtree

        self.logs_r_f.close()	
	os.remove(os.path.join(self.test_dir, 'logs_right.txt'))
        rmtree(self.test_dir)

    def test_def(self):
	from tardis.LOGS import metamodelling
	from os import path	
	logs_f = file('tardis/LOGS/OutputFiles/logs.txt')
	logs = logs_f.read()
	logs_r = self.logs_r_f.read()
	self.assertEquals(logs_r, logs)
