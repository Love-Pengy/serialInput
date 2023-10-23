# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
import serial
import time
from std_msgs.msg import String





class MinimalPublisher(Node):

    def __init__(self, serial):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.ser = serial

    def timer_callback(self):
        msg = String()
        try: 
                #while True:
                    # Read a line from the serial port
                    line = self.ser.readline().decode('utf-8').rstrip()
                    if line:
                        msg.data = line
                    
                    else:
                        msg.data = "Line Couldn't Be Read"
                        # Optionally, you can add a small delay to reduce CPU usage in case of no data
                        #time.sleep(0.01)
                    
        except serial.SerialException as e:
            print(f"Error connecting to {port}: {e}")

        except KeyboardInterrupt:
            print("\nExiting...")

        # msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    # Configure the serial connection
    port = '/dev/ttyACM0'
    baudrate = 115200
    timeout = 0.25  # in seconds, adjust if needed
    #open port
    with serial.Serial(port, baudrate=baudrate, timeout=timeout) as ser:
        print(f"Connected to {port} with baudrate {baudrate}")
        minimal_publisher = MinimalPublisher(ser)

        rclpy.spin(minimal_publisher)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
