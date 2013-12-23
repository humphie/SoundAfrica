# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataBuffer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DataBuffer.proto',
  package='protobuffers',
  serialized_pb='\n\x10\x44\x61taBuffer.proto\x12\x0cprotobuffers\"\xac\x01\n\x04Song\x12\x13\n\x0btrackNumber\x18\x01 \x02(\x05\x12\r\n\x05title\x18\x02 \x02(\t\x12\r\n\x05genre\x18\x03 \x02(\t\x12\x0e\n\x06\x61rtist\x18\x04 \x02(\t\x12\x0c\n\x04year\x18\x05 \x02(\t\x12\x0c\n\x04path\x18\x06 \x02(\t\x12\x0f\n\x07\x63omment\x18\x07 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x02(\t\x12\x10\n\x08language\x18\t \x02(\t\x12\r\n\x05\x61lbum\x18\n \x02(\t\"\xe3\x01\n\x05\x41lbum\x12\x11\n\talbumName\x18\x01 \x02(\t\x12\x13\n\x0b\x61lbumArtist\x18\x02 \x02(\t\x12!\n\x05songs\x18\x03 \x03(\x0b\x32\x12.protobuffers.Song\x12\x10\n\x08\x63overArt\x18\x04 \x01(\x0c\x12\x32\n\x05value\x18\x05 \x01(\x0e\x32\x19.protobuffers.Album.Value:\x08NONEFREE\x12\x0e\n\x06rating\x18\x06 \x01(\x05\x12\r\n\x05price\x18\x07 \x01(\x05\"*\n\x05Value\x12\x08\n\x04\x46REE\x10\x00\x12\x0c\n\x08NONEFREE\x10\x01\x12\t\n\x05PROMO\x10\x02\"1\n\nCollection\x12#\n\x06\x61lbums\x18\x01 \x03(\x0b\x32\x13.protobuffers.AlbumB#\n\x14\x63om.app.protobuffersB\x0b\x44\x61tabuffers')



_ALBUM_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='protobuffers.Album.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONEFREE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMO', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=395,
  serialized_end=437,
)


_SONG = _descriptor.Descriptor(
  name='Song',
  full_name='protobuffers.Song',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trackNumber', full_name='protobuffers.Song.trackNumber', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='protobuffers.Song.title', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genre', full_name='protobuffers.Song.genre', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='artist', full_name='protobuffers.Song.artist', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='protobuffers.Song.year', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='protobuffers.Song.path', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='protobuffers.Song.comment', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='protobuffers.Song.description', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='protobuffers.Song.language', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='album', full_name='protobuffers.Song.album', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=35,
  serialized_end=207,
)


_ALBUM = _descriptor.Descriptor(
  name='Album',
  full_name='protobuffers.Album',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='albumName', full_name='protobuffers.Album.albumName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='albumArtist', full_name='protobuffers.Album.albumArtist', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='songs', full_name='protobuffers.Album.songs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coverArt', full_name='protobuffers.Album.coverArt', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protobuffers.Album.value', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rating', full_name='protobuffers.Album.rating', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='protobuffers.Album.price', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALBUM_VALUE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=210,
  serialized_end=437,
)


_COLLECTION = _descriptor.Descriptor(
  name='Collection',
  full_name='protobuffers.Collection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='albums', full_name='protobuffers.Collection.albums', index=0,
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
  extension_ranges=[],
  serialized_start=439,
  serialized_end=488,
)

_ALBUM.fields_by_name['songs'].message_type = _SONG
_ALBUM.fields_by_name['value'].enum_type = _ALBUM_VALUE
_ALBUM_VALUE.containing_type = _ALBUM;
_COLLECTION.fields_by_name['albums'].message_type = _ALBUM
DESCRIPTOR.message_types_by_name['Song'] = _SONG
DESCRIPTOR.message_types_by_name['Album'] = _ALBUM
DESCRIPTOR.message_types_by_name['Collection'] = _COLLECTION

class Song(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SONG

  # @@protoc_insertion_point(class_scope:protobuffers.Song)

class Album(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ALBUM

  # @@protoc_insertion_point(class_scope:protobuffers.Album)

class Collection(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COLLECTION

  # @@protoc_insertion_point(class_scope:protobuffers.Collection)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\024com.app.protobuffersB\013Databuffers')
# @@protoc_insertion_point(module_scope)