"""
WSGI config for startlearner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
"""python_home = '/var/myproject/python'
import sys
import site

site_packages = python_home + '/lib/python2.7/site-packages'

# Add the site-packages directory.

site.addsitedir(site_packages)
"""
"""
python_home = '/var/myproject/python'
activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
"""
import os
import sys
#import site

#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#if ROOT_DIR not in sys.path:
#    sys.path.append(ROOT_DIR)
sys.path.append('/var/myproject/python/lib/python2.7/site-packages')
sys.path.append('/var/myproject/startlearner')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "startlearner.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
