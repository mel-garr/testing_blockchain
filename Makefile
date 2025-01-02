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

	INFURA_URL=https://sepolia.infura.io/v3/68535a9d8e6e4f1f92ca21bd25ce1ed5
PRIVATE_KEY=c7734089f791f1c724451045ff606ffb0d1591bee61d562aa668a58b4a7466a2
ACCOUNT_ADDRESS=0xFb02aEeB164786B0885bB178CDC09133872093EE
