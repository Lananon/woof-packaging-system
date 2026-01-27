import os
import subprocess
import shutil
from pathlib import Path

def uninstall_package(package):
  home = Path.home()
  pkgname = pkgname = package.rsplit('/', 1).pop() 
  info_dir = str(home) + "/.woof/pkginfo/" + pkgname


  print ("running uninstall script...")
  os.chdir(info_dir)
  subprocess.call(["sh", os.getcwd() + "/uninstall.sh"])
  
  print("done !!")
  os.chdir(
      os.path.abspath(os.pardir)
  )
  print("removing pkginfo directory")
  shutil.rmtree(info_dir)
  print("done !!")
  print("-----------------------------------\npackage removal completed")
