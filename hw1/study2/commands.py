#
# Contains ordering of commands.
#

# The types of trials.
trialTypes = ['familiarity', 'performance']

# The types of UIs.
uiTypes = (
    ('commandMap', 'commandMap'),
    ('ribbon', 'ribbon'),
  )

# The command pattern for testing (30 trials total).
fPattern = [0, 2 , 3, 4, 1, 5, 2, 0, 3, 4, 5, 2, 1, 4, 0, 2, 5, 4, 1, 0, 5, 3, 2, 1, 4, 3, 5, 3, 4, 3]

# The command pattern for performance (90 trials total).
pPattern = [5, 4 , 3, 1, 3, 2, 0, 1, 3, 4, 1, 0, 2, 1, 0, 3, 5, 4, 1, 3, 4, 0, 2, 5, 3, 4, 3, 0, 1, 5, 3, 2, 4, 0, 1, 2, 4, 0, 2, 3, 4, 1, 0, 5, 2, 1, 0, 4, 3, 1, 2, 5, 0, 1, 3, 4, 5, 0, 2, 1, 4, 3, 5, 0, 1, 0, 1, 2, 0, 1, 3, 4, 2, 5, 0, 1, 3, 4, 1, 0, 4, 3, 2, 0, 1, 4, 3, 4, 3, 4]

# The indices of performance trials that involved tab switching.
tabSwitchIndices = {
    1: True,
    3: True,
    4: True,
    5: True,
    8: True,
    10: True,
    15: True,
    16: True,
    17: True,
    18: True,
    19: True,
    21: True,
    23: True,
    24: True,
    27: True,
    29: True,
    30: True,
    31: True,
    32: True,
    33: True,
    36: True,
    37: True,
    39: True,
    41: True,
    43: True,
    44: True,
    47: True,
    49: True,
    51: True,
    52: True,
    54: True,
    56: True,
    57: True,
    60: True,
    62: True,
    63: True,
    70: True,
    72: True,
    73: True,
    74: True,
    76: True,
    78: True,
    80: True,
    82: True,
    85: True
  }

# The command set for command maps and then ribbons.
commandMapCommands = ['increase-font-size', 'shape', 'underline', 'hyphenation', 'watermark', 'line']
ribbonCommands = ['align-text-right', 'italic', 'text-box', 'line-numbers', 'margins', 'bar']

# Mapping from short names to real names.
realNames = {
    'increase-font-size': 'Increase Font Size',
    'shape': 'Shape',
    'underline': 'Underline',
    'hyphenation': 'Hyphenation',
    'watermark': 'Watermark',
    'line': 'Line Chart',
    'align-text-right': 'Align Text Right',
    'italic': 'Italics',
    'text-box': 'Text Box',
    'line-numbers': 'Line Numbers',
    'margins': 'Margins',
    'bar': 'Bar Chart'
  }
  
# Names of tabs.
tabNames = [
    'home',
    'layout',
    'document-elements',
    'tables',
    'charts',
    'smartart',
    'review'
  ]

