# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/ssd_anchor_generator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/ssd_anchor_generator.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n2object_detection/protos/ssd_anchor_generator.proto\x12\x17object_detection.protos\"\x9f\x01\n\x12SsdAnchorGenerator\x12\x15\n\nnum_layers\x18\x01 \x01(\x05:\x01\x36\x12\x16\n\tmin_scale\x18\x02 \x01(\x02:\x03\x30.2\x12\x17\n\tmax_scale\x18\x03 \x01(\x02:\x04\x30.95\x12\x15\n\raspect_ratios\x18\x04 \x03(\x02\x12*\n\x1creduce_boxes_in_lowest_layer\x18\x05 \x01(\x08:\x04true'
)




_SSDANCHORGENERATOR = _descriptor.Descriptor(
  name='SsdAnchorGenerator',
  full_name='object_detection.protos.SsdAnchorGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_layers', full_name='object_detection.protos.SsdAnchorGenerator.num_layers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=6,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_scale', full_name='object_detection.protos.SsdAnchorGenerator.min_scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_scale', full_name='object_detection.protos.SsdAnchorGenerator.max_scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.95),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='object_detection.protos.SsdAnchorGenerator.aspect_ratios', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reduce_boxes_in_lowest_layer', full_name='object_detection.protos.SsdAnchorGenerator.reduce_boxes_in_lowest_layer', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=80,
  serialized_end=239,
)

DESCRIPTOR.message_types_by_name['SsdAnchorGenerator'] = _SSDANCHORGENERATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SsdAnchorGenerator = _reflection.GeneratedProtocolMessageType('SsdAnchorGenerator', (_message.Message,), {
  'DESCRIPTOR' : _SSDANCHORGENERATOR,
  '__module__' : 'object_detection.protos.ssd_anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SsdAnchorGenerator)
  })
_sym_db.RegisterMessage(SsdAnchorGenerator)


# @@protoc_insertion_point(module_scope)
