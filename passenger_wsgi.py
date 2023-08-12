from app import app as application

import sys, os
# INTERP = os.path.join(os.environ['HOME'], 'example.com', 'venv', 'bin', 'python3')
INTERP = os.path.expanduser("~/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

#sys.path.append(os.getcwd())
#sys.path.append('~/merrytutordata.site/app')


if __name__ == '__main__':
    app_instance = application
    app_instance.run()