import app

#sys.path.append(os.getcwd())
#sys.path.append('~/merrytutordata.site/app')
app_instance = app.create_app()

if __name__ == '__main__':
    app_instance.run(debug = False)