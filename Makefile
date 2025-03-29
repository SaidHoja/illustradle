run:
	python src/main.py

build:
	docker build . -t illustradle

docker-run:
	docker run -p 5050:8080 illustradle