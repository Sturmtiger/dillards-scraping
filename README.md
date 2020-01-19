# dillards-scraping
hw (dillards.com)

# How to work with the project
I used Python version 3.6.9

Note: Remember to configure the django environ in the scrapy_app settings according to the path on your computer.

Do not forget `pip install -r requirements.txt`

The project also has fixtures with parsed products(3500 items):

`./manage.py loaddata dillards_app/fixtures/parsed_products.json` (use that command to load the data in the Model)

# Project run
1. `scrapy crawl dillards`
2. `celery -A dillards_project.celery_app worker -l INFO`
3. `./manage.py runserver`

The site is intuitive.
