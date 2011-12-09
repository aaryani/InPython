import inspect
import sys
import os
import functools
import numpy as np

np.set_printoptions(threshold='nan',linewidth='nan')


def name(item):
    " Return an item's name. "
    return item.__name__
    
def is_classmethod(instancemethod):
    " Determine if an instancemethod is a classmethod. "
    return instancemethod.im_self is not None
    
def is_class_private_name(name):
    " Determine if a name is a class private name. "
    # Exclude system defined names such as __init__, __add__ etc
    return name.startswith("__") and not name.endswith("__")
    
def method_name(method):
    """ Return a method's name.
    
    This function returns the name the method is accessed by from
    outside the class (i.e. it prefixes "private" methods appropriately).
    """
    mname = name(method)
    if is_class_private_name(mname):
        mname = "_%s%s" % (name(method.im_class), mname)
    return mname
    
def format_arg_value(arg_val):
    """ Return a string representing a (name, value) pair.
    
    >>> format_arg_value(('x', (1, 2, 3)))
    'x=(1, 2, 3)'
    """
    arg, val = arg_val
    return "%s=%r" % (arg, val)
    
def echo(mod, klass, fn, write=sys.stdout.write):
    """ Echo calls to a function.
    
    Returns a decorated version of the input function which "echoes" calls
    made to it by writing out the function's name and the arguments it was
    called with.
    """
    code = fn.func_code
    # all functions are identified by modulename.[classname.]functionname
    module_id = code.co_filename.rsplit('.',1)[0]
    class_id = module_id
    if klass is not None:
	class_id += ".%s" % klass.__name__
    func_id = "%s.%s" % (class_id, code.co_name)
    if not (func_id in functions_dict) and not('/metamodelling.' in func_id):
	# in addition we need their idification by modulename.linenumber
	lineno = code.co_firstlineno
	func_id_line = "%s.%s"  % (module_id, lineno)

	# store both function identification in 2 separate lists
	all_functions.append(str(func_id_line))
	functions_dict.append(func_id)

	# Unpack function's arg count, arg names, arg defaults
	argcount = code.co_argcount 
	argnames = list(code.co_varnames[:argcount])
	fn_defaults = fn.func_defaults or list()
	argdefs = dict(zip(argnames[-len(fn_defaults):], fn_defaults))

	# add linenumber of each function to proper class in classes_dict
	for i in range(0, len(classes_dict)):
	    if classes_dict[i][0] == class_id:
		classes_dict[i].append(lineno)

	#dynamic part starts here
	@functools.wraps(fn)
	def wrapped(*v, **k):
	    # observation from de called functions view
	    callee = func_id_line
	    column = all_functions.index(str(callee))
	    classes_ro = 0
	    functions_ro = 0
            # Collect function arguments by chaining together positional, defaulted, extra positional and keyword arguments.
            positional = map(format_arg_value, zip(argnames, v))
            defaulted = [format_arg_value((a, argdefs[a]))
                 for a in argnames[len(v):] if a not in k]
            nameless = map(repr, v[argcount:])
            keyword = map(format_arg_value, k.items())
            args = positional + defaulted + nameless + keyword

	    #identify caller
	    frame = inspect.currentframe()
	    caller_mod = frame.f_back.f_code.co_filename.rsplit('.', 1)[0]

	    caller_line = frame.f_back.f_code.co_firstlineno
    	    caller = '%s.%s' % (caller_mod, caller_line)
	    try:
		functions_ro = all_functions.index(str(caller))
		call_list[functions_ro][column] += 1
	    except:
		print ('ERROR: %s & %s ' % (caller, callee) )

	# update call_list: still same caller but different view (now we consider functions instead of classes)
            return fn(*v, **k)
	return wrapped
    
def echo_instancemethod(mod, klass, method, write=sys.stdout.write):
    """ Change an instancemethod so that calls to it are echoed.
    
    Replacing a classmethod is a little more tricky.
    See: http://www.python.org/doc/current/ref/types.html
    """
    mname = method.__name__
    never_echo = "__str__", "__repr__", # Avoid recursion printing method calls
    if mname in never_echo:
        pass
    elif is_classmethod(method):
        setattr(klass, mname, classmethod(echo(mod, klass, method.im_func, write)))
    else:
        setattr(klass, mname, echo(mod, klass, method, write))
    
