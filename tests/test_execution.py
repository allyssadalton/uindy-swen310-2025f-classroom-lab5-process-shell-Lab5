import pytest
import os
from pathlib import Path
import filecmp


def test_psh2_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/answer/psh2_results"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "Arg"
  count = stdout_file_content.count(substring)

  if count >= 1:
    assert True
  else:
    assert False

def test_psh1_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/psh1_out"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()
  print("-----")
  print(stdout_file)
  substring = "PID"
  count = stdout_file_content.count(substring)

  if count > 0:
    assert True
  else:
    assert False

def test_psh1_output2():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/psh1_out"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()
  print("-----")
  print(stdout_file)
  substring = "TIME "
  count = stdout_file_content.count(substring)

  if count > 0:
    assert True
  else:
    assert False
    
# def test_exec_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello, Alex"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_exec_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out2"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello,"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False