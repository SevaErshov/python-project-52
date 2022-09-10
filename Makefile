runserver:
	poetry run python3 manage.py runserver

migrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

dj_shell:
	poetry run python manage.py shell