
### Migrate Database
`python manage.py makemigrations catalogue`

`python manage.py migrate catalogue`

### Sync Database with information (Only if needed)
`python manage.py loaddata catalogue/fixtures/*`

### Run Unit Tests
`coverage run manage.py test catalogue`

### Get Coverage Report in HTML
`coverage html`

### Run Server
`python manage.py runserver`
