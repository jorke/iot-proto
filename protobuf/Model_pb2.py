# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Utils_pb2 as Utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Model.proto',
  package='org.totalgrid.reef.client.service.proto.Model',
  syntax='proto2',
  serialized_options=b'\n\'org.totalgrid.reef.client.service.protoB\005Model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bModel.proto\x12-org.totalgrid.reef.client.service.proto.Model\x1a\x0bUtils.proto\"\x19\n\x08ReefUUID\x12\r\n\x05value\x18\x01 \x02(\t\"\x17\n\x06ReefID\x12\r\n\x05value\x18\x01 \x02(\t\"\xbc\x01\n\x06\x45ntity\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\r\n\x05types\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12N\n\trelations\x18\n \x03(\x0b\x32;.org.totalgrid.reef.client.service.proto.Model.Relationship\"\x96\x01\n\x0cRelationship\x12\x14\n\x0crelationship\x18\x01 \x01(\t\x12\x15\n\rdescendant_of\x18\x02 \x01(\x08\x12G\n\x08\x65ntities\x18\n \x03(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x10\n\x08\x64istance\x18\x0f \x01(\r\"\x88\x02\n\nEntityEdge\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x45\n\x06parent\x18\x02 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x44\n\x05\x63hild\x18\x03 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x14\n\x0crelationship\x18\x04 \x01(\t\x12\x10\n\x08\x64istance\x18\x05 \x01(\r\"\xa7\x01\n\x10\x45ntityAttributes\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12L\n\nattributes\x18\x02 \x03(\x0b\x32\x38.org.totalgrid.reef.client.service.proto.Utils.Attribute\"\xa5\x01\n\x0f\x45ntityAttribute\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12K\n\tattribute\x18\x02 \x01(\x0b\x32\x38.org.totalgrid.reef.client.service.proto.Utils.Attribute\"\xd4\x02\n\x05Point\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12G\n\x08\x65ndpoint\x18\x05 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x45\n\x06\x65ntity\x18\x07 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x10\n\x08\x61\x62normal\x18\x06 \x01(\x08\x12\x46\n\x04type\x18\x08 \x01(\x0e\x32\x38.org.totalgrid.reef.client.service.proto.Model.PointType\x12\x0c\n\x04unit\x18\t \x01(\t\"\xce\x02\n\x07\x43ommand\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12G\n\x08\x65ndpoint\x18\x05 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12\x45\n\x06\x65ntity\x18\x06 \x01(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity\x12H\n\x04type\x18\x07 \x01(\x0e\x32:.org.totalgrid.reef.client.service.proto.Model.CommandType\"\xcb\x01\n\nConfigFile\x12\x45\n\x04uuid\x18\x01 \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tmime_type\x18\x03 \x01(\t\x12\x0c\n\x04\x66ile\x18\x04 \x01(\x0c\x12G\n\x08\x65ntities\x18\x05 \x03(\x0b\x32\x35.org.totalgrid.reef.client.service.proto.Model.Entity*0\n\tPointType\x12\n\n\x06\x41NALOG\x10\x01\x12\x0b\n\x07\x43OUNTER\x10\x02\x12\n\n\x06STATUS\x10\x03*V\n\x0b\x43ommandType\x12\x0b\n\x07\x43ONTROL\x10\x01\x12\x10\n\x0cSETPOINT_INT\x10\x02\x12\x13\n\x0fSETPOINT_DOUBLE\x10\x03\x12\x13\n\x0fSETPOINT_STRING\x10\x04\x42\x30\n\'org.totalgrid.reef.client.service.protoB\x05Model'
  ,
  dependencies=[Utils__pb2.DESCRIPTOR,])

_POINTTYPE = _descriptor.EnumDescriptor(
  name='PointType',
  full_name='org.totalgrid.reef.client.service.proto.Model.PointType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANALOG', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COUNTER', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1962,
  serialized_end=2010,
)
_sym_db.RegisterEnumDescriptor(_POINTTYPE)

