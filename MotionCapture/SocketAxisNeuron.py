import socket
from BVHprotocol_pb2 import AXIS_PLUGIN_MESSAGE
import struct
import gzip
import io
import sys
import time

keys = ["Hips", "RightUpLeg", "RightLeg", "RightFoot", "LeftUpLeg", "LeftLeg", "LeftFoot", "Spine", "Spine1", "Spine2", "Spine3", "Neck", "Head", "RightShoulder", "RightArm", "RightForeArm", "RightHand", "RightHandThumb1", "RightHandThumb2", "RightHandThumb3", "RightInHandIndex", "RightHandIndex1", "RightHandIndex2", "RightHandIndex3", "RightInHandMiddle", "RightHandMiddle1", "RightHandMiddle2", "RightHandMiddle3", "RightInHandRing", "RightHandRing1", "RightHandRing2", "RightHandRing3", "RightInHandPinky", "RightHandPinky1", "RightHandPinky2", "RightHandPinky3", "LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand", "LeftHandThumb1", "LeftHandThumb2", "LeftHandThumb3", "LeftInHandIndex", "LeftHandIndex1", "LeftHandIndex2", "LeftHandIndex3", "LeftInHandMiddle", "LeftHandMiddle1", "LeftHandMiddle2", "LeftHandMiddle3", "LeftInHandRing", "LeftHandRing1", "LeftHandRing2", "LeftHandRing3", "LeftInHandPinky", "LeftHandPinky1", "LeftHandPinky2", "LeftHandPinky3"]

def handle_command(command):
    #print('Command Received')
    #print('Command Type:', command.Content)
    #print('Actor Tag:', command.ActorTag)
    if command.ErrorMsg:
        print(command.ErrorMsg.ErrorMsg)

def handle_header_data(header):
    print('Header Data Received')
    print('Root Join Name:', header.RootJoin.joinName)
    #print('Actor Tag:', header.ActorTag)
    #print('Actor Name:', header.ActorName)
    #for child in header.RootJoin.ChildJoin:
        #print('Child joint:', child.joinName)

def handle_frame_data(frame):
    #print('Frame Data Received')
    #print('Motion Data:', frame.MotionData)
    rounded = [round(num, 6) for num in frame.MotionData]
    output_dict = {keys[i]: rounded[i*3+3: (i+1)*3+3] for i in range(59)}
    #print('Dictionary:', output_dict)
    #print('Actor Tag:', frame.ActorTag)
    #print('Actor Name:', frame.ActorName)
    return output_dict


def socket_to_dictionary(host, port):
    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    try:
        while True:
            #time.sleep(2.0)
            # Read the header (8 bytes for start mark and data length)
            header_data = s.recv(8)

            # If we didn't get any data, the connection was closed
            if not header_data:
                break

            # Unpack the header
            start_mark, data_length = struct.unpack('<II', header_data)

            # Read the payload
            payload = s.recv(data_length)

            # If the start_mark is 0x43434343, the data is packed
            if start_mark == 0x43434343:
                # Decompress the payload
                payload_io = io.BytesIO(payload)
                with gzip.GzipFile(fileobj=payload_io) as f:
                    payload = f.read()

            # At this point, payload should be the uncompressed data
            # Parse it as a protobuf message
            message = AXIS_PLUGIN_MESSAGE()
            message.ParseFromString(payload)

            # Handle the message based on its type
            if message.Message == AXIS_PLUGIN_MESSAGE.COMMAND:
                handle_command(message.Command)

            elif message.Message == AXIS_PLUGIN_MESSAGE.HEADER_DATA:
                handle_header_data(message.Header)

            elif message.Message == AXIS_PLUGIN_MESSAGE.FRAME_DATA:
                return handle_frame_data(message.Frame)

    except KeyboardInterrupt:
        print("\nKeyboard interruption. Closing the socket!")
        s.close()
        sys.exit(0)
    
   
#print(socket_to_dictionary('192.168.0.244', 7005))


    #192.168.2.244
