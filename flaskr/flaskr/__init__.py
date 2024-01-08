import os

from flask import Flask

def create_app(test_config=None): #application factory function
    app=Flask(__name__, instance_relative_config=True) #this is a flask instance with name of the python module: __name__
    app.config.from_mapping(
        SECRET_KEY='9ebfa3d24c2c432878635ee587f561be32901b9545526a47cdbaefd097a13b11',
        DATABASE=os.path.join(app.instance_path,'flaskr')
    ) #this is default configuration of the app with the database file path 
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'
    #route to see the hello world code
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)


    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app