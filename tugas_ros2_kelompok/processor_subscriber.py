import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ProcessorSubscriber(Node):
    def __init__(self):
        super().__init__('processor_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            '/keyboard_input',
            self.listener_callback,
            10)
        self.get_logger().info('Node Subscriber siap, menunggu data...')

    def listener_callback(self, msg):
        # --- INI ADALAH BAGIAN PEMROSESAN DATA REAL-TIME ---
        input_data = msg.data
        char_count = len(input_data)
        processed_data = input_data.upper()

        self.get_logger().info(f'Menerima: "{input_data}" | Proses: "{processed_data}" | Jml Karakter: {char_count}')
        # ----------------------------------------------------

def main(args=None):
    rclpy.init(args=args)
    node = ProcessorSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
