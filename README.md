# Azercell Document Platform

## Project Description
**Azercell Document Platform** is a web application for managing documents. It provides different kinds of filtering and searches functionality, like search in document content, filter by type of document, filter by department, and other filters.

### Requirements:
| # | Package | Version |
|---|---|----|
|1 | asgiref | 3.3.1
|2|Django | 3.1.5
|3|django-taggit | 1.2.0
|4|gunicorn | 20.0.4
|5|pytz | 2020.5
|6|sqlparse | 0.4.1

### How to run:
| Step | Command | Description |
| --- | --- | --- |
| 1 | `python3 -m venv venv` | Create virtual environment.|
| 2 | `source venv/bin/activate/` | Activate it
| 3 | `pip3 install -r requirements/<last one>.txt` | Install requirements |
| 4 | `cd source` | Change directory.
| 5 | `python3 manage.py runserver` | Run local testing server |
| * |  * | Don't forget to change hostname to your own in `source/Platform/settings/__init__.py`