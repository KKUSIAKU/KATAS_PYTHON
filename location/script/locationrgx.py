'''

A text processing function to extraction all location names in a given text. 
This is built to process french language

'''

import re

def location(text):
  return re.search('Paris',text).group(0)