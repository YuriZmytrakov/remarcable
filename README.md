# Assignment

## Setup instructions

1. Create and activate a virtual environment: `python3 -m venv venv && source venv/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Run make migrations: `python3 manage.py makemigrations`
4. Run migrate: `python3 manage.py migrate`
5. Create admin user: `python3 manage.py createsuperuser`
6. Populate db: `python3 populate_db.py`
7. Run server: `python3 manage.py runserver`

## Tests
`python3 manage.py test products.tests`

## Product Listing
- Access at `/`
- Use search & filter functionality


## AI Support
- `populate_db.py`
- `base.html`, `product_detail.htmp` and `product_list.html`

## Recommendations
- Utilize Elasticsearch, OpenSearch for low maintenance, scalability and advanced search
