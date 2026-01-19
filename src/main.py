import sys
from git import Repo
import os
import subprocess

def main():
  repo_url = sys.argv[1]
  destination = "/tmp/repo"

  fetched_repo = Repo.clone_from(repo_url, destination)
  print(fetched_repo.working_dir)
  
  os.chdir(destination)
  subprocess.call(["sh", os.getcwd() + "/install.sh"])

  
if __name__ == "__main__":
  main()
