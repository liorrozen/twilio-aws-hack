from fabric.api import env, run, cd
# Kill previous process
print "Killing previous process"
env.host_string = "184.72.219.16"
env.user = "ubuntu"
repo_dir = "/home/ubuntu/hack/twilio-aws-hack"

with cd( repo_dir ):
    run( "git reset --hard" )
    run( "touch yeaaaaaaaa" )
    run( "git pull" )
    run( "python setup.py" )
    
