# Yogabook 🧘
Yogabook is a fitness class venue and yoga instructor booking site that enables the discovery and booking of classes between independent instructors and venues.

## Technologies
* SQLAlchemy ORM
* PostgreSQL
* Python | Flask
* HTML
* CSS
* JavaScript

## Database Schema
The relationships between venues and yoga instructors is modelled below.
![](yoga.png)

## Scripts

1. Seed the database

``` flask seed seed ```

2. Clear the database

``` flask seed clear ```

3. Make migrations

``` flask db migrate ```

4. Upgrade database

``` flask db upgrade ```

5. Set development environment

``` export FLASK_ENV=development ```

6. Start project

``` flask run ```
