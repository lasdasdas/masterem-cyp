# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datalog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='datalog.proto',
  package='station',
  syntax='proto3',
  serialized_pb=_b('\n\rdatalog.proto\x12\x07station\"\x8d\x01\n\x07Station\x12\x0c\n\x04town\x18\x01 \x01(\t\x12\x0e\n\x06postal\x18\x02 \x01(\x05\x12\x0e\n\x06\x63louds\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1b.station.Station.SensorData\x1a)\n\nSensorData\x12\x0e\n\x06number\x18\x01 \x01(\x02\x12\x0b\n\x03\x63\x61t\x18\x02 \x01(\x05\",\n\x07\x44\x61taLog\x12!\n\x07station\x18\x01 \x03(\x0b\x32\x10.station.Stationb\x06proto3')
)




_STATION_SENSORDATA = _descriptor.Descriptor(
  name='SensorData',
  full_name='station.Station.SensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='station.Station.SensorData.number', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cat', full_name='station.Station.SensorData.cat', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=168,
)

_STATION = _descriptor.Descriptor(
  name='Station',
  full_name='station.Station',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='town', full_name='station.Station.town', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postal', full_name='station.Station.postal', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clouds', full_name='station.Station.clouds', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='station.Station.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STATION_SENSORDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=168,
)


_DATALOG = _descriptor.Descriptor(
  name='DataLog',
  full_name='station.DataLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='station', full_name='station.DataLog.station', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=214,
)

_STATION_SENSORDATA.containing_type = _STATION
_STATION.fields_by_name['data'].message_type = _STATION_SENSORDATA
_DATALOG.fields_by_name['station'].message_type = _STATION
DESCRIPTOR.message_types_by_name['Station'] = _STATION
DESCRIPTOR.message_types_by_name['DataLog'] = _DATALOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Station = _reflection.GeneratedProtocolMessageType('Station', (_message.Message,), dict(

  SensorData = _reflection.GeneratedProtocolMessageType('SensorData', (_message.Message,), dict(
    DESCRIPTOR = _STATION_SENSORDATA,
    __module__ = 'datalog_pb2'
    # @@protoc_insertion_point(class_scope:station.Station.SensorData)
    ))
  ,
  DESCRIPTOR = _STATION,
  __module__ = 'datalog_pb2'
  # @@protoc_insertion_point(class_scope:station.Station)
  ))
_sym_db.RegisterMessage(Station)
_sym_db.RegisterMessage(Station.SensorData)

DataLog = _reflection.GeneratedProtocolMessageType('DataLog', (_message.Message,), dict(
  DESCRIPTOR = _DATALOG,
  __module__ = 'datalog_pb2'
  # @@protoc_insertion_point(class_scope:station.DataLog)
  ))
_sym_db.RegisterMessage(DataLog)


# @@protoc_insertion_point(module_scope)
