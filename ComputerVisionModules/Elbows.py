
import numpy as np

class Elbows():

    def __init__(self):
        super().__init__()
        self.elbows = ["left_elbow", "right_elbow"]
        self.elbows_output = {
          "Left": {
            "Roll": {
              "Degree": 180,
              "Radian": np.pi
            }
          },
          "Right": {
            "Roll": {
              "Degree": 180,
              "Radian": np.pi
            }
          }
        }
    
    def normalize(self, val, min_val, max_val):
      return (val - min_val) / (max_val - min_val)

    def denormalize(self, val, min_val, max_val):
        return val * (max_val - min_val) + min_val


    def get_elbows_info(self, rightarm, rightforearm, leftarm, leftforearm):

      for elbow in self.elbows:
        
        if elbow == "left_elbow":
          left_elbow = [a - b for a, b in zip(leftarm, leftforearm)]
          left_elbow_roll = self. normalize(left_elbow[0], 90, -90)
          left_elbow_roll = self.denormalize(left_elbow_roll, -88.5, 2)
          
          self.elbows_output["Left"]["Roll"] = {"Degree": -(left_elbow_roll), "Radian": np.deg2rad(-(left_elbow_roll))}
        
        if elbow == "right_elbow":

          right_elbow = [a - b for a, b in zip(rightarm, rightforearm)]
          right_elbow_roll = self.normalize(right_elbow[0], -90, 90)
          right_elbow_roll = self.denormalize(right_elbow_roll, -2, 88.5)

          self.elbows_output["Right"]["Roll"] = {"Degree": right_elbow_roll, "Radian": np.deg2rad(right_elbow_roll)}

      return self.elbows_output
