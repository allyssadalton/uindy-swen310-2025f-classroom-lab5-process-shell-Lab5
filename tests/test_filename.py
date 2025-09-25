import pytest
import os
import re
from pathlib import Path

filenames = ["fork.c", "myps.sh", "psh1.c", "psh2.c", "psh2_results"]

def test_answer_files_exist():
  #adding flags
  flags = []
  for i in range(len(filenames)):
    flags.append(0)

  #get root
  cwd = os.getcwd()
  print("\n------The root dir is----------")
  print(cwd)

  count_true = 0
  for i in range(len(filenames)):
    ans_file = str(cwd) + "/answer/" + filenames[i]
    print(ans_file)

    if os.path.exists(ans_file):
      flags[i] = 1
      count_true = count_true + 1
  
  if count_true == len(flags):
    assert True
  else:
    assert False


