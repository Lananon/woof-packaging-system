import sys
from subcommands import install
from subcommands import uninstall
from subcommands import update
from subcommands import install_from_pkg_repo

def main():
  if sys.argv[1] == "fetch":
    install_from_pkg_repo.pkg_repo_install(sys.argv[2])
  if sys.argv[1] == "bite":
    uninstall.uninstall_package(sys.argv[2])
  if sys.argv[1] == "update":
    update.update_system()


if __name__ == "__main__":
  main()
