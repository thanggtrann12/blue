
import paho.mqtt.client as mqtt
import time
import json
import threading
import logging
from mqtt.functions.teaminfo import *
from mqtt.config.mqttBrokerInfo import *
logging.basicConfig(level=logging.INFO)



clients=[
{"broker":"driver.cloudmqtt.com","port":18675,"name":"BlueTeamClient","sub_topic":"BlueTeam"},

{"broker":"driver.cloudmqtt.com","port":18675,"name":"BlueTeamClient_response"}
]
blueTeamClient=len(clients)

def Connect(client,broker,port,keepalive,run_forever=False):
    connflag=False
    delay=5
    badcount=0
    while not connflag:
        logging.info("connecting to broker "+str(broker))
        time.sleep(delay)
        try:
            client.username_pw_set(username, password)
            client.connect(broker,port,keepalive)
            connflag=True

        except:
            client.badconnection_flag=True
            logging.info("connection failed "+str(badcount))
            badcount +=1
            if badcount>=3 and not run_forever: 
                return -1



                
    return 0
def wait_for(client,msgType,period=1,wait_time=10,running_loop=False):
    client.running_loop=running_loop #
    wcount=0  
    while True:
        if msgType=="CONNACK":
            if client.on_connect:
                if client.connected_flag:
                    return True
                if client.bad_connection_flag: #
                    return False
                
        if msgType=="SUBACK":
            if client.on_subscribe:
                if client.suback_flag:
                    return True
        if msgType=="MESSAGE":
            if client.on_message:
                if client.message_received_flag:
                    return True
        if msgType=="PUBACK":
            if client.on_publish:        
                if client.puback_flag:
                    return True
     
        if not client.running_loop:
            client.loop(.01) 
        time.sleep(period)
        wcount+=1
        if wcount>wait_time:
            print("return from wait loop taken too long")
            return False
    return True

def client_loop(client,broker,port,keepalive=60,loop_function=None,          loop_delay=1,run_forever=False):
    client.run_flag=True
    client.broker=broker
    print("running loop ")
    client.reconnect_delay_set(min_delay=1, max_delay=12)
      
    while client.run_flag: 
        if client.bad_connection_flag:
            break         
        if not client.connected_flag:
            print("Connecting to ",broker)
            if Connect(client,broker,port,keepalive,run_forever) !=-1:
                if not wait_for(client,"CONNACK"):
                   client.run_flag=False #break no connack
            else:#connect fails
                client.run_flag=False #break
                print("quitting loop for  broker ",broker)
        client.loop(0.01)
        if client.connected_flag and loop_function: #function to call
                loop_function(client,loop_delay) #call function
    time.sleep(1)
    print("disconnecting from",broker)
    if client.connected_flag:
        client.disconnect()
        client.connected_flag=False
    
def on_message(client, userdata, message):
   time.sleep(1)
   print("message",str(message.payload.decode("utf-8")), "received in topic", message.topic)
   if message.topic == "BlueTeam":
     if client.subscribe(message.payload.decode("utf-8")):
        print("subscribed to ",message.payload.decode("utf-8"))
        client.suback_flag=True
   if message.topic in teamCode:
      
      print("message ",str(message.payload.decode("utf-8")), "received in topic", message.topic)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        if client == clients[0]["client"]:
            print("connected OK")
            client.subscribe(clients[0]["sub_topic"])
            print("subscribed to ",clients[0]["sub_topic"])
        
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()  
def on_disconnect(client, userdata, rc):
   client.connected_flag=False 
def on_publish(client, userdata, mid):
   time.sleep(1)

def pub(client,loop_delay):
    pass

def Create_connections():
   for i in range(blueTeamClient):
      cname="client"+str(i)
      t=int(time.time())
      client_id =cname+str(t) #create unique client_id
      client = mqtt.Client(client_id)             #create new instance
      clients[i]["client"]=client 
      clients[i]["client_id"]=client_id
      clients[i]["cname"]=cname
      broker=clients[i]["broker"]
      port=clients[i]["port"]
      client.on_connect = on_connect
      client.on_disconnect = on_disconnect
      #client.on_publish = on_publish
      client.on_message = on_message
      t = threading.Thread(target=client_loop,args=(client,broker,port,60,pub))
      threads.append(t)
      t.start()


mqtt.Client.connected_flag=False #create flag in class
mqtt.Client.bad_connection_flag=False #create flag in class

threads=[]
no_threads=threading.active_count()





