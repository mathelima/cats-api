<div id="top"></div>

<h3 align="center">Cats-API</h3>

  <p align="center">
    This API is based on <a href="https://thecatapi.com/">The Cat API</a> and is responsible for storing breeds information and cat images.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#entities">Entities</a></li>
    <li><a href="#logging">Logging</a></li>
    <li><a href="#metrics">Metrics</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![cats-api-diagram drawio](https://user-images.githubusercontent.com/32756259/157138997-eec3ac4d-4c67-4959-9544-2af59d555305.png)

The idea of this project was to create an API that store some cat information on a database, exposing logs and metrics on external tools, with everything running on docker containers.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Django](https://djangoproject.com/)
* [Django-rest-framework](https://django-rest-framework.org/)
* [Postgres](https://postgresql.org/)
* [Docker](https://docker.com/)
* [Prometheus](https://prometheus.io/)
* [Grafana](https://grafana.com)
* [Filebeat](https://elastic.co/beats/filebeat)
* [Elastic Search](https://elastic.co)
* [Kibana](https://www.elastic.co/kibana/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

To run the project it is necessary to have docker installed.
  ```sh
  https://www.docker.com/get-started
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mathelima/cats-api.git
   ```
2. Build the API docker image
   ```sh
   docker build -t matheuslima/cats-api .
   ```
3. Use docker-compose to create all containers
   ```sh
   docker-compose up -d
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

With all the containers up, the API should be running on http://localhost:8000 and it's possible to realize some requests.

To list all the cats breeds, use the method GET on http://localhost:8000/breeds/

To list a specific breed, use the method GET on http://localhost:8000/breeds/{id}

To see all the breeds from a specific origin, for example Egypt, use the method GET on http://localhost:8000/breeds/?origin=Egypt 

To filter all the breeds with a specific temperament, for example Playful, use the method GET on http://localhost:8000/breeds/?search=playful

_For all the endpoints, please look at the [Swagger](https://localhost:8000/docs)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Entities -->
## Entities

Breeds
- Atributes: 
1. description: Char
2. id: Char
3. images: Char 
4. name: Char
5. origin: Char
6. temperament: Char
- Endpoint: /breeds

Categories
- Atributes: 
1. id: Integer
2. images: Char 
3. name: Char
- Endpoint: /categories

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LOGGING -->
## Logging

Elastic search, Filebeat and Kibana are used to provide online logging.

Kibana can be accessed throw http://localhost:5601/ and can be configured to see the logging from cats-api.

To configure Kibana, you need to navigate to discover → index patterns → create index pattern and then:

![image](https://user-images.githubusercontent.com/32756259/158718762-7264f84b-7ddf-408b-82e8-647d4f7e3065.png)
![image](https://user-images.githubusercontent.com/32756259/158718791-5520bbaf-839a-4b8e-b0eb-e4f59d8ab7dc.png)

Now everything is done and you can see logs on menu → observability → logs

Exemple of logging on Kibana querying INFO logs:

![logs](https://user-images.githubusercontent.com/32756259/157148131-15bfe5ce-7d51-4c98-86b5-8ecc24a8cdb1.png)

If you prefer to see on the container, it is necessary to change the LOG_FORMAT on settings.py to console as default.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- METRICS -->
## Metrics

Prometheus and Grafana are used to provide the API metrics.

Grafana can be accessed throw http://localhost:3000/ and is is possible to configure some dashboards to extract cats-api metrics. The default user and password is admin.

Exemples of dashboards:
- Latency:
 
![latency](https://user-images.githubusercontent.com/32756259/157150365-35ac79ea-a5e5-4bd1-806f-bbba290695c9.png)

- Requests:
 
![requests](https://user-images.githubusercontent.com/32756259/157150383-aa67ffbd-8c59-4eab-ad23-e4c76b7ebd03.png)

- Errors:

![errors](https://user-images.githubusercontent.com/32756259/157150391-50090056-7912-4212-99a6-1be7bb9128bb.png)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Matheus Lima - [Linkedin](https://www.linkedin.com/in/matheus-lima-andrade/) - math.lima.andrade@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

