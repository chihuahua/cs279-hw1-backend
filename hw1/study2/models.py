from django.db import models

# Types of UIs.
uiTypes = (
  ('commandMap', 'commandMap'),
  ('ribbon', 'ribbon'),
)

# Create your models here.
class Session(models.Model):
  '''
  A single session by a user.
  '''

  # The hash that identifies this session.
  hash = models.CharField(max_length=50, unique=True)

  # Which UI was displayed first.
  firstUi = models.CharField(max_length=16, choices=uiTypes)

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
  uiType = models.CharField(max_length=16, choices=uiTypes)

  # The time at which the instructions for the trial load.
  beginTime = models.DateTimeField()

  # The time at which the user clicks on the right icon.
  endTime = models.DateTimeField()

  # Whether errors were made.
  errorsMade = models.BooleanField(default=False)

  # Whether this trial requires a tab switch.
  tabSwitch = models.BooleanField()

  # The number of this trial (from 1 to 90).
  number = models.IntegerField()

  def __unicode__(self):
    return "Trial for " + uiType + "."

