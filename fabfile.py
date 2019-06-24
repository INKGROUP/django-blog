from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "git@github.com:INKGROUP/django-blog.git"
env.user = 'INKGROUP'
env.password = 'ourteam2016'

env.hosts = ['10.103.27.60']

env.port = '22'


def deploy():
    source_floder = '/home/ytf/sites/blog-project'
    run('cd %s && git pull ' % source_floder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_floder))