import bvh
import cv2

def bvh_convert(filename):
    # Load the BVH file
    with open(filename, "r") as f:
        mocap = bvh.Bvh(f.read())

    # Get the joint names
    joint_names = mocap.get_joints_names()

    # Create dictionary for all data
    data_info = {}

    # Create dictionary for each frame
    joints_info_per_frame = {}

    # For each frame add the joint data to the joints_info_per_frame dictionary 
    # and add that dictionary to the data_info dictionary, clear the small dictionary and repeat
    # TAKES A LONG TIME (3min)
    for frame_index in range(mocap.nframes):
        for joint in joint_names:
            joints_info_per_frame[joint] = mocap.frame_joint_channels(frame_index,joint,['Xrotation', 'Yrotation', 'Zrotation'])

        data_info[frame_index+1] = joints_info_per_frame
        joints_info_per_frame = {}

    #print(data_info)
    # Frame 1, Hip Joint position and rotation
    #print(data_info[1]['Hips'])
    # Frame 2, LeftHandRing3, XPosition
    #print(data_info[2]['LeftHandRing3'][0])
    
    return data_info



