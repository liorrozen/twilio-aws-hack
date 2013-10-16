import sys
import subprocess

# install
pipfile = "dependencies"
cmd = "pip install -r %s --user" % pipfile
print "Run: %s" % cmd
subprocess.call( cmd, shell = True )
