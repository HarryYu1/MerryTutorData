from app import app as application

#sys.path.append(os.getcwd())
#sys.path.append('~/merrytutordata.site/app')
app_instance = application

if __name__ == '__main__':
    app_instance.run()