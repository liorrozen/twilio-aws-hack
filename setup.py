import sys
import subprocess
import argparse

class Setup( object ):

    def __init__( self ):

        parser = argparse.ArgumentParser( description='Defines environment and initializes dependencies.' )
        parser.add_argument('action', metavar='install', type=str, help='Run this script')
        self.args = parser.parse_args()

    def parse_args( self ):
        try:
            return {
                "install" : self.install
            }[ self.args.action ]()
        except KeyError:
            print "Unknown command"


    def install( self ):

        subprocess.call( "rm -rf site-packages", shell = True )

        pipfile = "dependencies"
        target = "site-packages"
        exists_action = "i"
        install_cmd = "pip install -r %s --target %s --exists-action %s" % ( pipfile, target, exists_action )
        subprocess.call( install_cmd, shell = True )

    

if __name__ == "__main__":
    Setup().parse_args()

