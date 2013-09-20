import commands
from django.db import models

# Create your models here.
class Session(models.Model):
  '''
  A single session by a user.
  '''

  # The hash that identifies this session.
  hash = models.CharField(max_length=50, unique=True)

  # Which UI was displayed first.
  firstUi = models.CharField(max_length=16, choices=commands.uiTypes)
  
  # Which UI is preferred.
  preferredUi = models.CharField(max_length=16, choices=commands.uiTypes, default='')

  # Time at which session was made.
  createdTime = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return "Session " + self.hash + " with " + self.firstUi + " displayed first." 

class Trial(models.Model):
  '''
  A single trial that occured during the testing phase.
  '''

  # The hash of the session during which this trial occured.
  sessionHash = models.CharField(max_length=50)

  # Which UI this trial tested.
  uiType = models.CharField(max_length=16, choices=commands.uiTypes)

  # The unix time in ms at which the instructions for the trial load.
  beginTime = models.BigIntegerField()

  # The unix time in ms at which the user clicks on the right icon.
  endTime = models.BigIntegerField()

  # Whether errors were made.
  errorsMade = models.IntegerField()

  # Whether this trial requires a tab switch.
  tabSwitch = models.BooleanField()

  # The number of this trial (from 1 to 90).
  number = models.IntegerField()
  
  # Time at which session was made.
  createdTime = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return "Trial for " + self.uiType + "."

class TaskLoadEntry(models.Model):
  '''
  A single set of responses for the NASA TLX form.
  '''
  
  # The hash of the session during which this trial occured.
  sessionHash = models.CharField(max_length=50)

  # Which UI this trial tested.
  uiType = models.CharField(max_length=16, choices=commands.uiTypes)
  
  # Various ratings.
  mentalDemandRating = models.IntegerField()
  physicalDemandRating = models.IntegerField()
  temporalDemandRating = models.IntegerField()
  performanceRating = models.IntegerField()
  effortRating = models.IntegerField()
  frustrationRating = models.IntegerField()

  """  
  # Ignore these fields for now. We're only doing 6 qs.
  # Various tallies.
  mentalDemandTally = models.IntegerField()
  physicalDemandTally = models.IntegerField()
  temporalDemandTally = models.IntegerField()
  performanceTally = models.IntegerField()
  effortTally = models.IntegerField()
  frustrationTally = models.IntegerField()
  
  # Various weights.
  mentalDemandWeight = models.FloatField()
  physicalDemandWeight = models.FloatField()
  temporalDemandWeight = models.FloatField()
  performanceWeight = models.FloatField()
  effortWeight = models.FloatField()
  frustrationWeight = models.FloatField()
  
  # Overall score.
  overallScore = models.FloatField()
  """
  
  # Time at which session was made.
  createdTime = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return 'Task load entry for ' + self.uiType

