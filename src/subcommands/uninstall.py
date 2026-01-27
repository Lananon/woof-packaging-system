import os
import subprocess
import shutil
from pathlib import Path

def uninstall_package(package):
  home = Path.home()
  pkgname = pkgname = package.rsplit('/', 1).pop() 
  uninstall_script_dir = str(home) + "/.woof/uninstall/" + pkgname

  os.chdir(uninstall_script_dir)
  subprocess.call(["sh", os.getcwd() + "/uninstall.sh"])
  
  os.chdir(
      os.path.abspath(os.pardir)
  )
  print(os.getcwd())
  shutil.rmtree(uninstall_script_dir)
