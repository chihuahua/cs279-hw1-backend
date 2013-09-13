import sys, os, os.path
currentDirectory = os.getcwd()
sys.path.append(currentDirectory)
sys.path.append(os.path.join(currentDirectory, "hw1"))
os.environ['DJANGO_SETTINGS_MODULE'] = "hw1.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
