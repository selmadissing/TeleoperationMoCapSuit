from naoqi import ALProxy
import time

nao_ip = "192.168.0.183"  # Replace with your NAO robot's IP
nao_port = 9559  # Replace with your NAO robot's port

motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
postureProxy = ALProxy("ALRobotPosture", nao_ip, nao_port)


isEnabled = True
motion_proxy.wbEnable(isEnabled)

# !!! TASK 1 !!!
def task1():
    # Arms to the side
    joint_names = ["LShoulderRoll", "RShoulderRoll"]
    target_angles = [1.0, -1.0]
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Arms up
    joint_names = ["LShoulderPitch", "RShoulderPitch", "LShoulderRoll", "RShoulderRoll"]
    target_angles = [-1.0, -1.0, 0, 0]  # Adjust these values based on your specific robot
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Arms down
    joint_names = ["LShoulderPitch", "RShoulderPitch"]
    target_angles = [1.5, 1.5]  # Adjust these values based on your specific robot
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! TASK 2 !!!
def task2():
    # Arms forward
    joint_names = ["LShoulderPitch", "RShoulderPitch", "LShoulderRoll", "RShoulderRoll"]
    target_angles = [0, 0, 0, 0]
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Arms up
    joint_names = ["LShoulderPitch", "RShoulderPitch", "LShoulderRoll", "RShoulderRoll"]
    target_angles = [-1.0, -1.0, 0, 0]  # Adjust these values based on your specific robot
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Arms down
    joint_names = ["LShoulderPitch", "RShoulderPitch"]
    target_angles = [1.5, 1.5]  
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)
    
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! TASK 3 !!!
def task3():
    # Head to the left
    motion_proxy.angleInterpolation("HeadYaw", -1.0, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Head to the right
    motion_proxy.angleInterpolation("HeadYaw", 1.0, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Head center
    motion_proxy.angleInterpolation("HeadYaw", 0, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Head up
    motion_proxy.angleInterpolation("HeadPitch", -0.6, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Head down
    motion_proxy.angleInterpolation("HeadPitch", 0.6, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Head center
    motion_proxy.angleInterpolation("HeadPitch", 0, 1.0, True)
    time.sleep(1)  # pause execution for 1 second
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# !!! TASK 4 !!!
def task4():
    # Elbow flexion (bend)
    joint_names = ["LElbowRoll", "RElbowRoll"]
    target_angles = [-1.5446, 1.5446]  # Maximum bend within the safe range
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Elbow extension (straighten)
    target_angles = [-0.0349, 0.0349]  # Minimum bend within the safe range
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)

    

# !!! TASK 5 !!!
def task5():
    # Arms to the side
    joint_names_shoulder = ["LShoulderRoll", "RShoulderRoll"]
    target_angles = [1.0, -1.0]
    motion_proxy.angleInterpolation(joint_names_shoulder, target_angles, 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Elbows bend
    joint_names_elbow = ["LElbowRoll", "RElbowRoll"]
    motion_proxy.angleInterpolation(joint_names_elbow, [-1.5, 1.5], 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Elbows straighten
    motion_proxy.angleInterpolation(joint_names_elbow, [0, 0], 1.0, True)
    time.sleep(1)  # pause execution for 1 second

    # Arms down
    joint_names = ["LShoulderPitch", "RShoulderPitch"]
    target_angles = [1.5, 1.5]  # Adjust these values based on your specific robot
    motion_proxy.angleInterpolation(joint_names, target_angles, 1.0, True)

    # Disable the whole body motion
    isEnabled = False
    motion_proxy.wbEnable(isEnabled)


# Play task (movement)
while True:
    task5()
