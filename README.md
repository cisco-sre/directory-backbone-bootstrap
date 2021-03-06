# Requirements
- git
- python virtualenv
- Python 3.6+
- pip
- various python modules (see requirements.txt after installing)

# First Time setup
- Clone this repository (will fail if the destination directory exists)
  * git clone https://github.com/cisco-sre/directory-backbone-bootstrap.git
- Enter newly created repository directory
  * cd directory-backbone-bootstrap
- Create virtualenv
  * python virtualenv venv --python=python3
- Use new virtualenv
  * Mac/Linux
    - source venv/bin/activate
  * Windows
    - venv\Scripts\activate

- Install requirements
  * pip install -r requirements.txt

# Launch
- From a terminal window, change to the directory where the repository was checked out above
- Make sure virtualenv is loaded
  - Mac/Linux
    * source venv/bin/activate
  - Windows
    * venv\Scripts\activate

- Set evironment variables and start flask (CTRL+C to stop)
  - Mac/Linux
    * export FLASK_DEBUG=1; export FLASK_APP=application.py; flask run
  - Windows
    * set FLASK_DEBUG=1
    * set FLASK_APP=application.py
    * flask run
    
# Notes
If you edit template files, you will need to stop and start flask to see the changes, editing python (.py) files will restart the server automatically.
