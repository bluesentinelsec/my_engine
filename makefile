run:
	./tools/pack_media.py -o data.dat media
	bash -c "source ./venv/bin/activate && python3 main.py data.dat"