from app.__init__ import app as application

import sys, os
app_root_dir = os.path.dirname(os.path.realpath(__file__))
INTERP = os.path.join(app_root_dir, 'venv/bin/python3.10')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

#sys.path.append(os.getcwd())
#sys.path.append('~/merrytutordata.site/app')


if __name__ == '__main__':
    app_instance = application
    app_instance.run()