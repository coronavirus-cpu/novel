# Novel

## System

* Ubuntu 18.04 LTS
* PostgreSQL 10.x
* Python 3.7.x

## Create Database

```
CREATE DATABASE golgotha;

CREATE USER golgotha WITH ENCRYPTED PASSWORD '********';


ALTER ROLE golgotha SET client_encoding TO 'utf8';
ALTER ROLE golgotha SET default_transaction_isolation TO 'read committed';
ALTER ROLE golgotha SET timezone TO 'UTC';


GRANT ALL PRIVILEGES ON DATABASE golgotha TO golgotha;
```
