# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Model_pb2 as Model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Commands.proto',
  package='org.totalgrid.reef.client.service.proto.Commands',
  syntax='proto2',
  serialized_options=b'\n\'org.totalgrid.reef.client.service.protoB\010Commands',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x43ommands.proto\x12\x30org.totalgrid.reef.client.service.proto.Commands\x1a\x0bModel.proto\"\x93\x03\n\x12UserCommandRequest\x12\x41\n\x02id\x18\x01 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.ReefID\x12Y\n\x0f\x63ommand_request\x18\x02 \x01(\x0b\x32@.org.totalgrid.reef.client.service.proto.Commands.CommandRequest\x12O\n\x06status\x18\x03 \x01(\x0e\x32?.org.totalgrid.reef.client.service.proto.Commands.CommandStatus\x12\x15\n\rerror_message\x18\x06 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x18\n\ntimeout_ms\x18\x05 \x01(\x05:\x04\x35\x30\x30\x30\x12O\n\x06result\x18\x07 \x01(\x0b\x32?.org.totalgrid.reef.client.service.proto.Commands.CommandResult\"w\n\rCommandResult\x12O\n\x06status\x18\x01 \x01(\x0e\x32?.org.totalgrid.reef.client.service.proto.Commands.CommandStatus\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\xd0\x02\n\x0b\x43ommandLock\x12\x41\n\x02id\x18\x01 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.ReefID\x12H\n\x08\x63ommands\x18\x02 \x03(\x0b\x32\x36.org.totalgrid.reef.client.service.proto.Model.Command\x12X\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\x0e\x32H.org.totalgrid.reef.client.service.proto.Commands.CommandLock.AccessMode\x12\x13\n\x0b\x65xpire_time\x18\x04 \x01(\x04\x12\x0c\n\x04user\x18\x05 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x06 \x01(\x08\"&\n\nAccessMode\x12\x0b\n\x07\x41LLOWED\x10\x01\x12\x0b\n\x07\x42LOCKED\x10\x02\"\xb8\x02\n\x0e\x43ommandRequest\x12G\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x36.org.totalgrid.reef.client.service.proto.Model.Command\x12\x16\n\x0e\x63orrelation_id\x18\x02 \x01(\t\x12V\n\x04type\x18\x03 \x01(\x0e\x32H.org.totalgrid.reef.client.service.proto.Commands.CommandRequest.ValType\x12\x0f\n\x07int_val\x18\x04 \x01(\x05\x12\x12\n\ndouble_val\x18\x05 \x01(\x01\x12\x12\n\nstring_val\x18\x06 \x01(\t\"4\n\x07ValType\x12\x07\n\x03INT\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\n\n\x06STRING\x10\x04*\xd4\x01\n\rCommandStatus\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x12\r\n\tNO_SELECT\x10\x03\x12\x10\n\x0c\x46ORMAT_ERROR\x10\x04\x12\x11\n\rNOT_SUPPORTED\x10\x05\x12\x12\n\x0e\x41LREADY_ACTIVE\x10\x06\x12\x12\n\x0eHARDWARE_ERROR\x10\x07\x12\t\n\x05LOCAL\x10\x08\x12\x10\n\x0cTOO_MANY_OPS\x10\t\x12\x12\n\x0eNOT_AUTHORIZED\x10\n\x12\r\n\tUNDEFINED\x10\x0b\x12\r\n\tEXECUTING\x10\x0c\x42\x33\n\'org.totalgrid.reef.client.service.protoB\x08\x43ommands'
  ,
  dependencies=[Model__pb2.DESCRIPTOR,])

_COMMANDSTATUS = _descriptor.EnumDescriptor(
  name='CommandStatus',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_SELECT', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SUPPORTED', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_ACTIVE', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HARDWARE_ERROR', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_OPS', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_AUTHORIZED', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTING', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1263,
  serialized_end=1475,
)
_sym_db.RegisterEnumDescriptor(_COMMANDSTATUS)

