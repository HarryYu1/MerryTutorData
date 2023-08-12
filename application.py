from app import app as application

#sys.path.append(os.getcwd())
#sys.path.append('~/merrytutordata.site/app')


if __name__ == '__main__':
    app_instance = application
    app_instance.run()