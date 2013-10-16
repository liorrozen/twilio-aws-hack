import sys
import subprocess

# install
pipfile = "dependencies"
cmd = "pip install -r %s --target site-packages" % pipfile
print "Run: %s" % cmd
subprocess.call( cmd, shell = True )
