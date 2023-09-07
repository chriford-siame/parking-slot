
migrate:
	@python manage.py migrate

migrations:
	@python manage.py makemigrations

collectstatic:
	@python manage.py collectstatic --no-input

superuser:
	@python manage.py createsuperuser

runserver:
	@python manage.py runserver 8001

shell:
	@python manage.py shell

init-local:
	@pip install pip
	@pip install virtualenv
	@python -m virtualenv venv

dev:
	@pip install -r requirements.txt
	@python manage.py migrate
	@python manage.py collectstatic --no-input
	@python manage.py createsuperuser
	@python manage.py runserver
