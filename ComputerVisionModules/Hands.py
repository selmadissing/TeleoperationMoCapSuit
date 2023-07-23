

def get_hand_status(rightIndex, rightMiddle, leftIndex, leftMiddle):
    output = {
        "Left" : {
            "is_open" : False
        } ,
        "Right" : {
            "is_open" : False
        }
    }
    # I assume the hand is closed when the index finger and middle finger are bent 

    # The values were taken from looking at the motion data
    if rightIndex[2] > 47 and rightMiddle[2] > -10:
       output["Right"]["is_open"] = 0
    else:
       output["Right"]["is_open"] = 1
    
    if leftIndex[2] < -23 and leftMiddle[2] < -37:
       output["Left"]["is_open"] = 0
    else:
       output["Left"]["is_open"] = 1


    return output