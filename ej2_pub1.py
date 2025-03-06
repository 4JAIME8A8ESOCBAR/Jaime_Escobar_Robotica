import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32



class MiNodoPublicador1(Node):
    def __init__(self):
        super().__init__('Nodo1')
        self.publisher = self.create_publisher(Int32, 'odd', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        msg1 = Int32()
        msg1.data = self.i
        
        self.publisher.publish(msg1)
        self.get_logger().info('Numero impar evidado: "%s"' % msg1.data)
        self.i +=2

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicador1() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()