#!/bin/bash

if ! dpkg -l | grep python3-pip >/dev/null 2>&1; then
    sudo apt install python3-pip
fi

if ! pip3 list --format=columns | grep virtualenvwrapper >/dev/null 2>&1; then
    sudo pip3 install virtualenv virtualenvwrapper
fi

if [ -z "$WORKON_HOME" ]; then
    mkdir ~/python3-env
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
    echo "export WORKON_HOME=~/python3-env" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source ~/.bashrc
fi

if [ ! -d "~/python3-env/octoberry_backend" ]; then
    mkvirtualenv octoberry_backend -p python3 --no-site-packages
    workon octoberry_backend
fi

pip3 install -r requirements/dev.txt