PointType = enum_type_wrapper.EnumTypeWrapper(_POINTTYPE)
_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='org.totalgrid.reef.client.service.proto.Model.CommandType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTROL', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETPOINT_INT', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETPOINT_DOUBLE', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SETPOINT_STRING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2012,
  serialized_end=2098,
)
_sym_db.RegisterEnumDescriptor(_COMMANDTYPE)

CommandType = enum_type_wrapper.EnumTypeWrapper(_COMMANDTYPE)
ANALOG = 1
COUNTER = 2
STATUS = 3
CONTROL = 1
SETPOINT_INT = 2
SETPOINT_DOUBLE = 3
SETPOINT_STRING = 4



_REEFUUID = _descriptor.Descriptor(
  name='ReefUUID',
  full_name='org.totalgrid.reef.client.service.proto.Model.ReefUUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='org.totalgrid.reef.client.service.proto.Model.ReefUUID.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=75,
  serialized_end=100,
)


_REEFID = _descriptor.Descriptor(
  name='ReefID',
  full_name='org.totalgrid.reef.client.service.proto.Model.ReefID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='org.totalgrid.reef.client.service.proto.Model.ReefID.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=102,
  serialized_end=125,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='org.totalgrid.reef.client.service.proto.Model.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Model.Entity.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='org.totalgrid.reef.client.service.proto.Model.Entity.types', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.Model.Entity.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relations', full_name='org.totalgrid.reef.client.service.proto.Model.Entity.relations', index=3,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=128,
  serialized_end=316,
)


_RELATIONSHIP = _descriptor.Descriptor(
  name='Relationship',
  full_name='org.totalgrid.reef.client.service.proto.Model.Relationship',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relationship', full_name='org.totalgrid.reef.client.service.proto.Model.Relationship.relationship', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descendant_of', full_name='org.totalgrid.reef.client.service.proto.Model.Relationship.descendant_of', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='org.totalgrid.reef.client.service.proto.Model.Relationship.entities', index=2,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='org.totalgrid.reef.client.service.proto.Model.Relationship.distance', index=3,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=319,
  serialized_end=469,
)


_ENTITYEDGE = _descriptor.Descriptor(
  name='EntityEdge',
  full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge.parent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child', full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge.child', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relationship', full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge.relationship', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='org.totalgrid.reef.client.service.proto.Model.EntityEdge.distance', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=472,
  serialized_end=736,
)


_ENTITYATTRIBUTES = _descriptor.Descriptor(
  name='EntityAttributes',
  full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttributes.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttributes.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=739,
  serialized_end=906,
)


_ENTITYATTRIBUTE = _descriptor.Descriptor(
  name='EntityAttribute',
  full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttribute.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='org.totalgrid.reef.client.service.proto.Model.EntityAttribute.attribute', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=909,
  serialized_end=1074,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='org.totalgrid.reef.client.service.proto.Model.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Model.Point.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.Model.Point.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='org.totalgrid.reef.client.service.proto.Model.Point.endpoint', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='org.totalgrid.reef.client.service.proto.Model.Point.entity', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abnormal', full_name='org.totalgrid.reef.client.service.proto.Model.Point.abnormal', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='org.totalgrid.reef.client.service.proto.Model.Point.type', index=5,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit', full_name='org.totalgrid.reef.client.service.proto.Model.Point.unit', index=6,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=1077,
  serialized_end=1417,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='org.totalgrid.reef.client.service.proto.Model.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Model.Command.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.Model.Command.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='org.totalgrid.reef.client.service.proto.Model.Command.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='org.totalgrid.reef.client.service.proto.Model.Command.endpoint', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='org.totalgrid.reef.client.service.proto.Model.Command.entity', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='org.totalgrid.reef.client.service.proto.Model.Command.type', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1420,
  serialized_end=1754,
)


_CONFIGFILE = _descriptor.Descriptor(
  name='ConfigFile',
  full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile.uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile.mime_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile.file', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='org.totalgrid.reef.client.service.proto.Model.ConfigFile.entities', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=1757,
  serialized_end=1960,
)

