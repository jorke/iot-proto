# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FEP.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ApplicationManagement_pb2 as ApplicationManagement__pb2
import Model_pb2 as Model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='FEP.proto',
  package='org.totalgrid.reef.client.service.proto.FEP',
  syntax='proto2',
  serialized_options=b'\n\'org.totalgrid.reef.client.service.protoB\003FEP',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tFEP.proto\x12+org.totalgrid.reef.client.service.proto.FEP\x1a\x1b\x41pplicationManagement.proto\x1a\x0bModel.proto\"\xad\x01\n\x06IpPort\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x02(\t\x12\x0c\n\x04port\x18\x02 \x02(\r\x12N\n\x04mode\x18\x03 \x01(\x0e\x32\x38.org.totalgrid.reef.client.service.proto.FEP.IpPort.Mode:\x06SERVER\x12\x14\n\x07network\x18\x04 \x01(\t:\x03\x61ny\"\x1e\n\x04Mode\x12\n\n\x06\x43LIENT\x10\x01\x12\n\n\x06SERVER\x10\x02\"\x96\x03\n\nSerialPort\x12\x10\n\x08location\x18\x01 \x02(\t\x12\x11\n\tport_name\x18\x02 \x02(\t\x12\x17\n\tbaud_rate\x18\x03 \x01(\r:\x04\x39\x36\x30\x30\x12\x14\n\tstop_bits\x18\x04 \x01(\r:\x01\x31\x12\x14\n\tdata_bits\x18\x05 \x01(\r:\x01\x38\x12X\n\x06parity\x18\x06 \x01(\x0e\x32>.org.totalgrid.reef.client.service.proto.FEP.SerialPort.Parity:\x08PAR_NONE\x12U\n\x04\x66low\x18\x07 \x01(\x0e\x32<.org.totalgrid.reef.client.service.proto.FEP.SerialPort.Flow:\tFLOW_NONE\":\n\x04\x46low\x12\r\n\tFLOW_NONE\x10\x01\x12\x11\n\rFLOW_HARDWARE\x10\x02\x12\x10\n\x0c\x46LOW_XONXOFF\x10\x03\"1\n\x06Parity\x12\x0c\n\x08PAR_NONE\x10\x01\x12\x0c\n\x08PAR_EVEN\x10\x02\x12\x0b\n\x07PAR_ODD\x10\x03\"\xff\x02\n\x0b\x43ommChannel\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12?\n\x02ip\x18\x03 \x01(\x0b\x32\x33.org.totalgrid.reef.client.service.proto.FEP.IpPort\x12G\n\x06serial\x18\x04 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.FEP.SerialPort\x12M\n\x05state\x18\x05 \x01(\x0e\x32>.org.totalgrid.reef.client.service.proto.FEP.CommChannel.State\"B\n\x05State\x12\n\n\x06\x43LOSED\x10\x01\x12\x0b\n\x07OPENING\x10\x02\x12\x08\n\x04OPEN\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05\"2\n\x13\x43ommEndpointRouting\x12\x1b\n\x13service_routing_key\x18\x01 \x01(\t\"\xc9\x01\n\x11\x46rontEndProcessor\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x11\n\tprotocols\x18\x02 \x03(\t\x12Z\n\napp_config\x18\x03 \x01(\x0b\x32\x46.org.totalgrid.reef.client.service.proto.Application.ApplicationConfig\"5\n\x11\x45ndpointOwnership\x12\x0e\n\x06points\x18\x01 \x03(\t\x12\x10\n\x08\x63ommands\x18\x02 \x03(\t\"\xd2\x03\n\x08\x45ndpoint\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x45\n\x06\x65ntity\x18\x07 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x10\n\x08protocol\x18\x03 \x01(\t\x12\x14\n\x0c\x61utoAssigned\x18\t \x01(\x08\x12I\n\x07\x63hannel\x18\x04 \x01(\x0b\x32\x38.org.totalgrid.reef.client.service.proto.FEP.CommChannel\x12R\n\nownerships\x18\x06 \x01(\x0b\x32>.org.totalgrid.reef.client.service.proto.FEP.EndpointOwnership\x12O\n\x0c\x63onfig_files\x18\x05 \x03(\x0b\x32\x39.org.totalgrid.reef.client.service.proto.Model.ConfigFile\x12\x12\n\ndataSource\x18\x08 \x01(\x08\"\x91\x04\n\x12\x45ndpointConnection\x12\x41\n\x02id\x18\x01 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.ReefID\x12Q\n\tfront_end\x18\x02 \x01(\x0b\x32>.org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor\x12G\n\x08\x65ndpoint\x18\x03 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.FEP.Endpoint\x12T\n\x05state\x18\x04 \x01(\x0e\x32\x45.org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.State\x12Q\n\x07routing\x18\x05 \x01(\x0b\x32@.org.totalgrid.reef.client.service.proto.FEP.CommEndpointRouting\x12\x13\n\x0blast_update\x18\x07 \x01(\x04\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12\x0e\n\x06\x61\x63tive\x18\t \x01(\x08\"=\n\x05State\x12\x0c\n\x08\x43OMMS_UP\x10\x01\x12\x0e\n\nCOMMS_DOWN\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\x8c\x01\n\x15\x43ommandHandlerBinding\x12\\\n\x13\x65ndpoint_connection\x18\x01 \x01(\x0b\x32?.org.totalgrid.reef.client.service.proto.FEP.EndpointConnection\x12\x15\n\rcommand_queue\x18\x02 \x01(\tB.\n\'org.totalgrid.reef.client.service.protoB\x03\x46\x45P'
  ,
  dependencies=[ApplicationManagement__pb2.DESCRIPTOR,Model__pb2.DESCRIPTOR,])



