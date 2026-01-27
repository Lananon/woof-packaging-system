from git import Repo
import subprocess
import os
import shutil
from pathlib import Path


def install_package(package):
  home = Path.home()

  # get name of package
  pkgname = package.rsplit('/', 1).pop()
  # clone package repo
  destination = "/tmp/repo"
  try:
    shutil.rmtree(destination)
  except:
    pass
  Repo.clone_from(package, destination)

  # create package uninstall directory if it doesnt exist
  uninstall_script_dir = str(home) + "/.woof/uninstall/" + pkgname
  try:
    os.mkdir(uninstall_script_dir)
  except OSError as e:
    print("Error: ", e)
  # copy uninstall script into uninstall script directory
  shutil.copyfile(destination + "/uninstall.sh", uninstall_script_dir + "/uninstall.sh")
  

  # go into repo dir and run install script
  os.chdir(destination)
  subprocess.call(["sh", os.getcwd() + "/install.sh"])
  shutil.rmtree(destination)
