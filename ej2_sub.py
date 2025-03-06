import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class MiNodoSubscriptor(Node):
    def __init__(self):
        super().__init__('Nodo3')
        self.subscription1 = self.create_subscription(Int32, 'odd', self.listener_callback1, 10)
        self.subscription1
        self.subscription2 = self.create_subscription(Int32, 'even', self.listener_callback2, 10)
        self.subscription2

        self.m1 = 0
        self.m2 = 0


        
    def listener_callback1(self, msg1):
        self.m1 = msg1.data * msg1.data

    def listener_callback2(self, msg2):
        self.m2 = msg2.data * msg2.data
        sum = self.m2 + self.m1
        self.get_logger().info('Suma Cadrados: "%s"' % sum)


        

        

def main(args=None):
    rclpy.init(args=args)
    mi_nodo = MiNodoSubscriptor() 
    rclpy.spin(mi_nodo)  
    mi_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()