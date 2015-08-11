#!/bin/sh
./vagrant/bootstrap_host.sh
vagrant up
fab vagrant setup_refresh
