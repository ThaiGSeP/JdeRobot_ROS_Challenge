import rclpy
from std_msgs.msg import String

def callback(msg):
    print('Received: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    subscriber = rclpy.create_node('subscriber')
    subscriber.create_subscription(String, 'topic', callback, 10)
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
