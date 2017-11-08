# PlyReader
A simple parser and renderer for stanford polygon format files to render in opengl with python.

Run (cow):

	python3 main.py model0.ply

Run (text):
	
	python3 main.py model1.ply

Add another model:

To add a model, simply add the .ply file into the model directory.

Draw outlines:

To draw an outline around the model (make all edges white), press SPACE.

Quit:

Click the x or press ESC.

Rotation:

By default the model will rotate around the x-axis. Pressing p, UP_ARROW, DOWN_ARROW, RIGHT_ARROW, or LEFT_ARROW changes this behavior.

p - Pressing p will stop and start the auto rotation.

UP_ARROW - Holding this key will rotate the model about the y-axis. The model will appear to rotate upwards.

DOWN_ARROW - Holding this key will rotate the model about the y-axis. The model will appear to rotate down.

RIGHT_ARROW - Holding this key will rotate the model about the x-axis. The model will appear to rotate to the right.

LEFT_ARROW - Holding this key will rotate the model about the x-axis. The model will appear to rotate to the left.
