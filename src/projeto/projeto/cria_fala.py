# pip install gTTS
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from std_msgs.msg import String

from gtts import gTTS
tts = gTTS('Olá, eu sou um robô! Meu nome é Maria. Como posso te ajudar?', lang ="pt")
tts.save('hello.mp3')

# pip install python-vlc
import vlc
p = vlc.MediaPlayer("hello.mp3")
p.play()



class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):

        # Aqui é definido o nome do nó
        super().__init__('Cria_fala')
        qos_profile = QoSProfile(depth=10, reliability = QoSReliabilityPolicy.BEST_EFFORT)
        self.get_logger().info('Criando as falas')
        self.subscription = self.create_subscription(String,'verbal',self.listener_callback,qos_profile )
       
    # Aqui o nó é executado no ROS
    def run(self):

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    # função de callback que lê a mensagem
    def listener_callback(self, msg):
        self.get_logger().info('Mensagem publicada: "%s"' % msg.data)

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Finalizando o nó! Tchau, tchau...')


# Função principal
def main(args=None):
    rclpy.init(args=args)
    node = MeuNo()
    try:
        node.run()
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
   
if __name__ == '__main__':
    main()    
