import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

def main(args=None):
    # Inicializa o processo
    rclpy.init(args=args)
    
    # Controi o nó
    node = Node('no_simples')

    # Define o nível do logger
    #logger = node.get_logger()
    #logger.set_level(LoggingSeverity.DEBUG)

    # Algumas impressões e exemplos de uso do logger
    node.get_logger().info('Parabéns, você rodou o seu primeiro nó!')   
    
    
    # Destroi o nó 
    node.destroy_node()

    # Finaliza o processo
    rclpy.shutdown()


if __name__ == '__main__':
    main()    


