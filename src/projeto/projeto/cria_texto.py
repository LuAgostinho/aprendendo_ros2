# sudo apt update && sudo apt install ffmpeg
# pip install openai-whisper
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import whisper



class MeuNo(Node):

    # Contrutor do nó
    def __init__(self):

        # Aqui é definido o nome do nó
        super().__init__('cria_texto')

        self.get_logger().info('Publicando texto escutado!')
        self.publisher = self.create_publisher(String, 'verbal', 10)

    # Aqui o nó é executado no ROS
    def run(self):


        self.get_logger().info('Publicando mensagem a cada um segundo!')
        model = whisper.load_model("base")
        self.result = model.transcribe("hello.mp3", fp16=False)
        timer = self.create_timer(2, self.talker_callback)
        

        # Executa uma iteração do loop de processamento de mensagens.
        rclpy.spin(self)

    # funcção de callback que publica a mensagem
    def talker_callback(self):
        if(self.result != NULL):
            msg = String()
            msg.data = self.result
            self.publisher.publish(msg)
        else:
            pass

    # Destrutor do nó
    def __del__(self):
        self.get_logger().info('Parando de detectar audio')


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
