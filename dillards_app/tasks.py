from dillards_project.celery_app import app
from .models import ParsedProduct


@app.task(name='dillards_app.tasks.save_products_to_db')
def save_products_to_db(items):
    for item in items:
        ParsedProduct.objects.create(**item)
