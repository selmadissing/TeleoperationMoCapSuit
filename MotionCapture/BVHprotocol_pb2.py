# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BVHprotocol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x42VHprotocol.proto\x12\tAxisPlugs\"-\n\nBVH_VECTOR\x12\t\n\x01X\x18\x01 \x02(\x02\x12\t\n\x01Y\x18\x02 \x02(\x02\x12\t\n\x01Z\x18\x03 \x02(\x02\"\xa7\x02\n\x08\x42VH_JOIN\x12\x10\n\x08joinName\x18\x01 \x02(\t\x12-\n\x08\x43hannels\x18\x02 \x03(\x0e\x32\x1b.AxisPlugs.BVH_JOIN.Channel\x12%\n\x06Offset\x18\x03 \x02(\x0b\x32\x15.AxisPlugs.BVH_VECTOR\x12&\n\x07\x45ndSite\x18\x04 \x01(\x0b\x32\x15.AxisPlugs.BVH_VECTOR\x12&\n\tChildJoin\x18\x05 \x03(\x0b\x32\x13.AxisPlugs.BVH_JOIN\"c\n\x07\x43hannel\x12\r\n\tXposition\x10\x00\x12\r\n\tYposition\x10\x01\x12\r\n\tZposition\x10\x02\x12\r\n\tXrotation\x10\x03\x12\r\n\tYrotation\x10\x04\x12\r\n\tZrotation\x10\x05\"D\n\tBVH_FRAME\x12\x12\n\nMotionData\x18\x01 \x03(\x02\x12\x10\n\x08\x41\x63torTag\x18\x02 \x01(\r\x12\x11\n\tActorName\x18\x03 \x01(\t\"X\n\nBVH_HEADER\x12%\n\x08RootJoin\x18\x01 \x02(\x0b\x32\x13.AxisPlugs.BVH_JOIN\x12\x10\n\x08\x41\x63torTag\x18\x02 \x01(\r\x12\x11\n\tActorName\x18\x03 \x01(\t\"m\n\x0eTAG_MAP_STRING\x12/\n\x03Map\x18\x01 \x03(\x0b\x32\".AxisPlugs.TAG_MAP_STRING.MapEntry\x1a*\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\rERROR_MESSAGE\x12\x11\n\tErrorCode\x18\x01 \x02(\r\x12\x10\n\x08\x45rrorMsg\x18\x02 \x02(\t\"\xeb\x02\n\x07\x43OMMAND\x12/\n\x07\x43ontent\x18\x01 \x02(\x0e\x32\x1e.AxisPlugs.COMMAND.CommandType\x12\x10\n\x08\x41\x63torTag\x18\x02 \x01(\r\x12-\n\nActorsList\x18\x03 \x01(\x0b\x32\x19.AxisPlugs.TAG_MAP_STRING\x12*\n\x08\x45rrorMsg\x18\x04 \x01(\x0b\x32\x18.AxisPlugs.ERROR_MESSAGE\"\xc1\x01\n\x0b\x43ommandType\x12\x18\n\x14Notify_Characterised\x10\x01\x12\x1a\n\x16Notify_Uncharacterised\x10\x02\x12\x15\n\x11Notify_ActorsList\x10\x03\x12\x10\n\x0cNotify_Error\x10\x05\x12\x1c\n\x18\x43ommand_Query_BVH_Header\x10\x06\x12\x1b\n\x17\x43ommand_Query_ActorList\x10\x07\x12\x18\n\x14\x43ommand_ZeroOutActor\x10\x08\"\x91\x02\n\x13\x41XIS_PLUGIN_MESSAGE\x12;\n\x07Message\x18\x01 \x02(\x0e\x32*.AxisPlugs.AXIS_PLUGIN_MESSAGE.MessageType\x12\'\n\x06Header\x18\x02 \x01(\x0b\x32\x15.AxisPlugs.BVH_HEADERH\x00\x12%\n\x05\x46rame\x18\x03 \x01(\x0b\x32\x14.AxisPlugs.BVH_FRAMEH\x00\x12%\n\x07\x43ommand\x18\x04 \x01(\x0b\x32\x12.AxisPlugs.COMMANDH\x00\";\n\x0bMessageType\x12\x0b\n\x07\x43OMMAND\x10\x00\x12\x0f\n\x0bHEADER_DATA\x10\x01\x12\x0e\n\nFRAME_DATA\x10\x02\x42\t\n\x07\x43ontentB\x05H\x01\xf8\x01\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BVHprotocol_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001\370\001\000'
  _TAG_MAP_STRING_MAPENTRY._options = None
  _TAG_MAP_STRING_MAPENTRY._serialized_options = b'8\001'
  _BVH_VECTOR._serialized_start=32
  _BVH_VECTOR._serialized_end=77
  _BVH_JOIN._serialized_start=80
  _BVH_JOIN._serialized_end=375
  _BVH_JOIN_CHANNEL._serialized_start=276
  _BVH_JOIN_CHANNEL._serialized_end=375
  _BVH_FRAME._serialized_start=377
  _BVH_FRAME._serialized_end=445
  _BVH_HEADER._serialized_start=447
  _BVH_HEADER._serialized_end=535
  _TAG_MAP_STRING._serialized_start=537
  _TAG_MAP_STRING._serialized_end=646
  _TAG_MAP_STRING_MAPENTRY._serialized_start=604
  _TAG_MAP_STRING_MAPENTRY._serialized_end=646
  _ERROR_MESSAGE._serialized_start=648
  _ERROR_MESSAGE._serialized_end=700
  _COMMAND._serialized_start=703
  _COMMAND._serialized_end=1066
  _COMMAND_COMMANDTYPE._serialized_start=873
  _COMMAND_COMMANDTYPE._serialized_end=1066
  _AXIS_PLUGIN_MESSAGE._serialized_start=1069
  _AXIS_PLUGIN_MESSAGE._serialized_end=1342
  _AXIS_PLUGIN_MESSAGE_MESSAGETYPE._serialized_start=1272
  _AXIS_PLUGIN_MESSAGE_MESSAGETYPE._serialized_end=1331
# @@protoc_insertion_point(module_scope)