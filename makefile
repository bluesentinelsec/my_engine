build:
	python3 tools/pack_media.py media/
	/bin/bash -c "source ./venv/bin/activate && python3 main.py -v data.dat"