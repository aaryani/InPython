#import djangorecipe.manage
#from tardis.import_module import *

#from tardis.checking import echo_module

#import the right echo_module function
import inspect
frame = inspect.currentframe()
caller = frame.f_back.f_code.co_filename
caller= caller.rsplit('.', 1)[0]
caller = caller.split('/', 4)[4]
caller = caller.replace('/','.')
if caller == 'tardis.LOGS.metamodelling':
	from tardis.LOGS.metamodelling import echo_module
elif caller == 'tardis.DEF_CALL.metamodelling':
	from tardis.DEF_CALL.metamodelling import echo_module


# while echoing count statically  and update the  above lists
import manage
echo_module(manage) 
import search_sites 			
echo_module(search_sites)
import settings	
echo_module(settings)
import test_settings
echo_module(test_settings)
import urls
echo_module(urls) 			

import apps
echo_module(apps)
import apps.equipment
echo_module(apps.equipment)
import apps.equipment.admin
echo_module(apps.equipment.admin) 
import apps.equipment.forms	
echo_module(apps.equipment.forms)
import apps.equipment.models
echo_module(apps.equipment.models)	
import apps.equipment.tests
echo_module(apps.equipment.tests)
import apps.equipment.urls	
echo_module(apps.equipment.urls)
import apps.equipment.views	
echo_module(apps.equipment.views)
import apps.equipment.migrations	
echo_module(apps.equipment.migrations)
#import apps.equipment.migrations.0001_initial
#echo_module(apps.equipment.migrations.0001_initial)	#SyntaxError: invalid syntax
import apps.hpctardis
echo_module(apps.hpctardis)
import apps.hpctardis.models
echo_module(apps.hpctardis.models)	
import apps.hpctardis.tests
echo_module(apps.hpctardis.tests)
import apps.hpctardis.urls
echo_module(apps.hpctardis.urls)
import apps.hpctardis.views	
echo_module(apps.hpctardis.views)
import apps.microtardis	
echo_module(apps.microtardis)
import apps.microtardis.models
echo_module(apps.microtardis.models)
import apps.microtardis.tests	
echo_module(apps.microtardis.tests)
import apps.microtardis.views	
echo_module(apps.microtardis.views)
import apps.microtardis.filters
echo_module(apps.microtardis.filters)
import apps.microtardis.filters.microtags 
echo_module(apps.microtardis.filters.microtags) 

import tardis_portal
echo_module(tardis_portal)
import tardis_portal.MultiPartForm
echo_module(tardis_portal.MultiPartForm)
import tardis_portal.ParameterSetManager
echo_module(tardis_portal.ParameterSetManager)
import tardis_portal.ProcessExperiment	
echo_module(tardis_portal.ProcessExperiment)
import tardis_portal.admin	
echo_module(tardis_portal.admin)
import tardis_portal.constants		
echo_module(tardis_portal.constants)
import tardis_portal.context_processors
echo_module(tardis_portal.context_processors)
import tardis_portal.download	
echo_module(tardis_portal.download)
import tardis_portal.errors		
echo_module(tardis_portal.errors)
import tardis_portal.fields
echo_module(tardis_portal.fields)
import tardis_portal.forms		
echo_module(tardis_portal.forms)
import tardis_portal.logging_middleware		
echo_module(tardis_portal.logging_middleware)	
import tardis_portal.managers
echo_module(tardis_portal.managers)
import tardis_portal.metsexporter		
echo_module(tardis_portal.metsexporter)	
import tardis_portal.metshandler	
echo_module(tardis_portal.metshandler)
import tardis_portal.metsparser
echo_module(tardis_portal.metsparser)
import tardis_portal.metsstruct		
echo_module(tardis_portal.metsstruct)

