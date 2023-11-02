# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Calculations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Model_pb2 as Model__pb2
import Measurements_pb2 as Measurements__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Calculations.proto',
  package='org.totalgrid.reef.client.service.proto.Calculations',
  syntax='proto2',
  serialized_options=b'\n\'org.totalgrid.reef.client.service.protoB\014Calculations',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x43\x61lculations.proto\x12\x34org.totalgrid.reef.client.service.proto.Calculations\x1a\x0bModel.proto\x1a\x12Measurements.proto\"8\n\x0fTriggerStrategy\x12\x11\n\tperiod_ms\x18\x01 \x01(\x04\x12\x12\n\nupdate_any\x18\x03 \x01(\x08\"U\n\x10MeasurementRange\x12\x12\n\nsince_last\x18\x04 \x01(\x08\x12\x0f\n\x07\x66rom_ms\x18\x01 \x01(\x04\x12\r\n\x05to_ms\x18\x02 \x01(\x04\x12\r\n\x05limit\x18\x03 \x01(\r\"\xaa\x01\n\x11SingleMeasurement\x12m\n\x08strategy\x18\x01 \x01(\x0e\x32[.org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement.MeasurementStrategy\"&\n\x13MeasurementStrategy\x12\x0f\n\x0bMOST_RECENT\x10\x01\"\x9e\x02\n\x10\x43\x61lculationInput\x12\x43\n\x05point\x18\x01 \x01(\x0b\x32\x34.org.totalgrid.reef.client.service.proto.Model.Point\x12\x15\n\rvariable_name\x18\x02 \x01(\t\x12U\n\x05range\x18\x03 \x01(\x0b\x32\x46.org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange\x12W\n\x06single\x18\x04 \x01(\x0b\x32G.org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement\"\xa8\x01\n\x0cInputQuality\x12]\n\x08strategy\x18\x01 \x01(\x0e\x32K.org.totalgrid.reef.client.service.proto.Calculations.InputQuality.Strategy\"9\n\x08Strategy\x12\x14\n\x10ONLY_WHEN_ALL_OK\x10\x01\x12\x17\n\x13REMOVE_BAD_AND_CALC\x10\x02\"\x9d\x01\n\rOutputQuality\x12^\n\x08strategy\x18\x01 \x01(\x0e\x32L.org.totalgrid.reef.client.service.proto.Calculations.OutputQuality.Strategy\",\n\x08Strategy\x12\x11\n\rWORST_QUALITY\x10\x01\x12\r\n\tALWAYS_OK\x10\x02\"\x86\x01\n\nOutputTime\x12[\n\x08strategy\x18\x01 \x01(\x0e\x32I.org.totalgrid.reef.client.service.proto.Calculations.OutputTime.Strategy\"\x1b\n\x08Strategy\x12\x0f\n\x0bMOST_RECENT\x10\x01\"\x91\x05\n\x0b\x43\x61lculation\x12\x45\n\x04uuid\x18\t \x01(\x0b\x32\x37.org.totalgrid.reef.client.service.proto.Model.ReefUUID\x12J\n\x0coutput_point\x18\x01 \x01(\x0b\x32\x34.org.totalgrid.reef.client.service.proto.Model.Point\x12\x12\n\naccumulate\x18\x02 \x01(\x08\x12Y\n\ntriggering\x18\x03 \x01(\x0b\x32\x45.org.totalgrid.reef.client.service.proto.Calculations.TriggerStrategy\x12[\n\x0b\x63\x61lc_inputs\x18\x04 \x03(\x0b\x32\x46.org.totalgrid.reef.client.service.proto.Calculations.CalculationInput\x12^\n\x12triggering_quality\x18\x05 \x01(\x0b\x32\x42.org.totalgrid.reef.client.service.proto.Calculations.InputQuality\x12[\n\x0equality_output\x18\x06 \x01(\x0b\x32\x43.org.totalgrid.reef.client.service.proto.Calculations.OutputQuality\x12U\n\x0btime_output\x18\x07 \x01(\x0b\x32@.org.totalgrid.reef.client.service.proto.Calculations.OutputTime\x12\x0f\n\x07\x66ormula\x18\x08 \x01(\tB7\n\'org.totalgrid.reef.client.service.protoB\x0c\x43\x61lculations'
  ,
  dependencies=[Model__pb2.DESCRIPTOR,Measurements__pb2.DESCRIPTOR,])



