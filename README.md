# WeatherBackendTest
Example Django proyect for a backend test

### Annotations
* This proyect doesn't protect/hide the API key, DB password/user and the Django secret keys because of the nature of the project, in a real world scenario there would be restricted access to said sensitive data and would be away from any public repositories.
* The app doesn't use any users.
* App API accesible via http://127.0.0.1/api (has web interface)

# How to
* **Docker and docker compose is needed.** 
* Execute `docker-compose up` and let it build.
* Once the containers are up and running, create the DB with `docker-compose exec weatherapi python manage.py migrate`
* To update (connect to the API) the DB forecast, run `docker-compose exec weatherapi python manage.py updateWeather`. It's made in a way it can be added to a crontab for daily updates, using Django admin custom commands.
* To run the tests, it can be done `docker-compose exec weatherapi python manage.py test locationModule`, taking advantage of built in Django tests.


### Requirements
* Data from external API: https://api.tutiempo.net/json.html (You can use other Open API if wanted)
* Data saved on a DB
* API Rest that shows the data saved on the DB, filtered by city
* Project runs on Docker
* Python 3
* This project should have unit tests.
