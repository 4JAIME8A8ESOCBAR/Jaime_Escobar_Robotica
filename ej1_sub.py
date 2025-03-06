import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8


class MiNodoSubscriptor(Node):
    def __init__(self):
        super().__init__('Nodo3')
        self.subscription = self.create_subscription(Int8, 'sum', self.listener_callback, 10)
        self.subscription
        self.k = 1


        
    def listener_callback(self, msg2):
        prom = msg2.data / self.k
        self.get_logger().info('N3_Promedio: "%s"' % prom)
        self.k +=1

        

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoSubscriptor() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()