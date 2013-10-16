import sys
import subprocess

# install
pipfile = "requirements.txt"
cmd = "pip install -r %s --user" % pipfile
print "Run: %s" % cmd
subprocess.call( cmd, shell = True )
