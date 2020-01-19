from dillards_project.celery_app import app
from .models import ParsedProduct


@app.task(name='dillards_app.tasks.save_products_to_db')
def save_products_to_db(items):
    """Bulk saves products to DB(ParsedProduct model)."""
    ParsedProduct.objects.bulk_create(
        [ParsedProduct(**item) for item in items]
    )
