
# python3 backend/manage.py dumpdata user          --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/user/fixtures/init_fixtures.json
# python3 backend/manage.py dumpdata show          --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/show/fixtures/init_fixtures.json
# python3 backend/manage.py dumpdata kit_of_values --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/kit_of_values/fixtures/init_fixtures.json
# python3 backend/manage.py dumpdata landing       --indent 2 --format json --exclude auth.permission --exclude contenttypes > backend/landing/fixtures/init_fixtures.json

# python3 backend/manage.py loaddata backend/user/fixtures/init_fixtures.json
# python3 backend/manage.py loaddata backend/show/fixtures/init_fixtures.json
# python3 backend/manage.py loaddata backend/kit_of_values/fixtures/init_fixtures.json
# python3 backend/manage.py loaddata backend/landing/fixtures/init_fixtures.json


