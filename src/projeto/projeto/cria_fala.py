from gtts import gTTS
import vlc
import whisper
import keyboard
import time

tts = gTTS('Olá, sou Matheus, Como posso te ajudar?', lang ="pt")
tts.save('hello.mp3')


p = vlc.MediaPlayer("hello.mp3")
p.play()

while true:
    try:
        print("Aguardando entrada")
        keyboard.wait('space')
        time.sleep(0.2)
        model = whisper.load_model("small")
        result = model.transcribe("gravado.mp3", fp16=False)
        fala = result["text"]
        if fala == "Gostaria de uma mesa":
            tts = gTTS('Claro, tem alguma preferência de local?', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

        if fala == "Já tenho reserva":
            tts = gTTS('Me diga seu nome por gentileza que vou guia-lós até a mesa', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

        if fala == "Gostaria de fazer um pedido":
            tts = gTTS('Beleza, me diga os items que já vou envia-los para a cozinha', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

            time.sleep(5)

            tts = gTTS('Seu pedido foi anotado, só aguardar que assim que estiver pronto eu trago pra vocês', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

        if fala == "Eu queria minha conta por favor":
            tts = gTTS('Certinho, vou pegar no sistema e já fechamos a sua conta', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

            time.sleep(5)

            tts = gTTS('Muito obrigado pela sua preferência, vou acompanhar vocês até a porta', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

        if fala == "Onde fica o banheiro?":
            tts = gTTS('O banheiro fica a direita nos fundos do restaurante', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()
        
        if fala == "Tá demorando muito meu pedido, o que que está acontecendo?":
            tts = gTTS('Mil desculpas a demora, vou verificar junto da cozinha e trago uma atualização para você', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()
        
        if fala == "Como você funciona?":
            tts = gTTS('Sou um robô para auxilio de restaurantes, tenho uma série de sensores e atuadores para ajudar em minha segurança e navegação, pode me perguntar qualquer coisa referente ao restaurante que eu te ajudo', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()
        
        if fala == "Pode devolver meu pedido até o chefe, está cru a comida":
            tts = gTTS('Perdão pelo transtorto, vou trazer outro pedido pra você', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()

            time.sleep (5)

            tts = gTTS('Chefe, poderia por gentileza refazer esse pedido, o cliente reclamou de estar cru', lang ="pt")
            tts.save('resposta.mp3')

            p = vlc.MediaPlayer("resposta.mp3")
            p.play()
    except:
        break

