# DIIC PROJECT

A maneira mais simples de trocar mensagens entre o raspbery e os arduinos é com uma pool do género Publish/Subscriber,
o Raspberry é o unico publisher e cada arduino é um subscriber (desta forma adicionar mais arduinos nao é um problema).

O raspbery faz ping, analisa o output e envia o resultado pa pool (verde, amarelo, vermelho ou nada..)

Os arduinos recebem a mensagem (se tiverem a subscrever a pool) e alteram a cor do led dependendo da mensagem recebida.

Source: https://www.hackster.io/ruchir1674/raspberry-pi-talking-to-esp8266-using-mqtt-ed9037

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

ARDUINO_SIDE

Codigo na pasta arduino_side.

basta alterar as variaveis iniciais com o nome da rede, pass respectiva e com o ip do raspberrypi, que em principio sera 
sempre 192.168.1.100 (alterei o dhcpconfig para ter sempre este ip estatico, em minha casa funciona bem mas pode ser que 
de merda no tagus)

Quando tivermos mais do que um arduino ligado a pool cada um vai ter de ter um username e uma pass mas logo tratamos desse caso.

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

RASPBERRY_SIDE

ligar por ssh (com o programa PuTTy por exemplo)

ip: 192.168.1.100

username: pi

password: diic


no raspbery ainda so temos um ficheiro python que faz ping a um determinado ip 
para executar:

python ping.py <ip_address>


also, instalei todas as bibliotecas e packages necessarias para este ser um publisher
se executarem no terminal:

mosquitto_pub -h raspberrypi -t "/leds/esp8266" -m "ON"

todos os arduinos subscritores recebem a string "ON",
neste caso, -h e o publisher/source
            -t e o canal que os arduinos subscrevem
            -m a mensagem enviada

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

TODO LIST:

-falta montar o led rgd no arduino e reconhece-lo no codigo

-alterar a cor do led dependendo da mendagem recebida pelo raspbery (basta procurar o comment TODO no codigo do arduino pa saberem onde implementar isto)

-alterar o script python do raspbery para enviar mensagens aos subscritores dependendo do resultado do ping




