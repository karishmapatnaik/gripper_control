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

from robotiq_85_msgs.msg import GripperCmd, GripperStat


class GripperPublisher(Node):

    def __init__(self):
        super().__init__('gripper_publisher')
        self.gripper_pub_ = self.create_publisher(GripperCmd, '/gripper/cmd', 10)
        timer_period = 1  # seconds

        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0

    def timer_callback(self):

        msg = GripperCmd()

        if self.i < 5:
            msg.position = 0.0
            msg.speed = 0.02
            msg.force = 5.0
            self.i += 1
        elif (self.i >= 5) & (self.i < 10):
            msg.position = 0.085
            msg.speed = 0.02
            msg.force = 5.0
            self.i += 1
        elif (self.i >= 10) & (self.i < 15):
            msg.position = 0.0
            msg.speed = 0.02
            msg.force = 5.0
            self.i += 1
        else:
            msg.position = 0.085/2
            msg.speed = 0.02
            msg.force = 5.0

        self.gripper_pub_.publish(msg)
        self.get_logger().info('Publishing gripper command as "%f"' % msg.position)

def main(args=None):
    rclpy.init(args=args)

    gripper_publisher = GripperPublisher()

    rclpy.spin(gripper_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gripper_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
