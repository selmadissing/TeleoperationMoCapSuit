from ComputerVisionModules import computerVision
from MotionCapture.bvh_convert import bvh_convert
from MotionCapture.SocketAxisNeuron import socket_to_dictionary
import json
import time

def get_json_file(path):
    try:
        with open(path,"r",encoding="utf-8") as dfile :
            return json.load(dfile)
    except:
        print("Couldn't read JSON file !!!!!!!!!!!!!!")
        pass


####### !!!! USE IF UTILISING RECORDED MOTION DATA !!!! #######
# dictionary = bvh_convert("testing_motion.bvh")
# print("converted")
# with open('./dictionary.json', 'w') as file:
#     json.dump(dictionary, file)

# data = get_json_file("./dictionary.json")
###############################################################


frame = 1

while True:
    print(frame)
    dictionary = socket_to_dictionary('192.168.0.244', 7005)
    #print(dictionary)
    computerVision.run_computer_vision(dictionary)
    frame +=1 
    time.sleep(0.2)