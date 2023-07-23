from naoqi import ALProxy
import time

nao_ip = "192.168.0.183"  # Replace with your NAO robot's IP
nao_port = 9559  # Replace with your NAO robot's port

motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
postureProxy = ALProxy("ALRobotPosture", nao_ip, nao_port)
isEnabled = True
motion_proxy.wbEnable(isEnabled)

# !!! POSITION 1 !!!
def position1():
    # Arms to the side
    joint_names = ["LShoulderRoll", "RShoulderRoll"]
    target_angles = [1.3, -1.3]
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second
    
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! POSITION 2 !!!
def position2():
    # Arms forward
    joint_names = ["LShoulderPitch", "RShoulderPitch", "LShoulderRoll", "RShoulderRoll"]
    target_angles = [0, 0, 0, 0]
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second
    
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! POSITION 3 !!!
def position3():
    # Head to the left
    motion_proxy.angleInterpolation("HeadYaw", -1.0, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! POSITION 4 !!!
def position4():
    # Head down
    motion_proxy.angleInterpolation("HeadPitch", 0.5, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    isEnabled = False
    motion_proxy.wbEnable(isEnabled)

    
# Play task (movement)
while True:
    position4()