#import tardis_portal.models
#echo_module(tardis_portal.models)		# problems with tests: RuntimeError: maximum recursion depth exceeded
import tardis_portal.rfc3339
echo_module(tardis_portal.rfc3339)
#import tardis_portal.search_indexes
#echo_module(tardis_portal.search_indexes)	#No module named haystack.indexes
import tardis_portal.shortcuts
echo_module(tardis_portal.shortcuts)
import tardis_portal.staging		
echo_module(tardis_portal.staging)
#import tardis_portal.views		
#echo_module(tardis_portal.views)		#ViewDoesNotExist: Tried single_search in module tardis.tardis_portal.views. Error was: 						# 'tardis.tardis_portal.views.single_search' is not a callable
import tardis_portal.widgets		
echo_module(tardis_portal.widgets)
import tardis_portal.auth		
echo_module(tardis_portal.auth)
import tardis_portal.auth.authentication
echo_module(tardis_portal.auth.authentication)
import tardis_portal.auth.authservice
echo_module(tardis_portal.auth.authservice)
import tardis_portal.auth.decorators
echo_module(tardis_portal.auth.decorators)
import tardis_portal.auth.interfaces
echo_module(tardis_portal.auth.interfaces)
import tardis_portal.auth.ip_auth
echo_module(tardis_portal.auth.ip_auth)
import tardis_portal.auth.ldap_auth
echo_module(tardis_portal.auth.ldap_auth)
import tardis_portal.auth.localdb_auth
echo_module(tardis_portal.auth.localdb_auth)
import tardis_portal.auth.utils
echo_module(tardis_portal.auth.utils)
import tardis_portal.filters
echo_module(tardis_portal.filters)
#import tardis_portal.filters.exif
#echo_module(tardis_portal.filters.exif)		#ImportError: Can't import pyexiv2 please install it
import tardis_portal.management
echo_module(tardis_portal.management)
import tardis_portal.management.commands
echo_module(tardis_portal.management.commands)
#import tardis_portal.management.commands.echo
#echo_module(tardis_portal.management.commands.echo) 
import tardis_portal.management.commands.backupdb
echo_module(tardis_portal.management.commands.backupdb)
import tardis_portal.management.commands.createsuperuser
echo_module(tardis_portal.management.commands.createsuperuser)
import tardis_portal.management.commands.dumpschemas
echo_module(tardis_portal.management.commands.dumpschemas)
import tardis_portal.management.commands.loadschemas
echo_module(tardis_portal.management.commands.loadschemas)
import tardis_portal.migrations
echo_module(tardis_portal.migrations)
#import tardis_portal.migrations.0001_initial
#echo_module(tardis_portal.migrations.0001_initial)				#SyntaxError: invalid syntax
#import tardis_portal.migrations.0002_auto__add_field_parametername_order
#echo_module(tardis_portal.migrations.0002_auto__add_field_parametername_order)
import tardis_portal.minidetector
echo_module(tardis_portal.minidetector)
import tardis_portal.minidetector.useragents
echo_module(tardis_portal.minidetector.useragents)
import tardis_portal.publish
echo_module(tardis_portal.publish)
import tardis_portal.publish.interfaces
echo_module(tardis_portal.publish.interfaces)
import tardis_portal.publish.publishservice
echo_module(tardis_portal.publish.publishservice)
import tardis_portal.publish.rif_cs_profile
echo_module(tardis_portal.publish.rif_cs_profile)
import tardis_portal.publish.rif_cs_profile.rif_cs_PublishProvider 
echo_module(tardis_portal.publish.rif_cs_profile.rif_cs_PublishProvider)
import tardis_portal.schema
echo_module(tardis_portal.schema)
import tardis_portal.schema.mets
echo_module(tardis_portal.schema.mets)
import tardis_portal.schema.metssubs
echo_module(tardis_portal.schema.metssubs)
import tardis_portal.templatetags
echo_module(tardis_portal.templatetags)
import tardis_portal.templatetags.basiccomparisonfilters
echo_module(tardis_portal.templatetags.basiccomparisonfilters)
import tardis_portal.templatetags.dynurl
echo_module(tardis_portal.templatetags.dynurl)
import tardis_portal.templatetags.experimentstats
echo_module(tardis_portal.templatetags.experimentstats)
import tardis_portal.templatetags.feed
echo_module(tardis_portal.templatetags.feed)
import tardis_portal.templatetags.formfieldfilters
echo_module(tardis_portal.templatetags.formfieldfilters)
import tardis_portal.templatetags.uploadify_tags
echo_module(tardis_portal.templatetags.uploadify_tags)
import tardis_portal.templatetags.xmldate
echo_module(tardis_portal.templatetags.xmldate)
import tardis_portal.tests
echo_module(tardis_portal.tests)
import tardis_portal.tests.ldap_ldif
echo_module(tardis_portal.tests.ldap_ldif)
import tardis_portal.tests.mock_vbl_auth
echo_module(tardis_portal.tests.mock_vbl_auth)
import tardis_portal.tests.mock_vbl_download
echo_module(tardis_portal.tests.mock_vbl_download)
#import tardis_portal.tests.slapd
#echo_module(tardis_portal.tests.slapd)
#import tardis_portal.tests.test_authentication
#echo_module(tardis_portal.tests.test_authentication)
#import tardis_portal.tests.test_authorisation
#echo_module(tardis_portal.tests.test_authorisation)
#import tardis_portal.tests.test_authservice
#echo_module(tardis_portal.tests.test_authservice)
#import tardis_portal.tests.test_download
#echo_module(tardis_portal.tests.test_download)
#import tardis_portal.tests.test_filters
#echo_module(tardis_portal.tests.test_filters)
#import tardis_portal.tests.test_forms
#echo_module(tardis_portal.tests.test_forms)
#import tardis_portal.tests.test_ldap
#echo_module(tardis_portal.tests.test_ldap)
#import tardis_portal.tests.test_models
#echo_module(tardis_portal.tests.test_models)
#import tardis_portal.tests.test_parametersetmanager
#echo_module(tardis_portal.tests.test_parametersetmanager)
#import tardis_portal.tests.test_staging
#echo_module(tardis_portal.tests.test_staging)
#import tardis_portal.tests.test_views
#echo_module(tardis_portal.tests.test_views)
#import tardis_portal.tests.tests
#echo_module(tardis_portal.tests.tests)
import tardis_portal.tests.urls
echo_module(tardis_portal.tests.urls)

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

