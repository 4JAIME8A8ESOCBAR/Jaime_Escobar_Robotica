import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32



class MiNodoPublicador2(Node):
    def __init__(self):
        super().__init__('Nodo2')
        self.publisher = self.create_publisher(Int32, 'even', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.j = 2

    def timer_callback(self):
        msg2 = Int32()
        msg2.data = self.j
        
        self.publisher.publish(msg2)
        self.get_logger().info('Numero evidado: "%s"' % msg2.data)
        self.j +=2

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoPublicador2() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()