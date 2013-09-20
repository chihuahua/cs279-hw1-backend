#
# Views for hw1: study2 of the command maps paper.
#

import commands, models, random, section
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  '''
  Home page view.
  '''
  # potentially discount logs.
  if 'suppressLogs' in request.GET:
    request.session['suppressLogs'] = True

  return render_to_response('home.html',
      context_instance=RequestContext(request))


def consent(request):
  '''
  Responsible for loading a consent form.
  '''
  return render_to_response('consent.html')


def beginSession(request):
  '''
  Begins a session of user testing.
  '''
  if 'sessionId' not in request.session:
    # begin a session if necessary.
    hashValue = random.getrandbits(128)
    request.session['sessionId'] = hashValue
    request.session['trialNumber'] = 1 # trial numbers start at 1.
    request.session['trialType'] = 0 # 0 for famili., 1 for performance.
    request.session['done'] = False
  
    # decide whether command maps or ribbon first by a coin toss.
    firstUi = getFirstUi() 
    firstUiStr = commands.uiTypes[firstUi][0]
    request.session['firstUi'] = firstUi  
    request.session['ui'] = firstUi
    if not 'suppressLogs' in request.session:
      session = models.Session(
          hash = hashValue,
          firstUi = commands.uiTypes[firstUi][0]
        )
      session.save()

  return doTrials(request)

def getFirstUi():
  '''
  Gets the first UI to use.
  '''
  if not models.Session.objects.all().count():
    # no records yet. begin with command map.
    return 0

  lastSession = models.Session.objects.latest('id')
  return 0 if lastSession.firstUi == 'ribbon' else 1


def doTrials(request):
  '''
  Does trials of user testing.
  '''
  session = request.session
  
  if 'sessionId' not in session:
    # create a new session.
    return beginSession(request)
  
  trialNumber = session['trialNumber']
  currentUiNum = session['ui']
  trialType = session['trialType']

  currentTab = None
  if request.method == 'POST':
    postData = request.POST
    
    # get the current command.
    trialIndex = trialNumber - 1
    abstractCommandNum = commands.pPattern[trialIndex] if trialType else commands.fPattern[trialIndex]
    commandShort = commands.ribbonCommands[abstractCommandNum] if currentUiNum else commands.commandMapCommands[abstractCommandNum]
    
    if postData['selection'] == commandShort:
      if trialType:
        # add in a new record if performance trial was just performed.
        if not 'suppressLogs' in session:
          trial = models.Trial(
              sessionHash = session['sessionId'],
              uiType = commands.uiTypes[currentUiNum][0],
              beginTime = int(postData['beginTime']),
              endTime = int(postData['endTime']),
              errorsMade = int(postData['errorsMade']),
              tabSwitch = trialIndex in commands.tabSwitchIndices,
              number = trialNumber
            )
          trial.save()
      
      # move to next trial.
      session['trialNumber'] = trialNumber + 1 
  
    # maintain the current tab.
    currentTab = postData['currentTab']  

  # determine if switching to another section is needed.
  numFTrials = len(commands.fPattern)
  numPTrials = len(commands.pPattern)
  trialNumber = session['trialNumber']
  if trialType and trialNumber > numPTrials or trialType == 0 and trialNumber > numFTrials:
    # we should move to the next section.
    
    if trialType and trialNumber > numPTrials:
      # we're done with all trials for a single UI.
      return render_to_response('concludeUi.html', {'session': session})
    
    # switch to the next section.
    return moveToNextSection(request)
  
  trialIndex = trialNumber - 1
  abstractCommandNum = commands.pPattern[trialIndex] if trialType else commands.fPattern[trialIndex]
  commandShort = commands.ribbonCommands[abstractCommandNum] if currentUiNum else commands.commandMapCommands[abstractCommandNum]
  command = (commandShort, commands.realNames[commandShort])
  totalTrials = len(commands.pPattern) if trialType else len(commands.fPattern)
  
  return render_to_response('trial.html', {'currentTab': currentTab, 'session': session, 'totalTrials': totalTrials, 'command': command, 'tabs': commands.tabNames}, context_instance=RequestContext(request))


def moveToNextSection(request):
  '''
  Moves to the next section.
  '''
  session = request.session
  if session['trialType']:
    # move to next ui.
    session['ui'] = (session['ui'] + 1) % 2
    session['trialType'] = 0
  else:
    # move to next type of test.
    session['trialType'] = 1
  session['trialNumber'] = 1
  sect = section.sections[session['ui']][session['trialType']]
  return render_to_response('introToNextSection.html', {'section': sect})

def questionnaire(request):
  '''
  Concludes a UI with some questions.
  '''
  session = request.session
  if request.method == 'POST':
    postData = request.POST
    if not 'suppressLogs' in session:
      taskLoadEntry = models.TaskLoadEntry(
          sessionHash = session['sessionId'],
          uiType = commands.uiTypes[session['ui']][0],
          mentalDemandRating = int(postData['mentalDemandRating']),
          physicalDemandRating = int(postData['physicalDemandRating']),
          temporalDemandRating = int(postData['temporalDemandRating']),
          performanceRating = int(postData['performanceRating']),
          effortRating = int(postData['effortRating']),
          frustrationRating = int(postData['frustrationRating']),
      )
      taskLoadEntry.save()
    
    # move on to next section if applicable.
    if session['ui'] == session['firstUi']:
      return moveToNextSection(request)
    
    # have user evaluate which UI is better.
    return choseBetweenUis(request, suppressPost=True)
  return render_to_response('questionnaire.html', {'session': session}, context_instance=RequestContext(request))


def choseBetweenUis(request, suppressPost=False):
  '''
  Lets the user pick between 2 UIs.
  '''
  if request.method == 'POST' and not suppressPost:
    # Save the preference result.
    if not 'suppressLogs' in request.session:
      session = models.Session.objects.get(hash=request.session['sessionId'])
      session.preferredUi = request.POST['preferredUi']
      session.save()
    
    # We're done.
    request.session['done'] = True
    return render_to_response('done.html')
  return render_to_response('choseBetweenUis.html', context_instance=RequestContext(request))

