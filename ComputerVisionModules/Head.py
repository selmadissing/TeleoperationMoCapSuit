import numpy as np


def get_head_positions(angles):
    output = {
        "Pitch" : {
            "Degree" : 0 ,
            "Radian" : 0
        } ,
        "Yaw" : {
            "Degree" : 0 ,
            "Radian" : 0
        }
    }

    head_pitch = angles[0]
    head_yaw = angles[1]

    head_pitch_degree, head_pitch_radian = head_pitch, np.deg2rad(head_pitch)
    head_yaw_degree, head_yaw_radian = head_yaw, np.deg2rad(head_yaw)

    output["Pitch"]["Degree"] = head_pitch_degree
    output["Pitch"]["Radian"] = head_pitch_radian
    output["Yaw"]["Degree"] = head_yaw_degree
    output["Yaw"]["Radian"] = head_yaw_radian

    return output

