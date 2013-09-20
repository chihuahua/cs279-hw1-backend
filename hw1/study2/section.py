#
# Introduces the concept of a section.
#

class Section:
  def __init__(self, title, instructions):
    self.title = title 
    self.instructions = instructions

fInstructions = """
  You will be given 30 icons to find and click on as accurately and quickly as possible.
  The purpose of this section is to get you familiar with an interface, so results from this section (of 30 tasks) will be discarded.
  Clicking on a wrong icon will produce a beep.
  """

pInstructions = """
  You will be given 90 icons to find and click on as accurately and as quickly as possible. Please do your best!
  Clicking on a wrong icon will produce a beep.
  """

# The first are for command maps. The second are for ribbons.
fSection = Section('UI Familiarization', fInstructions)
pSection = Section('UI Evaluation', pInstructions)
sections = [
    [fSection, pSection],
    [fSection, pSection]
  ]

