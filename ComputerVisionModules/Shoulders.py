import numpy as np

class Shoulders() :

    def __init__(self) :
        super().__init__()
        self.shoulders = ["left_shoulder" , "right_shoulder"]
        self.shoulders_output = {
            "Left" : {
                "Roll" : {
                    "Degree" : 0 ,
                    "Radian" : 0
                } ,
                "Pitch" : {
                    "Degree" : 0 ,
                    "Radian" : 0
                }
            },
            "Right" : {
                "Roll" : {
                    "Degree" : 0 ,
                    "Radian" : 0
                } ,
                "Pitch" : {
                    "Degree" : 0 ,
                    "Radian" : 0
                }
            }
        }
    
    # Function to normalize values
    def normalize(self, val, min_val, max_val):
        return (val - min_val) / (max_val - min_val)
    

    # Function to denormalize values (NAO's range of motion)
    def denormalize(self, val, min_val, max_val):
        return val * (max_val - min_val) + min_val

    def get_shoulders_info(self, joint_info_left, joint_info_right) :

        # NAO left shoulder roll range: -18 to 76
        # NAO left shoulder pitch range: -119.5 to 119.5
        # NAO right shoulder roll range: -76 to 18
        # NAO right shoulder pitch range: -119.5 to 119.5


        for shoulder in self.shoulders:

            if shoulder == "left_shoulder":

                left_roll = self.normalize(joint_info_left[2], -30, 30)
                left_roll_nao = self.denormalize(left_roll, -18, 76)
                left_pitch = self.normalize(joint_info_left[1], -30, 30)
                left_pitch_nao = self.denormalize(left_pitch, -119.5, 119.5)

                self.shoulders_output["Left"]["Roll"] = {'Degree': left_roll_nao, 'Radian': np.deg2rad(left_roll_nao)}
                self.shoulders_output["Left"]["Pitch"] = {'Degree': -left_pitch_nao, 'Radian': np.deg2rad(-left_pitch_nao)}

            if shoulder == "right_shoulder":

                right_roll = self.normalize(joint_info_right[2], -30, 30)
                right_roll = self.denormalize(right_roll, -76, 18)
                right_pitch = self.normalize(joint_info_right[1], -30, 30)
                right_pitch = self.denormalize(right_pitch, -119.5, 119.5)

                
                self.shoulders_output["Right"]["Roll"] = {'Degree': right_roll, 'Radian': np.deg2rad(right_roll)}
                self.shoulders_output["Right"]["Pitch"] = {'Degree': right_pitch, 'Radian': np.deg2rad(right_pitch)}


        return self.shoulders_output