_SINGLEMEASUREMENT_MEASUREMENTSTRATEGY = _descriptor.EnumDescriptor(
  name='MeasurementStrategy',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement.MeasurementStrategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOST_RECENT', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=387,
  serialized_end=425,
)
_sym_db.RegisterEnumDescriptor(_SINGLEMEASUREMENT_MEASUREMENTSTRATEGY)

_INPUTQUALITY_STRATEGY = _descriptor.EnumDescriptor(
  name='Strategy',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.InputQuality.Strategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONLY_WHEN_ALL_OK', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_BAD_AND_CALC', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=828,
  serialized_end=885,
)
_sym_db.RegisterEnumDescriptor(_INPUTQUALITY_STRATEGY)

_OUTPUTQUALITY_STRATEGY = _descriptor.EnumDescriptor(
  name='Strategy',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputQuality.Strategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORST_QUALITY', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALWAYS_OK', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1001,
  serialized_end=1045,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTQUALITY_STRATEGY)

_OUTPUTTIME_STRATEGY = _descriptor.EnumDescriptor(
  name='Strategy',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputTime.Strategy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOST_RECENT', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1155,
  serialized_end=1182,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTTIME_STRATEGY)


_TRIGGERSTRATEGY = _descriptor.Descriptor(
  name='TriggerStrategy',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.TriggerStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='period_ms', full_name='org.totalgrid.reef.client.service.proto.Calculations.TriggerStrategy.period_ms', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_any', full_name='org.totalgrid.reef.client.service.proto.Calculations.TriggerStrategy.update_any', index=1,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=109,
  serialized_end=165,
)


_MEASUREMENTRANGE = _descriptor.Descriptor(
  name='MeasurementRange',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='since_last', full_name='org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange.since_last', index=0,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_ms', full_name='org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange.from_ms', index=1,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_ms', full_name='org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange.to_ms', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange.limit', index=3,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=167,
  serialized_end=252,
)


_SINGLEMEASUREMENT = _descriptor.Descriptor(
  name='SingleMeasurement',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement.strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SINGLEMEASUREMENT_MEASUREMENTSTRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=425,
)


_CALCULATIONINPUT = _descriptor.Descriptor(
  name='CalculationInput',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.CalculationInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='org.totalgrid.reef.client.service.proto.Calculations.CalculationInput.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variable_name', full_name='org.totalgrid.reef.client.service.proto.Calculations.CalculationInput.variable_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range', full_name='org.totalgrid.reef.client.service.proto.Calculations.CalculationInput.range', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='single', full_name='org.totalgrid.reef.client.service.proto.Calculations.CalculationInput.single', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=428,
  serialized_end=714,
)


_INPUTQUALITY = _descriptor.Descriptor(
  name='InputQuality',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.InputQuality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='org.totalgrid.reef.client.service.proto.Calculations.InputQuality.strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INPUTQUALITY_STRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=885,
)


_OUTPUTQUALITY = _descriptor.Descriptor(
  name='OutputQuality',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputQuality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputQuality.strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OUTPUTQUALITY_STRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=888,
  serialized_end=1045,
)


_OUTPUTTIME = _descriptor.Descriptor(
  name='OutputTime',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy', full_name='org.totalgrid.reef.client.service.proto.Calculations.OutputTime.strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OUTPUTTIME_STRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1048,
  serialized_end=1182,
)


_CALCULATION = _descriptor.Descriptor(
  name='Calculation',
  full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.uuid', index=0,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_point', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.output_point', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accumulate', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.accumulate', index=2,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='triggering', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.triggering', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='calc_inputs', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.calc_inputs', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='triggering_quality', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.triggering_quality', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quality_output', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.quality_output', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_output', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.time_output', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='formula', full_name='org.totalgrid.reef.client.service.proto.Calculations.Calculation.formula', index=8,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=1185,
  serialized_end=1842,
)

