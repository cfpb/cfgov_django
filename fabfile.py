from fabric.api import env, local, run, task, cd
from fabric.contrib import files

from fabtools.vagrant import vagrant
 
@task
def install_nvm():
    if not files.exists('/home/vagrant/.nvm'):
        run('curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh | bash')

@task
def setup_sh_deps():
    if not files.exists('/home/vagrant/.depsinstalled'):
        install_nvm()
        run('git config --global url."https://".insteadOf git://')
        run('nvm install 0.12')
        run('nvm use 0.12 && npm install -g grunt-cli && npm install -g bower')
        run('touch /home/vagrant/.depsinstalled')
@task
def setup_refresh():
    setup_sh_deps()
    with cd('/code/cfgov-refresh'):
        run('nvm use 0.12 && ./setup.sh')

@task
def sheer_index():
    with cd('/code/cfgov-refresh/dist'):
        run('WORDPRESS=http://www.consumerfinance.gov sheer index')
@task
def gruntserver():
    with cd('/code/cfgov-django/cfgov'):
        run('nvm use 0.12 && python manage.py gruntserver 0.0.0.0:8000')


@task
def test():
    with cd('/code/cfgov-django/cfgov'):
        run('tox -e py27')
