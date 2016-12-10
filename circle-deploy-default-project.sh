# A script to deploy the default project automatically
# to github to provide easier viewing of code and documentation
# Meant to be run on a circleci machine

# abort the script if there is a non-zero error
set -e

# show where we are on the machine
pwd

remote=git@github.com:JTarball/django-myproject.git

cd django-myproject

# now lets setup a new repo so we can update the master branch
git config --global user.email "james.tarball@gmail.com" > /dev/null 2>&1
git config --global user.name "JTarball" > /dev/null 2>&1
git init
git remote add --fetch origin "$remote"


# stage any changes and new files
git add -A
# now commit, ignoring branch gh-pages doesn't seem to work, so trying skip
git commit --allow-empty -m "Deploy to Default Django Page for `git log -1 --pretty=short --abbrev-commit`"
# and push, but send any output to /dev/null to hide anything sensitive
git push --force origin master

echo "Finished Deployment of files to https://JTarball/django-myproject/ !"

