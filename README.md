# CC_AWS_Project

This repository contains a **Flask-based user registration app** that stores user data in SQLite and renders registration and profile pages with HTML templates.

## Files

- pp.py defines the Flask routes and database interactions
- 	emplates/ contains the registration and profile pages
- users.db stores the application data
- laskapp.wsgi supports WSGI-based deployment

## Features

- user registration form
- SQLite-backed persistence
- profile page lookup by username
- simple server-side routing with Flask

## Run Locally

`ash
pip install flask
python app.py
`

Then open http://127.0.0.1:5000/ in your browser.

## Notes

This project looks like a classroom or deployment-practice app. For production use, secrets management, password hashing, and form validation should be added.