CommandStatus = enum_type_wrapper.EnumTypeWrapper(_COMMANDSTATUS)
SUCCESS = 1
TIMEOUT = 2
NO_SELECT = 3
FORMAT_ERROR = 4
NOT_SUPPORTED = 5
ALREADY_ACTIVE = 6
HARDWARE_ERROR = 7
LOCAL = 8
TOO_MANY_OPS = 9
NOT_AUTHORIZED = 10
UNDEFINED = 11
EXECUTING = 12


_COMMANDLOCK_ACCESSMODE = _descriptor.EnumDescriptor(
  name='AccessMode',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.AccessMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLOWED', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLOCKED', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=907,
  serialized_end=945,
)
_sym_db.RegisterEnumDescriptor(_COMMANDLOCK_ACCESSMODE)

_COMMANDREQUEST_VALTYPE = _descriptor.EnumDescriptor(
  name='ValType',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.ValType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1208,
  serialized_end=1260,
)
_sym_db.RegisterEnumDescriptor(_COMMANDREQUEST_VALTYPE)


_USERCOMMANDREQUEST = _descriptor.Descriptor(
  name='UserCommandRequest',
  full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_request', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.command_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.error_message', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.user', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_ms', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.timeout_ms', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest.result', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=82,
  serialized_end=485,
)


_COMMANDRESULT = _descriptor.Descriptor(
  name='CommandResult',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandResult.error_message', index=1,
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
  serialized_start=487,
  serialized_end=606,
)


_COMMANDLOCK = _descriptor.Descriptor(
  name='CommandLock',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.commands', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.access', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.expire_time', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandLock.deleted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDLOCK_ACCESSMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=945,
)


_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='correlation_id', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.correlation_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.int_val', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.double_val', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='org.totalgrid.reef.client.service.proto.Commands.CommandRequest.string_val', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDREQUEST_VALTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=948,
  serialized_end=1260,
)

_USERCOMMANDREQUEST.fields_by_name['id'].message_type = Model__pb2._REEFID
_USERCOMMANDREQUEST.fields_by_name['command_request'].message_type = _COMMANDREQUEST
_USERCOMMANDREQUEST.fields_by_name['status'].enum_type = _COMMANDSTATUS
_USERCOMMANDREQUEST.fields_by_name['result'].message_type = _COMMANDRESULT
_COMMANDRESULT.fields_by_name['status'].enum_type = _COMMANDSTATUS
_COMMANDLOCK.fields_by_name['id'].message_type = Model__pb2._REEFID
_COMMANDLOCK.fields_by_name['commands'].message_type = Model__pb2._COMMAND
_COMMANDLOCK.fields_by_name['access'].enum_type = _COMMANDLOCK_ACCESSMODE
_COMMANDLOCK_ACCESSMODE.containing_type = _COMMANDLOCK
_COMMANDREQUEST.fields_by_name['command'].message_type = Model__pb2._COMMAND
_COMMANDREQUEST.fields_by_name['type'].enum_type = _COMMANDREQUEST_VALTYPE
_COMMANDREQUEST_VALTYPE.containing_type = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['UserCommandRequest'] = _USERCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandResult'] = _COMMANDRESULT
DESCRIPTOR.message_types_by_name['CommandLock'] = _COMMANDLOCK
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.enum_types_by_name['CommandStatus'] = _COMMANDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserCommandRequest = _reflection.GeneratedProtocolMessageType('UserCommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCOMMANDREQUEST,
  '__module__' : 'Commands_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Commands.UserCommandRequest)
  })
_sym_db.RegisterMessage(UserCommandRequest)

CommandResult = _reflection.GeneratedProtocolMessageType('CommandResult', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDRESULT,
  '__module__' : 'Commands_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Commands.CommandResult)
  })
_sym_db.RegisterMessage(CommandResult)

CommandLock = _reflection.GeneratedProtocolMessageType('CommandLock', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDLOCK,
  '__module__' : 'Commands_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Commands.CommandLock)
  })
_sym_db.RegisterMessage(CommandLock)

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDREQUEST,
  '__module__' : 'Commands_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Commands.CommandRequest)
  })
_sym_db.RegisterMessage(CommandRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)