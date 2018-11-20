# snproject

in an environment with >= python3.6 and pip installed

`pip install -r requirements.txt` from `snproject`

`python manage.py migrate` from `snproject/socialnetwork`

The users' passwords are `AdminAdmin1`

There is a single view at `http://localhost:8000/user/login/`

With an authenticated user: `http://localhost:8000/api/` lists endpoints

Different users have different privileges - login with `jagenau:AdminAdmin1` to view in `http://localhost:8000/admin`