_ENTITY.fields_by_name['uuid'].message_type = _REEFUUID
_ENTITY.fields_by_name['relations'].message_type = _RELATIONSHIP
_RELATIONSHIP.fields_by_name['entities'].message_type = _ENTITY
_ENTITYEDGE.fields_by_name['uuid'].message_type = _REEFUUID
_ENTITYEDGE.fields_by_name['parent'].message_type = _ENTITY
_ENTITYEDGE.fields_by_name['child'].message_type = _ENTITY
_ENTITYATTRIBUTES.fields_by_name['entity'].message_type = _ENTITY
_ENTITYATTRIBUTES.fields_by_name['attributes'].message_type = Utils__pb2._ATTRIBUTE
_ENTITYATTRIBUTE.fields_by_name['entity'].message_type = _ENTITY
_ENTITYATTRIBUTE.fields_by_name['attribute'].message_type = Utils__pb2._ATTRIBUTE
_POINT.fields_by_name['uuid'].message_type = _REEFUUID
_POINT.fields_by_name['endpoint'].message_type = _ENTITY
_POINT.fields_by_name['entity'].message_type = _ENTITY
_POINT.fields_by_name['type'].enum_type = _POINTTYPE
_COMMAND.fields_by_name['uuid'].message_type = _REEFUUID
_COMMAND.fields_by_name['endpoint'].message_type = _ENTITY
_COMMAND.fields_by_name['entity'].message_type = _ENTITY
_COMMAND.fields_by_name['type'].enum_type = _COMMANDTYPE
_CONFIGFILE.fields_by_name['uuid'].message_type = _REEFUUID
_CONFIGFILE.fields_by_name['entities'].message_type = _ENTITY
DESCRIPTOR.message_types_by_name['ReefUUID'] = _REEFUUID
DESCRIPTOR.message_types_by_name['ReefID'] = _REEFID
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Relationship'] = _RELATIONSHIP
DESCRIPTOR.message_types_by_name['EntityEdge'] = _ENTITYEDGE
DESCRIPTOR.message_types_by_name['EntityAttributes'] = _ENTITYATTRIBUTES
DESCRIPTOR.message_types_by_name['EntityAttribute'] = _ENTITYATTRIBUTE
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['ConfigFile'] = _CONFIGFILE
DESCRIPTOR.enum_types_by_name['PointType'] = _POINTTYPE
DESCRIPTOR.enum_types_by_name['CommandType'] = _COMMANDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReefUUID = _reflection.GeneratedProtocolMessageType('ReefUUID', (_message.Message,), {
  'DESCRIPTOR' : _REEFUUID,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.ReefUUID)
  })
_sym_db.RegisterMessage(ReefUUID)

ReefID = _reflection.GeneratedProtocolMessageType('ReefID', (_message.Message,), {
  'DESCRIPTOR' : _REEFID,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.ReefID)
  })
_sym_db.RegisterMessage(ReefID)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.Entity)
  })
_sym_db.RegisterMessage(Entity)

Relationship = _reflection.GeneratedProtocolMessageType('Relationship', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONSHIP,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.Relationship)
  })
_sym_db.RegisterMessage(Relationship)

EntityEdge = _reflection.GeneratedProtocolMessageType('EntityEdge', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYEDGE,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.EntityEdge)
  })
_sym_db.RegisterMessage(EntityEdge)

EntityAttributes = _reflection.GeneratedProtocolMessageType('EntityAttributes', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYATTRIBUTES,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.EntityAttributes)
  })
_sym_db.RegisterMessage(EntityAttributes)

EntityAttribute = _reflection.GeneratedProtocolMessageType('EntityAttribute', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYATTRIBUTE,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.EntityAttribute)
  })
_sym_db.RegisterMessage(EntityAttribute)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.Point)
  })
_sym_db.RegisterMessage(Point)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.Command)
  })
_sym_db.RegisterMessage(Command)

ConfigFile = _reflection.GeneratedProtocolMessageType('ConfigFile', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGFILE,
  '__module__' : 'Model_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Model.ConfigFile)
  })
_sym_db.RegisterMessage(ConfigFile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
