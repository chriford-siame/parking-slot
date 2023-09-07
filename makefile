
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

dev:
	@pip install pip
	@python -m virtualenv venv
	@source venv/bin/activate
	@pip install -r requirements.txt
	@python manage.py migrate
	@python manage.py collectstatic --no-input
	@python manage.py createsuperuser
	@python manage.py runserver
