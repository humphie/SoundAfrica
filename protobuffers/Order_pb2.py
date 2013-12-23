# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Order.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Order.proto',
  package='protobuffers',
  serialized_pb='\n\x0bOrder.proto\x12\x0cprotobuffers\"\xb2\x02\n\x05Order\x12\x12\n\nalbum_name\x18\x01 \x02(\t\x12\x0e\n\x06\x61rtist\x18\x02 \x02(\t\x12\x10\n\x08username\x18\x03 \x02(\t\x12\x10\n\x08password\x18\x04 \x02(\t\x12\x13\n\x0b\x61rchivePath\x18\x05 \x01(\t\x12-\n\x03job\x18\x06 \x01(\x0e\x32\x17.protobuffers.Order.Job:\x07NOTDONE\x12\x31\n\x04type\x18\x07 \x01(\x0e\x32\x1d.protobuffers.Order.AlbumType:\x04\x46REE\x12\x11\n\x06\x63redit\x18\x08 \x01(\x03:\x01\x30\"-\n\tAlbumType\x12\x08\n\x04\x46REE\x10\x00\x12\x0b\n\x07NONFREE\x10\x01\x12\t\n\x05PROMO\x10\x02\"(\n\x03Job\x12\x08\n\x04\x44ONE\x10\x00\x12\x0b\n\x07NOTDONE\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x42#\n\x14\x63om.app.protobuffersB\x0bOrderBuffer')



_ORDER_ALBUMTYPE = _descriptor.EnumDescriptor(
  name='AlbumType',
  full_name='protobuffers.Order.AlbumType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONFREE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMO', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=249,
  serialized_end=294,
)

_ORDER_JOB = _descriptor.EnumDescriptor(
  name='Job',
  full_name='protobuffers.Order.Job',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTDONE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=296,
  serialized_end=336,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='protobuffers.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='album_name', full_name='protobuffers.Order.album_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='artist', full_name='protobuffers.Order.artist', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='protobuffers.Order.username', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='protobuffers.Order.password', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='archivePath', full_name='protobuffers.Order.archivePath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job', full_name='protobuffers.Order.job', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='protobuffers.Order.type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='credit', full_name='protobuffers.Order.credit', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDER_ALBUMTYPE,
    _ORDER_JOB,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=336,
)

_ORDER.fields_by_name['job'].enum_type = _ORDER_JOB
_ORDER.fields_by_name['type'].enum_type = _ORDER_ALBUMTYPE
_ORDER_ALBUMTYPE.containing_type = _ORDER;
_ORDER_JOB.containing_type = _ORDER;
DESCRIPTOR.message_types_by_name['Order'] = _ORDER

class Order(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ORDER

  # @@protoc_insertion_point(class_scope:protobuffers.Order)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\024com.app.protobuffersB\013OrderBuffer')
# @@protoc_insertion_point(module_scope)
