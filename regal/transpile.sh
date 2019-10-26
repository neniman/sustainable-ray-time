#!/bin/bash -eu
#: Transpile source changes to SCAD.
#: Optionally send SCAD files somewhere for rendering.

TARGET=${1:-}
RENDERER=${2:-}

inotifywait -m -e modify box.py |
while read file;
do
	echo "Transpiling."
	#make $TARGET
	python3 box.py
	echo "Waiting for source changes."
done
