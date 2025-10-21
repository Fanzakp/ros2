import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Modul Python untuk membaca input keyboard
import sys
import tty
import termios

class KeyboardPublisher(Node):
    def __init__(self):
        super().__init__('keyboard_publisher_node')
        self.publisher_ = self.create_publisher(String, '/keyboard_input', 10)

        # Simpan pengaturan terminal lama
        self.old_settings = termios.tcgetattr(sys.stdin)
        self.get_logger().info('Node Publisher siap.')
        self.get_logger().info('Tekan tombol apapun... (Ctrl+C untuk berhenti)')

    def read_key(self):
        # Atur terminal ke mode "cbreak" (baca per karakter)
        tty.setcbreak(sys.stdin.fileno())
        key = sys.stdin.read(1) # Baca 1 karakter
        return key

    def restore_terminal(self):
        # Kembalikan pengaturan terminal seperti semula
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def run_loop(self):
        try:
            while rclpy.ok():
                key = self.read_key()

                # Cek jika itu Ctrl+C
                if key == '\x03':
                    self.get_logger().info('Ctrl+C ditekan, keluar...')
                    break

                # Buat pesan dan publish
                msg = String()
                msg.data = key
                self.publisher_.publish(msg)
                self.get_logger().info(f'Mem-publish: "{msg.data}"')

        except Exception as e:
            self.get_logger().error(f'Error: {e}')
        finally:
            # Pastikan terminal kembali normal saat program berhenti
            self.restore_terminal()

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardPublisher()
    node.run_loop()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
