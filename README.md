# Calorie Counter
SIMPLE CRUD API WITH DJANGO REST FRAMEWORK

## Requirements
- Python 3.6
- PostgreSQL 9.6 or higher

## Installation  
`python -m venv env`

You can install all the required dependencies

pip install -r requirements.txt

### Create Database

`sudo -u postgres psql`  
  
`CREATE DATABASE calorie_counter;`  
`CREATE USER cal_user WITH PASSWORD 'pa$$word';`  
`GRANT ALL PRIVILEGES ON DATABASE calorie_counter TO cal_user;`  

### Create .env file
- In the project directory create a file `.env`
- Save env variables to this file  
    `DEBUG=on`  
    `DATABASE_URL=postgres://cal_user:passpass@127.0.0.1:5432/calorie_counter`  
    `ALLOWED_HOSTS="0.0.0.0","localhost"`  

 Run migrations and start server
 `python manage.py runserver 0.0.0.0:8002`
