import json
from agent import Agent
import time

# Dict for mapping joints onto robot
def get_joint_values(data, joint_name, angle_type="Radian"):

    angles = data['Angles']
    status = data['Status'] 

    joint_angle_dict = {
        "HeadPitch": angles['Head']['Pitch'][angle_type], 
        "HeadYaw": angles['Head']['Yaw'][angle_type], 
        
        "LShoulderRoll": angles["Shoulders"]["Left"]["Roll"][angle_type], 
        "LShoulderPitch": angles["Shoulders"]["Left"]["Pitch"][angle_type], 
        
        "RShoulderRoll": angles["Shoulders"]["Right"]["Roll"][angle_type], 
        "RShoulderPitch": angles["Shoulders"]["Right"]["Pitch"][angle_type], 
        
        "LElbowRoll": angles["Elbows"]["Left"]["Roll"][angle_type], 
        "RElbowRoll": angles["Elbows"]["Right"]["Roll"][angle_type], 
        
        "LHand": status["Hands"]["Left"]["is_open"],
        "RHand": status["Hands"]["Right"]["is_open"]}

        # "LHipRoll" : angles["Hips"]["Left"]["Roll"][angle_type],
        # "RHipRoll" : angles["Hips"]["Right"]["Roll"][angle_type]
        
    return joint_angle_dict[joint_name]


def get_json_file(path):
    try:
        with open(path,"r",encoding="utf-8") as dfile :

            return json.load(dfile)
    except:
        print("Couldn't read JSON file !!!!!!!!!!!!!!")
        pass


def scale_radian(value, joint_name):
    # Dict for getting max and min angles
    dictionaryAngles = {
        "HeadYaw" : {
            "Min" : -2.0857,
            "Max" : 2.0857
        },
        "HeadPitch" : {
            "Min" : -0.6720,
            "Max" : 0.5149
        },
        "LShoulderRoll" :{
            "Min" : -0.3142,
            "Max" : 1.3265
        },
        "LShoulderPitch" : {
            "Min" : -2.0857,
            "Max" : 2.0857
        },
        "RShoulderRoll" : {
            "Min" : -1.3265,
            "Max" : 0.3142
        },
        "RShoulderPitch" : {
            "Min" : -2.0857,
            "Max" : 2.0857
        },
        "LElbowYaw" : {
            "Min" : -2.0857,
            "Max" : 2.0857
        },
        "LElbowRoll" : {
            "Min" : -1.5446,
            "Max" : -0.0349
        },
        "LWristYaw" : {
            "Min" : -1.8238,
            "Max" : 1.8238
        },
        "RElbowYaw" : {
            "Min" : -2.0857,
            "Max" : 2.0857
        },
        "RElbowRoll" : {
            "Min" : 0.0349,
            "Max": 1.5446
        },
        "RWristYaw" : {
            "Min" : -1.8238,
            "Max" : 1.8238
        },
        "LHipRoll" : {
            "Min" : -0.379472,
            "Max" : 0.790477,
        },    
        "RHipRoll" : {
            "Min" : -0.790477,
            "Max" : 0.379472,
        },
        "LHand" : {
            "Min" : 0.0,
            "Max" : 1.0
        },
        "RHand" : {
            "Min" : 0.0,
            "Max" : 1.0
        }
    }

    if value > dictionaryAngles[joint_name]["Max"]:
        value = dictionaryAngles[joint_name]["Max"]
    if value < dictionaryAngles[joint_name]["Min"]:
        value = dictionaryAngles[joint_name]["Min"]
    
    return value


def run_simulation():
    
    nao_angles_list = []
    try: 
        data = get_json_file("../output.json")
        #print(data)

    except:
        print("Couldn't read angle from JSON file.")
        
    
    joint_names = ["LShoulderRoll", "LShoulderPitch","RShoulderRoll","RShoulderPitch",
    "HeadYaw","HeadPitch", "LElbowRoll", "RElbowRoll", "LHand", "RHand"]

    for i in range(len(joint_names)):
        try:
            radian = get_joint_values(data, joint_names[i])
            #print(joint_names[i], radian)
        except:
            print(joint_names[i],"error but program continues")
            continue

        if radian == None:
            continue
        
        if joint_names[i] == "LShoulderPitch" or joint_names[i] == "RShoulderPitch":
            radian = 1.5708 - radian
        
        try:
            radian = scale_radian(radian,joint_names[i])
        except:
            print("could not be scaled")

        if radian == None:
            radian = 0
        try:
            #print(joint_names[i], radian)
            nao_angles_list.append(radian)
        except:
            print("could not set angle")
    print(nao_angles_list)
    i = 0
    # action input is in the form of 1d np.array of shape (action_dimension,)
    if len(nao_angles_list) == 10:
        print(nao_angles_list)
        agent.take_action(nao_angles_list, vel=0.2, role=None) 

    else:
        pass
    time.sleep(0.2)
    #return nao_angles_list

agent = Agent()
agent.set_stiffness(1.0)

try:
    while True:
        run_simulation() 
        
except KeyboardInterrupt:
    print("Program stopped by the user.")
