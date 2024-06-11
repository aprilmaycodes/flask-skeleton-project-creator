# Flask Project Skeleton Generator

## Introduction

Welcome to the Flask Project Skeleton Generator! This tool creates a Flask project skeleton from the command line, complete with a `requirements.txt` file, `base.html` with bootstrap imported, and blueprints. I started learning Django recently, and was inspired by it's project creation, how the basic structure of the app is set up for you. This generator aims to streamline the setup process for Flask projects, saving time so you can jump right in to the coding.

## Features

- **Automatic Project Structure**: Generates a standard Flask project structure with blueprints of your choice.
- **Pre-configured Files**: Includes `requirements.txt`, `config`, `__init__.py`, `main.py`, and more.
- **Templates and Static Files**: Creates `templates` and `static` folders in each blueprint and the main app.
- **Bootstrap Integration**: Provides a `base.html` file with (as of now) the most recent Bootstrap integration for quick UI development.
- **TODO Comments**: Includes TODO comments throughout, pointing out places where you may want to update the default settings (ex: `#TODO update database name if needed`)
- **Completely Customizable**: Update skeleton.py with your ideal setup. Add pages, remove pages, etc.

## Installation

To install and use the Flask Project Skeleton Generator, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AprilBlossoms/flask-skeleton-project-creator.git
    ```

2. **Update The Defaults**:
    
    In your favorite code editor, open skeleton.py and search for `# TODO TODO-FIRST` (or see lines 11, 15, 240, and 263)

    There are multiple TODO comments that will be added to your created projects, to remind you to change default values if needed. Additionally, there are four within `skeleton.py` that are important to review before you run the code.

    - Line 11 (optional): update your default dependencies
        - (what will be added to requirements.txt if the dependencies prompt is left blank). You're welcome to just use mine if you like.

    - Line 15 (important!): update `base_dir`
        - This can be an absolute path to the folder you'd like your projects created in (probably best practice) or you can be a rebel and move skeleton.py to your `repos` folder, for example. If you run it from there, with base_dir set to something like `flask_projects`, it will create your projects in `repos\flask_projects` without needing the absolute path

    - Line 240 (optional): Update your config.py.  
        - You're welcome to use the setup I use, but if you don't need Flask-Mail, you may as well remove the mail settings. Add other configurations you use frequently, etc.

    - Line 263 (important!): Update your `.env`
        - Unless you want each project being created with dummy data, update the .env creation to include the environment variables you want to include

## Usage

To generate a new Flask project skeleton
 - navigate to the folder containing `skeleton.py`
   - probably your repos folder, if you've opted for a local `base_dir`, or the cloned repo if you're using an absolute path for `base_dir`

- run the following command:

```bash
python skeleton.py
```

- You will be prompted to enter a project name (snake_case).
- Then you will be prompted to enter the desired blueprints (snake_case, comma separated)
- Finally, you will be prompted to enter the dependencies you want to include (watch your spelling). If you leave this blank, the defaults will be added to requirements.txt

- Open your new project in our favorite code editor, activate the venv ( `venv\Scripts\activate` on windows) and then run
 ```bash
pip install -r requirements.txt
```
- Go through the TODOs (Pycharm has this feature built in, but if you're using VS Code, I recommend the TODO Tree extension. On other code editors, I guess ctrl+F) and make any necessary changes.

## Congratulations, you've created a basic project and are ready to dive into the code!

The generated project structure will look like this:
```
└── project_name/
    ├── project_name/
    │   ├── blueprint_one/
    │   │   ├── static
    │   │   ├── templates
    │   │   ├── routes.py
    │   │   ├── forms.py
    │   │   └── __init__.py
    │   ├── blueprint_two/
    │   │   ├── static
    │   │   ├── templates
    │   │   ├── routes.py
    │   │   ├── forms.py
    │   │   └── __init__.py
    │   ├── static/
    │   │   └── styles.css
    │   ├── templates/
    │   │   └── base.html
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── venv
    ├── .env
    ├── .flaskenv
    ├── config.py
    ├── main.py
    └── requirements.txt
```

## Contact
For any questions or suggestions, please open an issue or reach out via contact@aprilmaycodes.com.

Thank you for checking out the Flask Project Skeleton Generator! Happy Coding!
