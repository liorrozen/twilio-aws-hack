import site
import sys
import os

full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)
site.addsitedir( path + '/site-packages' )

import fabric
from fabric.api import env, run, cd

env.host_string = "184.72.219.16"
env.user = "ubuntu"
repo_dir = "/home/ubuntu/hack/twilio-aws-hack"

with cd( repo_dir ):

    run( "git reset --hard" )
    run( "touch yeaaaaaaaa" )
    run( "git pull" )

    # Creating virtual env
    run( "virtualenv venv --no-site-packages" )
    run( "source venv/bin/activate" )

    run( "python setup.py install" )
    run( "service twilio-aws-hack stop" )
    run( "service twilio-aws-hack start" )

fabric.network.disconnect_all()