_IPPORT_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLIENT', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVER', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=244,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_IPPORT_MODE)

_SERIALPORT_FLOW = _descriptor.EnumDescriptor(
  name='Flow',
  full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.Flow',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOW_NONE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOW_HARDWARE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOW_XONXOFF', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=574,
  serialized_end=632,
)
_sym_db.RegisterEnumDescriptor(_SERIALPORT_FLOW)

_SERIALPORT_PARITY = _descriptor.EnumDescriptor(
  name='Parity',
  full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.Parity',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAR_NONE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAR_EVEN', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAR_ODD', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=634,
  serialized_end=683,
)
_sym_db.RegisterEnumDescriptor(_SERIALPORT_PARITY)

_COMMCHANNEL_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPENING', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1003,
  serialized_end=1069,
)
_sym_db.RegisterEnumDescriptor(_COMMCHANNEL_STATE)

_ENDPOINTCONNECTION_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMMS_UP', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMS_DOWN', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2320,
  serialized_end=2381,
)
_sym_db.RegisterEnumDescriptor(_ENDPOINTCONNECTION_STATE)


_IPPORT = _descriptor.Descriptor(
  name='IpPort',
  full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort.address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort.port', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network', full_name='org.totalgrid.reef.client.service.proto.FEP.IpPort.network', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"any".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IPPORT_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=274,
)


_SERIALPORT = _descriptor.Descriptor(
  name='SerialPort',
  full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.location', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_name', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.port_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='baud_rate', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.baud_rate', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=9600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop_bits', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.stop_bits', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_bits', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.data_bits', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parity', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.parity', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow', full_name='org.totalgrid.reef.client.service.proto.FEP.SerialPort.flow', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERIALPORT_FLOW,
    _SERIALPORT_PARITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=683,
)


_COMMCHANNEL = _descriptor.Descriptor(
  name='CommChannel',
  full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.ip', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial', full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.serial', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='org.totalgrid.reef.client.service.proto.FEP.CommChannel.state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMCHANNEL_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=686,
  serialized_end=1069,
)


_COMMENDPOINTROUTING = _descriptor.Descriptor(
  name='CommEndpointRouting',
  full_name='org.totalgrid.reef.client.service.proto.FEP.CommEndpointRouting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_routing_key', full_name='org.totalgrid.reef.client.service.proto.FEP.CommEndpointRouting.service_routing_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1071,
  serialized_end=1121,
)


_FRONTENDPROCESSOR = _descriptor.Descriptor(
  name='FrontEndProcessor',
  full_name='org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocols', full_name='org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor.protocols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_config', full_name='org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor.app_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1124,
  serialized_end=1325,
)


_ENDPOINTOWNERSHIP = _descriptor.Descriptor(
  name='EndpointOwnership',
  full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointOwnership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointOwnership.points', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointOwnership.commands', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1327,
  serialized_end=1380,
)


_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.entity', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.protocol', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoAssigned', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.autoAssigned', index=4,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.channel', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ownerships', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.ownerships', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config_files', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.config_files', index=7,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='org.totalgrid.reef.client.service.proto.FEP.Endpoint.dataSource', index=8,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1383,
  serialized_end=1849,
)


_ENDPOINTCONNECTION = _descriptor.Descriptor(
  name='EndpointConnection',
  full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='front_end', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.front_end', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.endpoint', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routing', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.routing', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.last_update', index=5,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.enabled', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='org.totalgrid.reef.client.service.proto.FEP.EndpointConnection.active', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENDPOINTCONNECTION_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1852,
  serialized_end=2381,
)


_COMMANDHANDLERBINDING = _descriptor.Descriptor(
  name='CommandHandlerBinding',
  full_name='org.totalgrid.reef.client.service.proto.FEP.CommandHandlerBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint_connection', full_name='org.totalgrid.reef.client.service.proto.FEP.CommandHandlerBinding.endpoint_connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_queue', full_name='org.totalgrid.reef.client.service.proto.FEP.CommandHandlerBinding.command_queue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2384,
  serialized_end=2524,
)

