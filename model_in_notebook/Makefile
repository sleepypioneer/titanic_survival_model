IMG_NAME := sleepypioneer/titanic-model

.PHONY: build
build:
	docker build -t $(IMG_NAME) .

.PHONY: dev
dev: build
	docker run -i --network host \
		-v "$(shell pwd)/notebooks:/work" -w /work \
		$(IMG_NAME) \
		jupyter notebook \
			--notebook-dir=/work \
			--ip='0.0.0.0' --port=8888 \
			--no-browser --allow-root \
			--NotebookApp.token='' --NotebookApp.password=''

