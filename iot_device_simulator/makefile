init:
	pip install termplotlib
ifeq ($(UNAME), Darwin)
	brew install gnuplot
endif

run:
	python main.py

run_gui:
	python main.py graph

test:
	python ./tests/test_data_processor.py