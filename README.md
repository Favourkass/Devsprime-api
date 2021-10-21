# DevsPrime API

![DevsPrime API](https://devsprime.herokuapp.com)

API Service backing client interfaces

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description


## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/decadevs/devsprime-api.git` to clone the project repository.

Change directory into the project folder `cd devsprime-api` and build the base python image used for the project that was specified in ***dockerfile*** by running ` docker build . ` *Note the dot (.) at end of the command*.

Spin up other services needed for the project that are specified in ***docker-compose.yml*** file by running the command `docker-compose up`. At this moment, your project should be up and running with a warning that *you have unapplied migrations*.

Open up another terminal and run this command `docker-compose exec api python project/manage.py makemigrations` for creating new migrations based on the models defined and also run `docker compose exec api python project/manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/decadevs/devsprime-api.git
2. cd devsprime-api
3. docker build .
4. docker-compose up
5. docker-compose exec api python project/manage.py makemigrations
6. docker-compose exec api python project/manage.py migrate
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

```docker
docker-compose exec api python project/manage.py test
```

## License

The MIT License - Copyright (c) 2020 - Present, Decagon Institute. https://decagonhq.com/

## Contributors

<table>
    <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/47287618?v=4" width="100px;">
                <br /><sub><b>Elias Imokhai</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/81363219?v=4" width="100px;">
                <br /><sub><b>Omolade Ologun</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/81357407?v=4" width="100px;">
                <br /><sub><b>Favour Nnabue Chukwuemeka</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/42432746?v=4" width="100px;">
                <br /><sub><b>Folorunso Elujoba</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/76221338?v=4" width="100px;">
                <br /><sub><b>Benjamin Idewor</b></sub>
            </div>
        </td>
      </tr>
      <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/49361680?v=4" width="100px;">
                <br /><sub><b>Ajibola Oluewatobi Gureje</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/71507031?v=4" width="100px;">
                <br /><sub><b>Afeez Agbaje</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/80605206?v=4" width="100px;">
                <br /><sub><b>Ayodele Oluwatosin</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/67855565?v=4" width="100px;">
                <br /><sub><b>Oyerinmade Hakeem</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/81101034?v=4" width="100px;">
                <br /><sub><b>Samson Osiomwan</b></sub>
            </div>
        </td>
      </tr>
      <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/38279402?v=4" width="100px;">
                <br /><sub><b>Believe Ohiozua</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars0.githubusercontent.com/u/59091045?s=400&v=4" width="100px;">
                <br /><sub><b>Confidence Peters - Lead</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars0.githubusercontent.com/u/41590285?s=400&u=94012e0e2613d9dd6178beafd2507f97dab5a241&v=4" width="100px;">
                <br /><sub><b>Adenike Awofeso</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars0.githubusercontent.com/u/61936161?s=400&v=4" width="100px;">
                <br /><sub><b>Rafihatu Oziohu Bello - Lead</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars1.githubusercontent.com/u/49355114?s=460&u=17218f01b571cbad08912982baab6c31cc8cf004&v=4" width="100px;">
                <br /><sub><b>Olatunde Sodiq - Lead</b></sub>
            </div>
        </td>
      </tr>
</table>
