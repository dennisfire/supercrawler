# Author: Yunqiao Zhang
# Email: zhangyunqiao@gmail.com
'''
A Timing class which work with python WITH statement can get how much time
the enclosing context runs. See sample usage below.
'''

from datetime import datetime

class Timing(object):
  def __enter__(self):
    self.__start = datetime.now()
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.__end = datetime.now()
    self.Timing = self.__end - self.__start

  def __str__(self):
    return str(self.Timing)




# Unit test & Sample usage
if __name__ == '__main__':
  t = Timing()
  import time
  with t:
    time.sleep(2.5)
  print t



