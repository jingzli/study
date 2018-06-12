import os
import sys
import shutil
import subprocess
import urllib
"""
The commands module doesn't work on Windows it's Unix-only. 
Additionally, it's deprecated since version 2.6, 
and it has been removed in Python 3, 
so you should use the subprocess module instead. Replace these lines:
"""


def print_file_in_dir (dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename)
    print path
    print os.path.abspath(path)
    
# find file in current directory
print_file_in_dir ('.')


print 'check dir or file exists----------------'
print os.path.exists('.\google-python-exercises')   # True
print os.path.exists('.\sample_dir')                # False        
print os.path.exists('D1_file.py')                  # True
print os.path.isdir('.\google-python-exercises')    # True
print os.path.isfile('.\google-python-exercises')   # False


print 'create dir----------------'
dir = '.\sample_dir'
if os.path.exists(dir): 
  os.rmdir(dir) # remove a empty directory 
if not os.path.exists(dir): 
  os.mkdir(dir)
  print os.path.exists('.\sample_dir')
  os.rmdir(dir)

# file copy
#shutil.copy(source, dest)


# run other script, and waite, return a tuple (status, output)
print 'run_cmd --------------------------------'
def run_cmd(win_cmd):
  process = subprocess.Popen(win_cmd, shell=True, stdout=subprocess.PIPE)
  (output, error) = process.communicate()
  if error:
    print 'ERROR:', error
  else:
    print output
 
def run_win_cmd(win_cmd):
  result = []
  process = subprocess.Popen(win_cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
  for line in process.stdout:
    result.append(line)
  errcode = process.returncode
  for line in result:
    print line,
  if errcode is not None:
    raise Exception('cmd %s failed, see above for details', cmd)


run_cmd('dir .')    
# run_win_cmd('dir .')

print 'returns output -----'
output =  subprocess.check_output("dir C:", shell=True)
print 'output: \n', output
print 'returns status -----'
status =  subprocess.call("dir C:", shell=True)
print 'status: ', status

# open network
uf = urllib.urlopen('http://google.com')
text  = uf.read()
print text
file_name = "https://www.google.com/logos/doodles/2018/celebrating-garden-gnomes-6194737877876736-2xa.gif"
urllib.urlretrieve(file_name, 'picfile.gif')
