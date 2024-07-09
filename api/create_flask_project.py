import os

def create_flask_project(project_name):
    # Define the structure of the Flask project
    directories = [
        f"{project_name}",
        f"{project_name}/app",
        f"{project_name}/app/templates",
        f"{project_name}/app/static",
        f"{project_name}/app/models",
        f"{project_name}/app/views",
        f"{project_name}/app/controllers",
        f"{project_name}/instance"
    ]
    
    files = {
        f"{project_name}/run.py": run_py_content,
        f"{project_name}/app/__init__.py": init_py_content,
        f"{project_name}/app/views/views.py": views_py_content,
        f"{project_name}/app/models/__init__.py": "",
        f"{project_name}/app/controllers/__init__.py": "",
        f"{project_name}/config.py": config_py_content,
        f"{project_name}/instance/config.py": instance_config_py_content,
        f"{project_name}/requirements.txt": requirements_txt_content,
    }
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Create files with content
    for file_path, content in files.items():
        with open(file_path, "w") as file:
            file.write(content)
    
    print(f"Flask project '{project_name}' created successfully.")

# Content for the files
run_py_content = '''from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
'''

init_py_content = '''from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    
    return app
'''

views_py_content = '''from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')
'''

config_py_content = '''import os

class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG = True
'''

instance_config_py_content = '''SECRET_KEY = 'you-will-never-guess'
'''

requirements_txt_content = '''Flask==2.1.1
'''

# Main entry point
if __name__ == '__main__':
    project_name = input("Enter the project name: ")
    create_flask_project(project_name)
