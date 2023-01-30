#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import re
def rearrange_name(name):
  result = re.search(r"^([\w\.\s]*), ([\w\.\s]*)$",name)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])