# Task Manager
### Hexlet tests and linter status:
[![Actions Status](https://github.com/MKashtanov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MKashtanov/python-project-52/actions)
[![lint&tests](https://github.com/MKashtanov/python-project-52/actions/workflows/main.yml/badge.svg)](https://github.com/MKashtanov/python-project-52/actions/workflows/main.yml)
### CodeClimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/3f1d20e3756af7b88113/maintainability)](https://codeclimate.com/github/MKashtanov/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3f1d20e3756af7b88113/test_coverage)](https://codeclimate.com/github/MKashtanov/python-project-52/test_coverage)
## About  
[Task Manager](https://task-manager-2l3z.onrender.com/) is a highly responsive web application designed to facilitate efficient task management and organization. With its user-friendly interface and robust features, users can seamlessly assign tasks, set labels, and manage task statuses.  
## Install  
- Clone repo: `git clone https://github.com/MKashtanov/python-project-52.git`
- Install dependencies: `make install`
- Run development server: `make dev`
## Deploy
- Build Command: `./build.sh`
- Start Command: `gunicorn task_manager.wsgi:application`
## Uses environments
- `DATABASE_URL` - database connection string. For example: postgresql://[user[:password]@][netloc][:port][/dbname]
- `SECRET_KEY` - is used in Django for cryptographic signing
- `RENDER_EXTERNAL_HOSTNAME` - specify a dynamic URL for your environment
- `ROLLBAR_ACCESS_TOKEN` - enter the access token you copied from Rollbar

## Stack  
![Static Badge](https://img.shields.io/badge/Python-3.10-blue)  
![Static Badge](https://img.shields.io/badge/Django-4.2.5-green)  
![Static Badge](https://img.shields.io/badge/Django_bootstrap4-23.2-purple)  
![Static Badge](https://img.shields.io/badge/rollbar-0.16.3-red)  
#### Development DB:  
![Static Badge](https://img.shields.io/badge/SQLite-3-brown)  
#### Production DB:  
![Static Badge](https://img.shields.io/badge/PostgreSQL-15-brown)  

