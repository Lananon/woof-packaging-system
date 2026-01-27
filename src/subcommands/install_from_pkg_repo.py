import json
from . import install
from pathlib import Path

home = Path.home()

def pkg_repo_install(package):
  # put your packages into repo.json like this
  # {
  #   "pkgname": "url/to/pkg/repo" 
  # }
  # note that pkgname should be identical to the repository name on whatever git host the package is using
  repo_file = open(str(home) + "/.woof/config/repo.json").read()
  pkg_repo = json.loads(repo_file)
  package_url = pkg_repo[package]
  install.install_package(package_url)
