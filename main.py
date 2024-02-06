#libraries
import os
#function definition
def create_project_structure(project_name):
    project_path = os.path.join(os.path.expanduser('~'), 'Downloads', project_name)
    print(project_path)
    
    os.makedirs(project_path)

    # Create project folder
    folders = ['src', 'tests', 'docs']
    
    for folder in folders:
        os.makedirs(os.path.join(project_path, folder))

    
    # Create placeholder files
    open(os.path.join(project_path, 'src', '_init_.py'), 'a').close()
    open(os.path.join(project_path, 'src', 'module1.py'), 'a').close()
    open(os.path.join(project_path, 'tests', '_init_.py'), 'a').close()
    open(os.path.join(project_path, 'tests', 'test_module1.py'), 'a').close()
    open(os.path.join(project_path, 'requirements.txt'), 'a').close()
    open(os.path.join(project_path, 'README.md'), 'a').close()
    open(os.path.join(project_path, '.gitignore'), 'a').close()
    open(os.path.join(project_path, 'setup.py'), 'a').close()

    print(f"Project structure for '{project_name}' created in Downloads folder.")

# Function call
create_project_structure('Your Project Name')
