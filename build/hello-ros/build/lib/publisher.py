import rclpy
from std_msgs.msg import String
from rclpy.node import Node
import time

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_message)
        self.i = 0

    def publish_message(self):
        message = String()
        message.data = 'Hello! ROS2 is fun'
        self.publisher_.publish(message)
        self.get_logger().info('Publishing: "%s"' % message.data)

def main(args=None):
    rclpy.init(args=args)
    publisher = PublisherNode()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
