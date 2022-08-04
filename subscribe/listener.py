import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import test


broker =  'broker.emqx.io'
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

    # write subscribe topic on on_connect
    # if we lose connect or re-connect
    # will re-subscribe
    client.subscribe("direction")

def on_message(client, userdata, msg):
    print(msg.topic+ " "+ msg.payload.decode('utf-8'))
    
    if msg.payload.decode('utf-8') == 'forward' :
        print('1')
        test.MoveForward()
        print('1.1')

    if msg.payload.decode('utf-8') == 'back' :
        print('2')
        test.MoveBack()
        print('2.1')

    if msg.payload.decode('utf-8') == 'left' :
        print('3')
        test.MoveLeft()
        print('3.1')

    if msg.payload.decode('utf-8') == 'right' :
        print('4')
        test.MoveRight()
        print('4.1')


# set connection and initialize
client = mqtt.Client()

# set connection action
client.on_connect = on_connect

# set recieve action
client.on_message = on_message

# set login username and password
#client.username_pw_set("try", "xxxx")

# set connection information (ip, port, connect time)

client.connect(broker, 1883)
print("connected");
# start connect
# it also can use the other loop function ot link
client.loop_forever()

