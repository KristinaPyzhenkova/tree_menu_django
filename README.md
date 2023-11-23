# tree_menu_django

## Description
This project aims to implement a hierarchical tree menu using Django. The project provides a Dockerized environment for easy setup and deployment. Additionally, a custom Django migration is included to populate the database with sample data for convenience.

## Create environment files by copying the provided template files:
```
cp .env.template .env
cp .env.db.template .env.db
```

## Building and Running
Build and run the Docker containers:
```
 docker compose build && docker compose down && docker compose up --build
```

## Custom Django Migration
A custom Django migration has been added to populate the database with sample data. 

## Usage
Navigate to 
```
http://localhost:8022/app/world_classics
``` 
in your web browser to interact with the tree menu.
