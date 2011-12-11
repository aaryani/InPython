import inspect
import sys
import os
import functools
import logging

logger = logging.getLogger('logs')
hdlr = logging.FileHandler('tardis/LOGS/OutputFiles/log.txt')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


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
    code = fn.__code__
    # all functions are identified by modulename.[classname.]functionname
    module_id = code.co_filename.rsplit('.',1)[0]
    class_id = module_id
    if klass is not None:
	class_id += ".%s" % klass.__name__
    func_id = "%s.%s" % (class_id, code.co_name)

    if not (func_id in functions_dict) and not('/metamodelling.' in func_id) and (fn.__module__ == mod.__name__):
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

    	#dynamic part starts here
    	@functools.wraps(fn)
    	def wrapped(*v, **k):
		callee = func_id

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
		caller_found = False
		callee_appended = False
		callee_string = ''
		test_1 = caller_mod
		try:
			starting_module_1 = caller_mod.rsplit('/', 1)[1]
		except:
			starting_module_1 = ''
		try:
			starting_module_2 = caller_mod.rsplit('.', 1)[1]
		except:
			starting_module_2 = ''
		#in case of an un-annotated function called this functin -> determine which was the last annotated function		
		while not caller_found:
			if 'unittest' in caller_mod:
				caller_found = True
				callee_appended = True				
			elif (starting_module_1.startswith('test') and not (starting_module_1 == 'testcases')) or (starting_module_2.startswith('test') and not (starting_module_2 == 'testcases')):
				logger.info(' ')
				log_list.append(' ')
				logger.info(' %s %s' % (caller_mod, caller_line))
				log_list.append(' %s %s' % (caller_mod, caller_line))
				logger.info(' start')
				log_list.append(' start')
				callee_string = callee_string + '+ %s' % func_id
				logger.info(callee_string)
				log_list.append(callee_string)
				callee_appended = True
				caller_found = True
			elif caller in all_functions:
				column = all_functions.index(caller)
				caller = functions_dict[column]
				caller_found = True
			else :
				frame = frame.f_back
				caller_mod = frame.f_back.f_code.co_filename.rsplit('.', 1)[0]
				caller_line = frame.f_back.f_code.co_firstlineno
				caller = '%s.%s' % (caller_mod, caller_line)
				callee_string = callee_string + '-'
				try:
					starting_module_1 = caller_mod.rsplit('/', 1)[1]
				except:
					starting_module_1 = ''
				try:
					starting_module_2 = caller_mod.rsplit('.', 1)[1]
				except:
					starting_module_2 = ''
		# update log_list:
		length = len(log_list) - 1
		while not callee_appended:
	    	    if caller == log_list[length].rsplit(' ', 1)[1]:
			callee_string = callee_string + '%s+ %s' % (log_list[length].rsplit(' ', 1)[0],func_id)
			logger.info(callee_string)
			log_list.append(callee_string)
			callee_appended = True
		    elif not (log_list[length] == ' start'):
			length = length - 1
		    else: 
			callee_appended = True
		
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
    for _, method in inspect.getmembers(klass, inspect.ismethod):
	#due to not echoing twice (if method is only imported)
	if (method.__module__ == mod.__name__):
            echo_instancemethod(mod, klass, method, write)
    for _, fn in inspect.getmembers(klass, inspect.isfunction):
	#due to not echoing twice (if function is only imported)
	if (fn.__module__ == mod.__name__):
            setattr(klass, name(fn), staticmethod(echo(mod, klass, fn, write)))
    
def echo_module(mod, write=sys.stdout.write):
    """ Echo calls to functions and methods in a module.
    """
    for fname, fn in inspect.getmembers(mod, inspect.isfunction):
	#due to not echoing twice (that is if function is only imported and not defined in mod)
	if (fn.__module__ == mod.__name__):
            setattr(mod, fname, echo(mod, None, fn, write))
    for _, klass in inspect.getmembers(mod, inspect.isclass):
	#due to not echoing twice (if class is only imported and not defined in mod)
	if (klass.__module__ == mod.__name__):
            echo_class(mod, klass, write)

# initialise lists for all views: classes and functions before annotating
all_functions = []
functions_dict = []
log_list = []
log_list.append(' start')



#instrument functions by echoing all modules
from tardis import echo_all

func_length = len(all_functions)
print ('# Functions: %s' % len(all_functions))



##For the tests it looks like that##
from django.core.management import ManagementUtility
utility = ManagementUtility(None)
utility.execute()


path_name = 'tardis/LOGS/OutputFiles/'
log_f_name = path_name + 'logs.txt'
log_f = file(log_f_name, 'w')
