"""
Module documentation here
"""


def replace(text, n, old, new):
  """

  Parameters
  ---------
  text:  a string 

  n:  an integer the caracter position index to replace

  old:  the charac to be replaced 

  new : new character value

  returns: new string

  """
  old_index = [i for i in range(len(text)) if text[i] == old]
  print(old_index)
  text_chars = list(text)
  for index in old_index:
    if((old_index.index(index)+1)%n ==0):
      text_chars[index] = new
    
  return ''.join(text_chars)


