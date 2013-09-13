#
# Views for hw1: study2 of the command maps paper.
#

import random
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  '''
  Home page view.
  '''
  # Create an ID for this session.
  if "sessionId" not in request.session:
    request.session["sessionId"] = random.getrandbits(128)

  return render_to_response('home.html',
      context_instance=RequestContext(request))

