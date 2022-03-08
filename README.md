<div id="top"></div>

<h3 align="center">Cats-API</h3>

  <p align="center">
    This API is based on `The Cat API`: https://thecatapi.com/ and is responsible for storing breeds information and cat images.
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

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- METRICS -->
## Metrics

Prometheus and Grafana are used to provide the API metrics.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Matheus Lima - [Linkedin](https://www.linkedin.com/in/matheus-lima-andrade/) - math.lima.andrade@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

