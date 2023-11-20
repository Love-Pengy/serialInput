
	To find the serial port: 
		- in the test folder there's a python file that you can run. Itll echo the port/device info when you unplug/plugin the device. Youll need to change the serial port accordingly in the publisher file. 
	To build: 
		- colcon build --packages-select py_pubsub
	To run: 
		- open new terminal and run "source install/setup.bash" 
		- run "ros2 run py_pubsub talker" or "ros2 run py_pubsub listener" 
