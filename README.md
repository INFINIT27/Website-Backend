To create a virtual environment in a UNIX environment:
- sudo apt install python3-pip -y
- sudo apt install python3-venv -y
- python3 -m venv env
- source env/bin/activate
- git clone https://github.com/INFINIT27/Website-Backend.git

To activate the virtual environment run the following line:

- env/Scripts/activate

To run the server type:
- change the directory to the backend -> cd .../backend
- run this command -> python manage.py runserver 0.0.0.0:8000

To run migrations type in the console:
- python manage.py makemigrations
- python manage.py migrate

Also, remember to install the dependencies that are located under the Website-Backend/backend directory using the command:
- pip install -r requirements.txt
