FROM python:latest as base

RUN pip3 install --upgrade \
	python-telegram-bot \
	googletrans \
	pandas \ 
	numpy


