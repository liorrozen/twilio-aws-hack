import site
import sys
import os

full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)
site.addsitedir( path + '/site-packages' )

from fabric.api import env, run, cd

# TODO: Kill previous process
print "Killing previous process"

env.host_string = "184.72.219.16"
env.user = "ubuntu"
repo_dir = "/home/ubuntu/hack/twilio-aws-hack"

with cd( repo_dir ):
    run( "git reset --hard" )
    run( "touch yeaaaaaaaa" )
    run( "git pull" )
    run( "python setup.py install" )
    
