# ERP RC




# Trabajando con Django

## Migraciones y Cargar Datos
Si has realizado cambios en los modelos o necesitas cargar datos iniciales en tu base de datos, asegúrate de ejecutar las migraciones como mencionamos anteriormente:

bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

## Accede al contenedor de Django
Puedes acceder al contenedor de tu aplicación Django usando el siguiente comando:

bash
Copiar código
docker-compose exec web sh

## Crear super usuario

bash
docker-compose exec web python manage.py createsuperuser

## Conectarme a Postgresql

bash
docker-compose exec db psql -U erp-rc -d erp-rc

### Obtener tablas
\dt


