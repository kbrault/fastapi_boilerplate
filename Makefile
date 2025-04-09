.PHONY: run test docker-build docker-run docker-shell

run:
	uvicorn app.main:app --reload

test:
	pytest

docker-build:
	docker build -t fastapi-app .

docker-run:
	docker run -it --rm -p 8000:8000 fastapi-app

docker-shell:
	docker run -it --rm fastapi-app /bin/bash