_IPPORT.fields_by_name['mode'].enum_type = _IPPORT_MODE
_IPPORT_MODE.containing_type = _IPPORT
_SERIALPORT.fields_by_name['parity'].enum_type = _SERIALPORT_PARITY
_SERIALPORT.fields_by_name['flow'].enum_type = _SERIALPORT_FLOW
_SERIALPORT_FLOW.containing_type = _SERIALPORT
_SERIALPORT_PARITY.containing_type = _SERIALPORT
_COMMCHANNEL.fields_by_name['uuid'].message_type = Model__pb2._REEFUUID
_COMMCHANNEL.fields_by_name['ip'].message_type = _IPPORT
_COMMCHANNEL.fields_by_name['serial'].message_type = _SERIALPORT
_COMMCHANNEL.fields_by_name['state'].enum_type = _COMMCHANNEL_STATE
_COMMCHANNEL_STATE.containing_type = _COMMCHANNEL
_FRONTENDPROCESSOR.fields_by_name['uuid'].message_type = Model__pb2._REEFUUID
_FRONTENDPROCESSOR.fields_by_name['app_config'].message_type = ApplicationManagement__pb2._APPLICATIONCONFIG
_ENDPOINT.fields_by_name['uuid'].message_type = Model__pb2._REEFUUID
_ENDPOINT.fields_by_name['entity'].message_type = Model__pb2._ENTITY
_ENDPOINT.fields_by_name['channel'].message_type = _COMMCHANNEL
_ENDPOINT.fields_by_name['ownerships'].message_type = _ENDPOINTOWNERSHIP
_ENDPOINT.fields_by_name['config_files'].message_type = Model__pb2._CONFIGFILE
_ENDPOINTCONNECTION.fields_by_name['id'].message_type = Model__pb2._REEFID
_ENDPOINTCONNECTION.fields_by_name['front_end'].message_type = _FRONTENDPROCESSOR
_ENDPOINTCONNECTION.fields_by_name['endpoint'].message_type = _ENDPOINT
_ENDPOINTCONNECTION.fields_by_name['state'].enum_type = _ENDPOINTCONNECTION_STATE
_ENDPOINTCONNECTION.fields_by_name['routing'].message_type = _COMMENDPOINTROUTING
_ENDPOINTCONNECTION_STATE.containing_type = _ENDPOINTCONNECTION
_COMMANDHANDLERBINDING.fields_by_name['endpoint_connection'].message_type = _ENDPOINTCONNECTION
DESCRIPTOR.message_types_by_name['IpPort'] = _IPPORT
DESCRIPTOR.message_types_by_name['SerialPort'] = _SERIALPORT
DESCRIPTOR.message_types_by_name['CommChannel'] = _COMMCHANNEL
DESCRIPTOR.message_types_by_name['CommEndpointRouting'] = _COMMENDPOINTROUTING
DESCRIPTOR.message_types_by_name['FrontEndProcessor'] = _FRONTENDPROCESSOR
DESCRIPTOR.message_types_by_name['EndpointOwnership'] = _ENDPOINTOWNERSHIP
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['EndpointConnection'] = _ENDPOINTCONNECTION
DESCRIPTOR.message_types_by_name['CommandHandlerBinding'] = _COMMANDHANDLERBINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IpPort = _reflection.GeneratedProtocolMessageType('IpPort', (_message.Message,), {
  'DESCRIPTOR' : _IPPORT,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.IpPort)
  })
_sym_db.RegisterMessage(IpPort)

SerialPort = _reflection.GeneratedProtocolMessageType('SerialPort', (_message.Message,), {
  'DESCRIPTOR' : _SERIALPORT,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.SerialPort)
  })
_sym_db.RegisterMessage(SerialPort)

CommChannel = _reflection.GeneratedProtocolMessageType('CommChannel', (_message.Message,), {
  'DESCRIPTOR' : _COMMCHANNEL,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.CommChannel)
  })
_sym_db.RegisterMessage(CommChannel)

CommEndpointRouting = _reflection.GeneratedProtocolMessageType('CommEndpointRouting', (_message.Message,), {
  'DESCRIPTOR' : _COMMENDPOINTROUTING,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.CommEndpointRouting)
  })
_sym_db.RegisterMessage(CommEndpointRouting)

FrontEndProcessor = _reflection.GeneratedProtocolMessageType('FrontEndProcessor', (_message.Message,), {
  'DESCRIPTOR' : _FRONTENDPROCESSOR,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.FrontEndProcessor)
  })
_sym_db.RegisterMessage(FrontEndProcessor)

EndpointOwnership = _reflection.GeneratedProtocolMessageType('EndpointOwnership', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTOWNERSHIP,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.EndpointOwnership)
  })
_sym_db.RegisterMessage(EndpointOwnership)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

EndpointConnection = _reflection.GeneratedProtocolMessageType('EndpointConnection', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTCONNECTION,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.EndpointConnection)
  })
_sym_db.RegisterMessage(EndpointConnection)

CommandHandlerBinding = _reflection.GeneratedProtocolMessageType('CommandHandlerBinding', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDHANDLERBINDING,
  '__module__' : 'FEP_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.FEP.CommandHandlerBinding)
  })
_sym_db.RegisterMessage(CommandHandlerBinding)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