def echo_class(mod, klass, write=sys.stdout.write):
    """ Echo calls to class methods and static functions
    """
    #collect all echoed classes in 2 lists
    class_id = '%s.%s' % (mod.__file__.rsplit('.', 1)[0], klass.__name__)
    all_classes.append(class_id)
    classes_dict.append([class_id])
    for _, method in inspect.getmembers(klass, inspect.ismethod):
	#due to not echoing twice
	if (method.__module__ == mod.__name__):
            echo_instancemethod(mod, klass, method, write)
    for _, fn in inspect.getmembers(klass, inspect.isfunction):
	#due to not echoing twice
	if (fn.__module__ == mod.__name__):
            setattr(klass, name(fn), staticmethod(echo(mod, klass, fn, write)))
    
def echo_module(mod, write=sys.stdout.write):
    """ Echo calls to functions and methods in a module.
    """


    for fname, fn in inspect.getmembers(mod, inspect.isfunction):
	#due to not echoing twice
	if (fn.__module__ == mod.__name__):
        	setattr(mod, fname, echo(mod, None, fn, write))
    for _, klass in inspect.getmembers(mod, inspect.isclass):
	#due to not echoing twice
	if (klass.__module__ == mod.__name__):
        	echo_class(mod, klass, write)




# initialise lists for all views: classes and functions before annotating
all_classes = []
classes_dict = []

all_functions = []
functions_dict = []

#instrument functions by echoing all modules
from tardis import echo_all
#from tardis.DEF_CALL.DEF_CALL_check import echoing
path_name = 'tardis/DEF_CALL/OutputFiles/'
#from tardis.tardis_portal.tests.meta_check.DEF_CALL import echoing

call_f_name = path_name + 'call.txt'
def_f_name = path_name + 'def.txt'
dc_f_name = path_name + 'dc.txt'
call_d_name = path_name + 'call.dat'
def_d_name = path_name + 'def.dat'
dc_d_name = path_name + 'dc.dat'


func_length = len(all_functions)
class_length = len(all_classes)
print ('# Functions: %s' % len(all_functions))
print ('# Classes: %s' % len(all_classes))

# initialise arrays for every considered relationship between callers and callees	
call_list = np.array([[0 for col in range(func_length)] for row in range(func_length)])
def_list = np.array([[0 for col in range(func_length)] for row in range(class_length)]) 
dc_list = np.array([[0 for col in range(func_length)] for row in range(class_length)])


# start the program
# everything you need to measure should stand here    
#e.g.: from tardis.tardis_portal.tests.meta_check.DEF_CALL import prog


from django.core.management import ManagementUtility
utility = ManagementUtility(None)
utility.execute()
#from tardis.DEF_CALL.DEF_CALL_check import prog


#compute def_list based on the list functions_dict and all_classes
for i in range(0, len(functions_dict)):
    fc = functions_dict[i].rsplit('.', 1)[0]
    for j in range(0, len(all_classes)):
    	if fc == all_classes[j]:
	    def_list[j][i] = 1


#compute def_call matrice (def*call)
dc_list = np.dot(def_list, call_list)

call_f = file(call_f_name, 'w')
def_f = file(def_f_name, 'w')
dc_f = file(dc_f_name, 'w')
call_d = file(call_d_name, 'w')
def_d = file(def_d_name, 'w')
dc_d = file(dc_d_name, 'w')


print ('\n CALL relations:')
for i in range(0,len(call_list)):
    call_f.writelines("%s \n" % call_list[i])
    call_d.writelines("%s %s \n" % (i, call_list[i].sum()))

print ('\n DEF relations:')
for i in range(0,len(def_list)):
    def_f.writelines("%s \n" % def_list[i])
    def_d.writelines("%s %s \n" % (i, def_list[i].sum()))

print ('\n DEF_CALL:')
for i in range(0,len(dc_list)):
    dc_f.writelines("%s \n" % dc_list[i])
    dc_d.writelines("%s %s \n" % (i, dc_list[i].sum()))

#If you need names of classes and functions
#print ('\n CLASSES_LIST')
#for i in range(0, len(classes_dict)):
#    print classes_dict[i]
#print ('\n FUNCTIONS_LIST')
#for line, name in zip(all_functions,functions_dict):
#    print ('%s: %s' % (line, name))

call_f.close()
def_f.close()
dc_f.close()
call_d.close()
def_d.close()
dc_d.close()
