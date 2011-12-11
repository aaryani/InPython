#import traceback

import sys
sys.path[0:0] = [
    '/home/nelli/CoreTardis/eggs/nose-1.1.2-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/coverage-3.4-py2.6-linux-i686.egg',
    '/home/nelli/CoreTardis/eggs/django_nose-0.1.3-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/nosexcover-1.0.7-py2.6.egg',
    '/home/nelli/CoreTardis',
    '/home/nelli/CoreTardis/eggs/python_ldap-2.4.3-py2.6-linux-i686.egg',
    '/home/nelli/CoreTardis/eggs/python_magic-0.4.0dev-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/psycopg2-2.4.2-py2.6-linux-i686.egg',
    '/home/nelli/CoreTardis/eggs/python_memcached-1.47-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/pysolr-2.1.0_beta-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/django_haystack-1.2.5-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/djangorecipe-0.99-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/Django-1.3-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/zc.recipe.egg-1.3.2-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/zc.buildout-1.5.2-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/setuptools-0.6c12dev_r88846-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/South-0.7.3-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/django_form_utils-0.2.0-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/django_extensions-0.6-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/django_registration-0.7-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/elementtree-1.2.7_20070827_preview-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/feedparser-5.0.1-py2.6.egg',
    '/home/nelli/CoreTardis/eggs/lxml-2.2.7-py2.6-linux-i686.egg',
    '/home/nelli/CoreTardis/parts/django',
    '/home/nelli/CoreTardis',
    ]
import tardis.counting_t
from tardis.counting_t import B


class class1:
    def __init__(self):
        self.description = 'class #1'
    def show(self):
	for i in range(5):  
	    c = class5()
	    c.show()  
	print self.description

class class5:
    def __init__(self):
        self.description = 'class #5'
    def show(self):
        print self.description
	B.function_b()	
