from git import Repo
import subprocess
import os
import shutil
from pathlib import Path


def install_package(package):
  
  # get home directory
  home = Path.home()
  # get name of package
  pkgname = package.rsplit('/', 1).pop()
  # clone package repo
  destination = "/tmp/repo"
  try:
    shutil.rmtree(destination)
  except:
    pass
  print("cloning repo,,,")
  Repo.clone_from(package, destination)


  # create package info directory if it doesnt exist
  print("creating info directory,,,")
  info_dir = str(home) + "/.woof/pkginfo/" + pkgname
  try:
    os.mkdir(info_dir)
  except OSError as e:
    print("Error: ", e)
  
  # copy uninstall script into info directory
  shutil.copyfile(destination + "/uninstall.sh", info_dir + "/uninstall.sh")

  # save commit ID to file in info dir
  # used to check if a package has been updated
  with open(info_dir + "/commit", "w") as f:
    f.write(Repo(package).git.rev_parse("HEAD"))
  # save repo url for updating
  with open(info_dir + "/origin", "w") as f:
    f.write(package)
  

  # go into repo dir and run install script
  os.chdir(destination)
  print("compiling package,,")
  subprocess.call(["sh", os.getcwd() + "/install.sh"])
  shutil.rmtree(destination)
  print("-----------------------------------\ninstallation complete x3")
