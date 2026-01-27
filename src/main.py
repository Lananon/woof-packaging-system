import sys
from subcommands import install
from subcommands import uninstall
from subcommands import update


def main():
  if sys.argv[1] == "fetch":
    install.install_package(sys.argv[2])
  if sys.argv[1] == "bite":
    uninstall.uninstall_package(sys.argv[2])
  if sys.argv[1] == "update":
    update.update_system()
if __name__ == "__main__":
  main()
