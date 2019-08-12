all:	build

PROJECT=kc-diagnostics

run = docker run --rm -it \
				-v $(shell pwd):/code \
				$(PROJECT):latest $1

build:
	docker build -t $(PROJECT):latest .

shell: 
	$(call run,bash)