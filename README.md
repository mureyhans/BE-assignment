## Description ##
This is a mini-project about Contact API using Django-Rest-Framework.

## Prerequisites ##
- Install Docker. To install Docker on Mac you can follow these steps explained [here](https://docs.docker.com/docker-for-mac/install/).

## How to Run ##
1. Clone this repository 
2. Start Docker
3. Open terminal and go to the project folder
4. Run `docker-compose build`, wait until the build has finished, then
5. Run `docker-compose up`
6. Finally, open up your browser and go to `localhost:8000/docs/`

## How to Test the API ##
- Open a new terminal and go to the project:
  - If the container already running, execute `docker exec contact_api python manage.py test`.
  - Otherwise, `docker-compose run web python manage.py test`.