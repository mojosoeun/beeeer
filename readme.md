# beeer 

-- Installation for mac

1. Install postgres.app and setup the path
2. Create beeeer database
    - In your terminal run:
        - `createdb beeeer`
        - `psql beeeer`
    - Now you are in psql terminal. Now run
        - `CREATE EXTENSION postgis;`
    - Exit out of psql with `\q` + enter
3. Create virtualenv (python 3.3+) and enter it
4. In the terminal: `pip install -r requirements.txt`
5. Make sure the database settings match up with your postgres setup. Especially user and password
6. Terminal: `python manage.py migrate`
    - If you get errors about `GDAL`, you might need to run `brew install gdal`
