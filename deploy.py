import site
import sys
import os
import subprocess

full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)
site.addsitedir( path + '/site-packages' )

import fabric
from fabric.api import env, run, cd

print "Killing previous process"
cmd = "ps aux | grep \'/usr/bin/python app.py\' | awk \'{ print $2 }\' | xargs kill -9"
subprocess.call( cmd, shell = True )

env.host_string = "184.72.219.16"
env.user = "ubuntu"
repo_dir = "/home/ubuntu/hack/twilio-aws-hack"

with cd( repo_dir ):
    print "Killing previous process"
    run( "cat pid.lock | xargs kill" )

    run( "git reset --hard" )
    run( "touch yeaaaaaaaa" )
    run( "git pull" )
    run( "python setup.py install" )
    run( "nohup python app.py &" )

fabric.network.disconnect_all()

    
