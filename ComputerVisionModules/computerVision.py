from ComputerVisionModules import Shoulders, Elbows, Head, Hands
from ProgramOutputModule import OutputModule

shoulders = Shoulders.Shoulders()
elbows = Elbows.Elbows()
hands_module = Hands
program_output = OutputModule.Output()


def run_computer_vision(joints_for_frame):

    head_angle = Head.get_head_positions(joints_for_frame["Head"])
    program_output.output["Angles"]["Head"] = head_angle


    shoulders_angle = shoulders.get_shoulders_info(joints_for_frame["LeftShoulder"], 
                                                    joints_for_frame["RightShoulder"])
    program_output.output["Angles"]["Shoulders"] = shoulders_angle
   

    elbows_angle = elbows.get_elbows_info(joints_for_frame["RightArm"], 
                                            joints_for_frame["RightForeArm"], 
                                            joints_for_frame["LeftArm"], 
                                            joints_for_frame["LeftForeArm"])
    program_output.output["Angles"]["Elbows"] = elbows_angle


    hands_status = hands_module.get_hand_status(joints_for_frame["RightHandIndex1"], 
                                                joints_for_frame["RightHandMiddle1"], 
                                                joints_for_frame["LeftHandIndex1"], 
                                                joints_for_frame["LeftHandMiddle1"])
    program_output.output["Status"]["Hands"] = hands_status


    program_output.write_json_data("./output.json")
    return


