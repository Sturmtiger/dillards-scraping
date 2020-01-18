# dillards-scraping
hw (dillards.com)

# How to work with the project
Note: Remember to configure the django environ in the scrapy_app settings according to the path on your computer.

Do not forget `pip install -r requirements.txt`

# Project run
1. `scrapy crawl dillards`
2. `celery -A dillards_project.celery_app worker -l INFO`
3. `./manage.py runserver`

The site is intuitive.
