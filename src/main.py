import sys
from subcommands import install
from subcommands import uninstall



def main():
  if sys.argv[1] == "fetch":
    install.install_package(sys.argv[2])
  if sys.argv[1] == "bite":
    uninstall.uninstall_package(sys.argv[2])

if __name__ == "__main__":
  main()
