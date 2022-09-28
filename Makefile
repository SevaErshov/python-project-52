runserver:
	poetry run python3 manage.py runserver

migrations: #migrate and migrations
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

dj_shell:
	poetry run python manage.py shell

test:
	poetry run python3 manage.py test