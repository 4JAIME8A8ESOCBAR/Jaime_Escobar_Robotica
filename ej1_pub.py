import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

import random

class MiNodoPublicador(Node):
    def __init__(self):
        super().__init__('Nodo1')
        self.publisher = self.create_publisher(Int8, 'numbers', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg1 = Int8()
        msg1.data = self.i
        
        self.publisher.publish(msg1)
        self.get_logger().info('Numero evidado: "%s"' % msg1.data)
        numero_aleatorio = random.randint(-10, 10)
        self.i = numero_aleatorio

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicador() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()