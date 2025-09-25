import pytest
import os
from pathlib import Path


def test_output_content1():
  cwd = os.getcwd()
  ansfile1 = cwd + "/answer/psh1.c"
  f = open(ansfile1)
  ans1_content = f.read()
  f.close()

  substring = "execvp"
  count = ans1_content.count(substring)
  # print count
  if count > 0:
    assert True
  else:
    assert False

def test_output_content2():
  cwd = os.getcwd()
  ansfile2 = cwd + "/answer/psh1.c"
  f = open(ansfile2)
  ans2_content = f.read()
  f.close()

  substring = "arglist"
  count = ans2_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False

def test_output_content3():
  cwd = os.getcwd()
  ansfile3 = cwd + "/answer/psh2.c"
  f = open(ansfile3)
  ans3_content = f.read()
  f.close()

  substring = "wait"
  count = ans3_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False

def test_output_content4():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/fork.c"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "Child"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content5():
  cwd = os.getcwd()
  ansfile5 = cwd + "/answer/fork.c"
  f = open(ansfile5)
  ans5_content = f.read()
  f.close()

  substring = "ls"
  count = ans5_content.count(substring)
  # print count
  if count > 0:
    assert True
  else:
    assert False


def test_output_content6():
  cwd = os.getcwd()
  ansfile6 = cwd + "/answer/fork.c"
  f = open(ansfile6)
  ans6_content = f.read()
  f.close()

  substring = "wait"
  count = ans6_content.count(substring)
  # print count
  if count > 0:
    assert True
  else:
    assert False


# def test_output_content7():
#   cwd = os.getcwd()
#   ansfile7 = cwd + "/answer/pc_pid.c"
#   f = open(ansfile7)
#   ans7_content = f.read()
#   f.close()

#   substring = "fork()"
#   count = ans7_content.count(substring)
#   # print count
#   if count > 0:
#     assert True
#   else:
#     assert False

# def test_output_content8():
#   cwd = os.getcwd()
#   ansfile8 = cwd + "/answer/pc_pid.c"
#   f = open(ansfile8)
#   ans8_content = f.read()
#   f.close()

#   substring = "getpid"
#   count = ans8_content.count(substring)
#   # print count
#   if count > 1:
#     assert True
#   else:
#     assert False


# def test_output_content9():
#   cwd = os.getcwd()
#   ansfile9 = cwd + "/answer/pc_pid.c"
#   f = open(ansfile9)
#   ans9_content = f.read()
#   f.close()

#   substring = "pid_t"
#   count = ans9_content.count(substring)
#   # print count
#   if count > 0:
#     assert True
#   else:
#     assert False
    
