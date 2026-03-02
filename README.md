![Language](https://img.shields.io/badge/language-python-blue.svg)
![Database](https://img.shields.io/badge/database-scyllaDB-lightgray.svg)
![Cache](https://img.shields.io/badge/cache-redis-red.svg)
![Tests](https://img.shields.io/badge/tests-locust-purple.svg)
![Infra](https://img.shields.io/badge/infra-docker-black.svg)
![Framework](https://img.shields.io/badge/framework-fastAPI-green.svg)
![License](https://img.shields.io/github/license/gitmvfs/fastAPI-shortlink.svg)

# About Project 👽
The fastAPI-shortlink project is based in a architecture proposal by Renato Augusto in your video [Arquitetando um Encurtador de URL](https://www.youtube.com/watch?v=m_anIoKW7Jg)
the objective is to fulfill the following requirements:

## System Requirements

| Requirement | Version |
| --- | --- |
| Python | 3.11 |
| Docker | 28.2.2 |
---
**Obs: Python 3.11 is obrigated because new versions has conflited with cassandra-driver**

## Functional requirements

 
| Requirement | Description |
| --- | --- |
| URL shortening | Given a long URL, return a much shorter URL.    |
| URL redirect | Given a shorter URL, redirect to the original URL. |

---

## Non functional requirements

- The system must support 100 million URLs generated per day.
- The shortened URL should be as short as possible.
- Only numbers (0-9) and characters (az, AZ) are allowed in the URL.
- For every 1 write operation in the database, there will be 10 read operations.
- The average length of stored URLs is 100 bytes.
- URLs must be stored for a minimum period of 10 years.
- The system must operate in high availability mode 24/7.

# How to start 🏗

## First step clone the project in your local machine

  ```bash
  git clone https://github.com/gitmvfs/fastAPI-shortlink
  ```

## Create a Virtual Environment on project folder

  ```bash
  py -3.11 -m venv venv
  ```
## Activate the Virtual Environment

  | System | Command |
  | --- | --- |
  | macOS/Linux | ` source venv/bin/activate ` |
  | Windows (CMD)| `.\\venv\\Scripts\\activate ` |
  | Windows (PowerShell)| `.\\venv\\Scripts\\Activate.ps1` |
  ---

## Confirm python version
 ```bash
 python -V
 ```
 Result:
 ```bash
 Python 3.11.9
 ```

## Install Packages
```bash
pip install -r requirements.txt
```

## Start docker-compose
```bash
docker-compose up -d
```

## Config .env

| Parameter | Description | Default value |
| --- | --- | --- |
| domain_host | `domain` is the URL of the API's domain or IP address. Example: `shortlink.com.br` | 127.0.0.1 |
| domain_port |`domain port` is the domain port where the API is hosted. | 3030 |
| node_database| The `node database` refers to the nodes of ScyllaDB. You can pass a comma-separated list, `e.g. "127.0.0.1,127.0.0.2"`, or just a single node as a parameter; it all depends on how you configure your cluster environment. | 127.0.0.1 |
| redis_host | `redis_host` is the default IP address where your Redis cluster or 'simple' database is hosted. | 127.0.0.1 |
| redis_port |The `redis_port` attribute indicates to the library/driver whether the connection is being made to a single database (6379) or a cluster (16379). | 6379 |
| redis_max_connections | `redis_max_connections` represents how many simultaneous connection pools will be established.  | 1000 |
| replication_factor |The `replication factor` is the ScyllaDB data backup configuration; it represents how many nodes the data will be replicated to. | 1 |
| secret_word | The `secret word` is responsible for scrambling the hash generation for link shortening. | marcos santos |

Obs: if you want use every default value only rename .env.example for .env

## Start fastAPI server

```bash
 uvicorn main:app --host 0.0.0.0 --port 3030 --reload
```
# Swagger

For use Swagger docs access: `http://127.0.0.1:3030/docs`

# Endpoints

### `GET /`
Health check

Response Example:
```json
{
  "Status": "Online",
  "Version": "1.0.0",
  "Current_Time": "2026-03-02T19:10:35.126569"
}
```

### `GET /url/{hash}` 
Redirect to Original URL

Structured Example:
```bash
curl "http://{domain_host}:{domain_port}/url/{hash}"
```

Default Env Example:
```bash
curl "http://127.0.0.1:3030/url/MVFS"
```

Response Example:
```swagger
curl -X 'GET' \
  'http://127.0.0.1:3030/url/MVFS' \
  -H 'accept: */*'
```

### `POST /url/{hash}`
Create a new short link

Structured Example:

```bash
  curl -X 'POST' \
  'http://{domain_host}:{domain_port}/url/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'original_url=www.google.com'
```

Default Env Example:

```bash
  curl -X 'POST' \
  'http://127.0.0.1:3030/url/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'original_url=www.google.com'
```

Response Example:
```json
{
  "message": "success",
  "data": {
    "original_url": "www.google.com",
    "short_url": "http://127.0.0.1:3030/WqQW"
  }
}
```

# Tests

### Use locust with GUI:

```bash
Locust -f ./tests/locustfile.py --host http://127.0.0.1:3030
```
`Now acess http://localhost:8089`


### Use locust without GUI:
```
locust -f ./tests/locustfile.py --headless -u 300 -r 15 --host http://127.0.0.1:3030
```

|Parameters|Description|
| --- | --- |
| u | Specifies the total number of users to simulate |
| r | Specifies the spawn rate (users per second) |

---
