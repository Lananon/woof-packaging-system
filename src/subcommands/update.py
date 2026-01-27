import os
from pathlib import Path
from git import Repo
from . import install

home = Path.home()
info_dir = str(home) + "/.woof/pkginfo"

def update_system():
  package_list = os.listdir(info_dir)
  # create list for storing packages that need updating
  packages_to_update = []
  for package in package_list:
    package_dir = info_dir + "/" + package
    commit_ID = open(package_dir + "/commit").read()
    repo_url = open(package_dir + "/remote").read()
    repo = Repo(repo_url)

    # compare local commit ID with remote commit ID to check if update is needed
    if commit_ID != repo.git.rev_parse("HEAD"):
      packages_to_update.append(package)

  # ask user to confirm
  print("the following packages will be updated: ")
  for package in packages_to_update:
    package_dir = info_dir + "/" + package
    repo_url = open(package_dir + "/remote").read()
    print(package)
  if input("-----------------------------\nproceed? (y/n): ") == "y":
    # actually update packages
    for package in packages_to_update:
      package_dir = info_dir + "/" + package
      repo_url = open(package_dir + "/remote").read()

      install.install_package(repo_url)
    
    print("-------------------- \nupdate completed !!")
  else:
    pass
