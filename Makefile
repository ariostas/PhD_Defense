SHELL := /bin/bash

.PHONY: jupyter render-all

jupyter:
	sudo docker run -it --rm --network host -v ${PWD}:/manim/manim/ manimcommunity/manim jupyter lab --ip=0.0.0.0

render-all:
	cat file_list.txt | while read f; do manim --save_sections --disable_caching $${f}; done
