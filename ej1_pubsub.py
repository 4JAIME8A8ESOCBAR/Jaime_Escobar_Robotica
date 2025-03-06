import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from std_msgs.msg import Int32

import random

class MiNodoPublicadorSubscriptor(Node):
    def __init__(self):
        super().__init__('Nodo2')
        self.publisher = self.create_publisher(Int8, 'sum', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.j = 0

        self.subscription = self.create_subscription(Int8, 'numbers', self.listener_callback, 10)
        self.subscription


        
    def listener_callback(self, msg1):
        self.get_logger().info('Recived: "%s"' % msg1.data)
        self.dat = msg1.data
        
    def timer_callback(self):
        msg2 = Int8()
        msg2.data = self.j + self.dat

        self.publisher.publish(msg2)
        self.get_logger().info('Suma: "%s"' % msg2.data)
        self.j = msg2.data

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicadorSubscriptor() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()