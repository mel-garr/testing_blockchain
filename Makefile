.PHONY: build up down logs shell clean shell-service

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

logs:
	docker-compose logs -f

logs-service:
	docker-compose logs -f $(SERVICE)

shell:
	docker-compose exec -f $(SERVICE) sh

clean:
	docker-compose system prume -f && docker system prume --volumes -f

re:
	docker-compose down && docker-compose up 
