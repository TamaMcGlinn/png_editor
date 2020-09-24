all:
	docker build -t png_edit .

run:
	docker run -it -v $(PWD)/src:/opt/application png_edit
