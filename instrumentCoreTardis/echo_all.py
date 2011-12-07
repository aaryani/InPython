#import djangorecipe.manage
from tardis.import_module import *

#from tardis.checking import echo_module

#import the right echo_module function
import inspect
frame = inspect.currentframe()
caller = frame.f_back.f_code.co_filename
caller= caller.rsplit('.', 1)[0]
caller = caller.split('/', 4)[4]
caller = caller.replace('/','.')
if caller == 'tardis.Logs.metamodelling':
	from tardis.Logs.metamodelling import echo_module
elif caller == 'tardis.DEF_CALL.metamodelling':
	from tardis.DEF_CALL.metamodelling import echo_module


# while echoing count statically  and update the  above lists
echo_module(manage) 			#No module named django.core.management
echo_module(search_sites) 		#No module named haystack #django.core.exceptions.ImproperlyConfigured: You must define the HAYSTACK_SITECONF setting before using the search framework.
echo_module(settings)
echo_module(test_settings)
echo_module(urls) 			#No module named django.contrib
#Settings cannot be imported, because environment variable DJANGO_SETTINGS_MODULE is undefined.

echo_module(apps)
echo_module(apps.equipment)
echo_module(apps.equipment.admin) 	
echo_module(apps.equipment.forms)	
echo_module(apps.equipment.models)	
echo_module(apps.equipment.tests)	
echo_module(apps.equipment.urls)	
echo_module(apps.equipment.views)	
echo_module(apps.equipment.migrations)
#echo_module(apps.equipment.migrations.0001_initial)	#SyntaxError: invalid syntax
echo_module(apps.hpctardis)
echo_module(apps.hpctardis.models)	
echo_module(apps.hpctardis.tests)	
echo_module(apps.hpctardis.urls)	
echo_module(apps.hpctardis.views)	
echo_module(apps.microtardis)
echo_module(apps.microtardis.models)	
echo_module(apps.microtardis.tests)	
echo_module(apps.microtardis.views)
echo_module(apps.microtardis.filters)
echo_module(apps.microtardis.filters.microtags) 

echo_module(tardis_portal)
echo_module(tardis_portal.MultiPartForm)
echo_module(tardis_portal.ParameterSetManager)	
echo_module(tardis_portal.ProcessExperiment)	
echo_module(tardis_portal.admin)		
echo_module(tardis_portal.constants)
echo_module(tardis_portal.context_processors)	
echo_module(tardis_portal.download)		
echo_module(tardis_portal.errors)
echo_module(tardis_portal.fields)		
echo_module(tardis_portal.forms)		
echo_module(tardis_portal.logging_middleware)	
echo_module(tardis_portal.managers)		
echo_module(tardis_portal.metsexporter)		
echo_module(tardis_portal.metshandler)
echo_module(tardis_portal.metsparser)		
echo_module(tardis_portal.metsstruct)

#echo_module(tardis_portal.models)		# problems with tests	
echo_module(tardis_portal.rfc3339)
#echo_module(tardis_portal.search_indexes)	#No module named haystack.indexes
echo_module(tardis_portal.shortcuts)		
echo_module(tardis_portal.staging)		
#echo_module(tardis_portal.views)		
echo_module(tardis_portal.widgets)		
echo_module(tardis_portal.auth)
echo_module(tardis_portal.auth.authentication)
echo_module(tardis_portal.auth.authservice)
echo_module(tardis_portal.auth.decorators)
echo_module(tardis_portal.auth.interfaces)
echo_module(tardis_portal.auth.ip_auth)
echo_module(tardis_portal.auth.ldap_auth)
echo_module(tardis_portal.auth.localdb_auth)
echo_module(tardis_portal.auth.utils)
echo_module(tardis_portal.filters)
#echo_module(tardis_portal.filters.exif)		#ImportError: Can't import pyexiv2 please install it
echo_module(tardis_portal.management)
echo_module(tardis_portal.management.commands)
#echo_module(tardis_portal.management.commands.echo) 
echo_module(tardis_portal.management.commands.backupdb)
echo_module(tardis_portal.management.commands.createsuperuser)
echo_module(tardis_portal.management.commands.dumpschemas)
echo_module(tardis_portal.management.commands.loadschemas)
echo_module(tardis_portal.migrations)
#echo_module(tardis_portal.migrations.0001_initial)		#SyntaxError: invalid syntax
#echo_module(tardis_portal.migrations.0002_auto__add_field_parametername_order)
echo_module(tardis_portal.minidetector)
echo_module(tardis_portal.minidetector.useragents)
echo_module(tardis_portal.publish)
echo_module(tardis_portal.publish.interfaces)
echo_module(tardis_portal.publish.publishservice)
echo_module(tardis_portal.publish.rif_cs_profile)
echo_module(tardis_portal.publish.rif_cs_profile.rif_cs_PublishProvider)
echo_module(tardis_portal.schema)
echo_module(tardis_portal.schema.mets)
echo_module(tardis_portal.schema.metssubs)
echo_module(tardis_portal.templatetags)
echo_module(tardis_portal.templatetags.basiccomparisonfilters)
echo_module(tardis_portal.templatetags.dynurl)
echo_module(tardis_portal.templatetags.experimentstats)
echo_module(tardis_portal.templatetags.feed)
echo_module(tardis_portal.templatetags.formfieldfilters)
echo_module(tardis_portal.templatetags.uploadify_tags)
echo_module(tardis_portal.templatetags.xmldate)
echo_module(tardis_portal.tests)
echo_module(tardis_portal.tests.ldap_ldif)
echo_module(tardis_portal.tests.mock_vbl_auth)
echo_module(tardis_portal.tests.mock_vbl_download)
#echo_module(tardis_portal.tests.slapd)
#echo_module(tardis_portal.tests.test_authentication)
#echo_module(tardis_portal.tests.test_authorisation)
#echo_module(tardis_portal.tests.test_authservice)
#echo_module(tardis_portal.tests.test_download)
#echo_module(tardis_portal.tests.test_filters)
#echo_module(tardis_portal.tests.test_forms)
#echo_module(tardis_portal.tests.test_ldap)
#echo_module(tardis_portal.tests.test_models)
#echo_module(tardis_portal.tests.test_parametersetmanager)
#echo_module(tardis_portal.tests.test_staging)
#echo_module(tardis_portal.tests.test_views)
#echo_module(tardis_portal.tests.tests)
#echo_module(tardis_portal.tests.urls)

#import django.conf.urls.defaults
#import django.contrib.auth.urls
#import django.http
#import django.template
#import django.template.base
#import django.template.context
#import django.template.debug
#import django.template.defaultfilters
#import django.template.loader
#import django.template.smartif

#echo_module(django.conf.urls.defaults)
#echo_module(django.contrib.auth.urls)
#echo_module(django.http)
#echo_module(django.template)
#echo_module(django.template.base)
#echo_module(django.template.context)
#echo_module(django.template.debug)
#echo_module(django.template.defaultfilters)
#echo_module(django.template.loader)
#echo_module(django.template.smartif)