_SINGLEMEASUREMENT.fields_by_name['strategy'].enum_type = _SINGLEMEASUREMENT_MEASUREMENTSTRATEGY
_SINGLEMEASUREMENT_MEASUREMENTSTRATEGY.containing_type = _SINGLEMEASUREMENT
_CALCULATIONINPUT.fields_by_name['point'].message_type = Model__pb2._POINT
_CALCULATIONINPUT.fields_by_name['range'].message_type = _MEASUREMENTRANGE
_CALCULATIONINPUT.fields_by_name['single'].message_type = _SINGLEMEASUREMENT
_INPUTQUALITY.fields_by_name['strategy'].enum_type = _INPUTQUALITY_STRATEGY
_INPUTQUALITY_STRATEGY.containing_type = _INPUTQUALITY
_OUTPUTQUALITY.fields_by_name['strategy'].enum_type = _OUTPUTQUALITY_STRATEGY
_OUTPUTQUALITY_STRATEGY.containing_type = _OUTPUTQUALITY
_OUTPUTTIME.fields_by_name['strategy'].enum_type = _OUTPUTTIME_STRATEGY
_OUTPUTTIME_STRATEGY.containing_type = _OUTPUTTIME
_CALCULATION.fields_by_name['uuid'].message_type = Model__pb2._REEFUUID
_CALCULATION.fields_by_name['output_point'].message_type = Model__pb2._POINT
_CALCULATION.fields_by_name['triggering'].message_type = _TRIGGERSTRATEGY
_CALCULATION.fields_by_name['calc_inputs'].message_type = _CALCULATIONINPUT
_CALCULATION.fields_by_name['triggering_quality'].message_type = _INPUTQUALITY
_CALCULATION.fields_by_name['quality_output'].message_type = _OUTPUTQUALITY
_CALCULATION.fields_by_name['time_output'].message_type = _OUTPUTTIME
DESCRIPTOR.message_types_by_name['TriggerStrategy'] = _TRIGGERSTRATEGY
DESCRIPTOR.message_types_by_name['MeasurementRange'] = _MEASUREMENTRANGE
DESCRIPTOR.message_types_by_name['SingleMeasurement'] = _SINGLEMEASUREMENT
DESCRIPTOR.message_types_by_name['CalculationInput'] = _CALCULATIONINPUT
DESCRIPTOR.message_types_by_name['InputQuality'] = _INPUTQUALITY
DESCRIPTOR.message_types_by_name['OutputQuality'] = _OUTPUTQUALITY
DESCRIPTOR.message_types_by_name['OutputTime'] = _OUTPUTTIME
DESCRIPTOR.message_types_by_name['Calculation'] = _CALCULATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TriggerStrategy = _reflection.GeneratedProtocolMessageType('TriggerStrategy', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERSTRATEGY,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.TriggerStrategy)
  })
_sym_db.RegisterMessage(TriggerStrategy)

MeasurementRange = _reflection.GeneratedProtocolMessageType('MeasurementRange', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENTRANGE,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.MeasurementRange)
  })
_sym_db.RegisterMessage(MeasurementRange)

SingleMeasurement = _reflection.GeneratedProtocolMessageType('SingleMeasurement', (_message.Message,), {
  'DESCRIPTOR' : _SINGLEMEASUREMENT,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.SingleMeasurement)
  })
_sym_db.RegisterMessage(SingleMeasurement)

CalculationInput = _reflection.GeneratedProtocolMessageType('CalculationInput', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATIONINPUT,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.CalculationInput)
  })
_sym_db.RegisterMessage(CalculationInput)

InputQuality = _reflection.GeneratedProtocolMessageType('InputQuality', (_message.Message,), {
  'DESCRIPTOR' : _INPUTQUALITY,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.InputQuality)
  })
_sym_db.RegisterMessage(InputQuality)

OutputQuality = _reflection.GeneratedProtocolMessageType('OutputQuality', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTQUALITY,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.OutputQuality)
  })
_sym_db.RegisterMessage(OutputQuality)

OutputTime = _reflection.GeneratedProtocolMessageType('OutputTime', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTTIME,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.OutputTime)
  })
_sym_db.RegisterMessage(OutputTime)

Calculation = _reflection.GeneratedProtocolMessageType('Calculation', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATION,
  '__module__' : 'Calculations_pb2'
  # @@protoc_insertion_point(class_scope:org.totalgrid.reef.client.service.proto.Calculations.Calculation)
  })
_sym_db.RegisterMessage(Calculation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)