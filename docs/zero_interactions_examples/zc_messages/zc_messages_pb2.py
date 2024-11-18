# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: zc_messages.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'zc_messages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11zc_messages.proto\"\xc9\x01\n\tZCVersion\x12\x1a\n\x03\x61pi\x18\x01 \x01(\x0e\x32\r.ZCApiVersion\x12\x11\n\x04uuid\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x12\x13\n\x06sw_ver\x18\x03 \x01(\x0cH\x01\x88\x01\x01\x12\x13\n\x06hw_ver\x18\x04 \x01(\x0cH\x02\x88\x01\x01\x12\x16\n\tlink_addr\x18\x05 \x01(\x0cH\x03\x88\x01\x01\x12\x13\n\x06sec_en\x18\x06 \x01(\x08H\x04\x88\x01\x01\x42\x07\n\x05_uuidB\t\n\x07_sw_verB\t\n\x07_hw_verB\x0c\n\n_link_addrB\t\n\x07_sec_en\"7\n\rZCTemperature\x12\x17\n\x03loc\x18\x01 \x01(\x0e\x32\n.ZCTempLoc\x12\r\n\x05value\x18\x02 \x01(\x05\"\xf6\x01\n\x08ZCStatus\x12\x0e\n\x06uptime\x18\x01 \x01(\r\x12$\n\x0cswitch_state\x18\x02 \x01(\x0e\x32\x0e.ZCSwitchState\x12$\n\x0c\x64\x65vice_state\x18\x03 \x01(\x0e\x32\x0e.ZCDeviceState\x12\x1b\n\x05\x63\x61use\x18\x04 \x01(\x0e\x32\x0c.ZCTripCause\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\r\x12\x0f\n\x07voltage\x18\x06 \x01(\r\x12\x0c\n\x04\x66req\x18\x07 \x01(\r\x12#\n\tdirection\x18\x08 \x01(\x0e\x32\x10.ZCFlowDirection\x12\x1c\n\x04temp\x18\t \x03(\x0b\x32\x0e.ZCTemperature\"/\n\x0cZCCurvePoint\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x10\n\x08\x64uration\x18\x02 \x01(\r\"1\n\x0fZCCsomModConfig\x12\x0e\n\x06\x63losed\x18\x01 \x01(\r\x12\x0e\n\x06period\x18\x02 \x01(\r\"J\n\x0cZCCsomConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1f\n\x03mod\x18\x02 \x01(\x0b\x32\x10.ZCCsomModConfigH\x00\x42\x08\n\x06\x63onfig\"S\n\rZCCurveConfig\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.ZCCurvePoint\x12#\n\tdirection\x18\x02 \x01(\x0e\x32\x10.ZCFlowDirection\"g\n\rZCOcpHwConfig\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\r\x12\x11\n\trec_delay\x18\x03 \x01(\r\x12\x14\n\x0crec_attempts\x18\x04 \x01(\r\x12\x0e\n\x06rec_en\x18\x05 \x01(\x08\"=\n\x0cZCOuvpConfig\x12\r\n\x05lower\x18\x01 \x01(\r\x12\r\n\x05upper\x18\x02 \x01(\r\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"=\n\x0cZCOufpConfig\x12\r\n\x05lower\x18\x01 \x01(\r\x12\r\n\x05upper\x18\x02 \x01(\r\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"!\n\rZCNotifConfig\x12\x10\n\x08interval\x18\x01 \x01(\r\"8\n\rZCCalibConfig\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.ZCCalibType\x12\x0b\n\x03\x61rg\x18\x02 \x01(\x0c\"\xf6\x01\n\x08ZCConfig\x12\x1f\n\x05\x63urve\x18\x01 \x01(\x0b\x32\x0e.ZCCurveConfigH\x00\x12\x1d\n\x04\x63som\x18\x02 \x01(\x0b\x32\r.ZCCsomConfigH\x00\x12 \n\x06ocp_hw\x18\x03 \x01(\x0b\x32\x0e.ZCOcpHwConfigH\x00\x12\x1d\n\x04ouvp\x18\x04 \x01(\x0b\x32\r.ZCOuvpConfigH\x00\x12\x1d\n\x04oufp\x18\x05 \x01(\x0b\x32\r.ZCOufpConfigH\x00\x12\x1f\n\x05notif\x18\x06 \x01(\x0b\x32\x0e.ZCNotifConfigH\x00\x12\x1f\n\x05\x63\x61lib\x18\x07 \x01(\x0b\x32\x0e.ZCCalibConfigH\x00\x42\x08\n\x06\x63onfig\" \n\x10ZCRequestVersion\x12\x0c\n\x04null\x18\x01 \x01(\r\"\x1f\n\x0fZCRequestStatus\x12\x0c\n\x04null\x18\x01 \x01(\r\"/\n\x12ZCRequestDeviceCmd\x12\x19\n\x03\x63md\x18\x01 \x01(\x0e\x32\x0c.ZCDeviceCmd\"/\n\x12ZCRequestSetConfig\x12\x19\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\t.ZCConfig\">\n\x17ZCRequestGetConfigCurve\x12#\n\tdirection\x18\x01 \x01(\x0e\x32\x10.ZCFlowDirection\"&\n\x16ZCRequestGetConfigCsom\x12\x0c\n\x04null\x18\x01 \x01(\r\"\'\n\x17ZCRequestGetConfigOcpHw\x12\x0c\n\x04null\x18\x01 \x01(\r\"&\n\x16ZCRequestGetConfigOuvp\x12\x0c\n\x04null\x18\x01 \x01(\r\"&\n\x16ZCRequestGetConfigOufp\x12\x0c\n\x04null\x18\x01 \x01(\r\"\'\n\x17ZCRequestGetConfigNotif\x12\x0c\n\x04null\x18\x01 \x01(\r\"5\n\x17ZCRequestGetConfigCalib\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.ZCCalibType\"\xc6\x02\n\x12ZCRequestGetConfig\x12)\n\x05\x63urve\x18\x01 \x01(\x0b\x32\x18.ZCRequestGetConfigCurveH\x00\x12\'\n\x04\x63som\x18\x02 \x01(\x0b\x32\x17.ZCRequestGetConfigCsomH\x00\x12*\n\x06ocp_hw\x18\x03 \x01(\x0b\x32\x18.ZCRequestGetConfigOcpHwH\x00\x12\'\n\x04ouvp\x18\x04 \x01(\x0b\x32\x17.ZCRequestGetConfigOuvpH\x00\x12\'\n\x04oufp\x18\x05 \x01(\x0b\x32\x17.ZCRequestGetConfigOufpH\x00\x12)\n\x05notif\x18\x06 \x01(\x0b\x32\x18.ZCRequestGetConfigNotifH\x00\x12)\n\x05\x63\x61lib\x18\x07 \x01(\x0b\x32\x18.ZCRequestGetConfigCalibH\x00\x42\x08\n\x06\x63onfig\"\x17\n\x07ZCError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\"\x87\x01\n\nZCResponse\x12\x1d\n\x07version\x18\x01 \x01(\x0b\x32\n.ZCVersionH\x00\x12\x1b\n\x06status\x18\x02 \x01(\x0b\x32\t.ZCStatusH\x00\x12\x1b\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\t.ZCConfigH\x00\x12\x19\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x08.ZCErrorH\x00\x42\x05\n\x03res\"\xd6\x01\n\tZCRequest\x12$\n\x07version\x18\x01 \x01(\x0b\x32\x11.ZCRequestVersionH\x00\x12\"\n\x06status\x18\x02 \x01(\x0b\x32\x10.ZCRequestStatusH\x00\x12\"\n\x03\x63md\x18\x03 \x01(\x0b\x32\x13.ZCRequestDeviceCmdH\x00\x12)\n\nset_config\x18\x04 \x01(\x0b\x32\x13.ZCRequestSetConfigH\x00\x12)\n\nget_config\x18\x05 \x01(\x0b\x32\x13.ZCRequestGetConfigH\x00\x42\x05\n\x03req\"I\n\tZCMessage\x12\x19\n\x03req\x18\x01 \x01(\x0b\x32\n.ZCRequestH\x00\x12\x1a\n\x03res\x18\x02 \x01(\x0b\x32\x0b.ZCResponseH\x00\x42\x05\n\x03msg*:\n\x0cZCApiVersion\x12\x14\n\x10ZC_API_VERSION_1\x10\x00\x12\x14\n\x10ZC_API_VERSION_2\x10\x01*G\n\rZCSwitchState\x12\x1a\n\x16ZC_SWITCH_STATE_OPENED\x10\x00\x12\x1a\n\x16ZC_SWITCH_STATE_CLOSED\x10\x01*\xa2\x01\n\rZCDeviceState\x12\x1d\n\x19ZC_DEVICE_STATE_UNDEFINED\x10\x00\x12\x1a\n\x16ZC_DEVICE_STATE_OPENED\x10\x01\x12\x1a\n\x16ZC_DEVICE_STATE_CLOSED\x10\x02\x12\x1b\n\x17ZC_DEVICE_STATE_STANDBY\x10\x03\x12\x1d\n\x19ZC_DEVICE_STATE_TRANSIENT\x10\x04*\x85\x02\n\x0bZCTripCause\x12\x16\n\x12ZC_TRIP_CAUSE_NONE\x10\x00\x12\x15\n\x11ZC_TRIP_CAUSE_EXT\x10\x01\x12\x18\n\x14ZC_TRIP_CAUSE_OCP_HW\x10\x02\x12\x1b\n\x17ZC_TRIP_CAUSE_OCP_CURVE\x10\x03\x12\x1d\n\x19ZC_TRIP_CAUSE_OCP_HW_TEST\x10\x04\x12\x15\n\x11ZC_TRIP_CAUSE_OTP\x10\x05\x12\x15\n\x11ZC_TRIP_CAUSE_UVP\x10\x06\x12\x15\n\x11ZC_TRIP_CAUSE_OVP\x10\x07\x12\x15\n\x11ZC_TRIP_CAUSE_UFP\x10\x08\x12\x15\n\x11ZC_TRIP_CAUSE_OFP\x10\t*P\n\x0fZCFlowDirection\x12\x1d\n\x19ZC_FLOW_DIRECTION_FORWARD\x10\x00\x12\x1e\n\x1aZC_FLOW_DIRECTION_BACKWARD\x10\x01*X\n\x0bZCDeviceCmd\x12\x16\n\x12ZC_DEVICE_CMD_OPEN\x10\x00\x12\x17\n\x13ZC_DEVICE_CMD_CLOSE\x10\x01\x12\x18\n\x14ZC_DEVICE_CMD_TOGGLE\x10\x02*\xd8\x01\n\tZCTempLoc\x12\x13\n\x0fZC_TEMP_LOC_AMB\x10\x00\x12\x15\n\x11ZC_TEMP_LOC_MCU_1\x10\x01\x12\x15\n\x11ZC_TEMP_LOC_MCU_2\x10\x02\x12\x15\n\x11ZC_TEMP_LOC_MCU_3\x10\x03\x12\x15\n\x11ZC_TEMP_LOC_MCU_4\x10\x04\x12\x15\n\x11ZC_TEMP_LOC_BRD_1\x10\x05\x12\x15\n\x11ZC_TEMP_LOC_BRD_2\x10\x06\x12\x15\n\x11ZC_TEMP_LOC_BRD_3\x10\x07\x12\x15\n\x11ZC_TEMP_LOC_BRD_4\x10\x08*\x81\x01\n\x0bZCCalibType\x12\x1b\n\x17ZC_CALIB_TYPE_VOLTAGE_1\x10\x00\x12\x1b\n\x17ZC_CALIB_TYPE_VOLTAGE_2\x10\x01\x12\x1b\n\x17ZC_CALIB_TYPE_CURRENT_1\x10\x02\x12\x1b\n\x17ZC_CALIB_TYPE_CURRENT_2\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'zc_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ZCAPIVERSION']._serialized_start=2635
  _globals['_ZCAPIVERSION']._serialized_end=2693
  _globals['_ZCSWITCHSTATE']._serialized_start=2695
  _globals['_ZCSWITCHSTATE']._serialized_end=2766
  _globals['_ZCDEVICESTATE']._serialized_start=2769
  _globals['_ZCDEVICESTATE']._serialized_end=2931
  _globals['_ZCTRIPCAUSE']._serialized_start=2934
  _globals['_ZCTRIPCAUSE']._serialized_end=3195
  _globals['_ZCFLOWDIRECTION']._serialized_start=3197
  _globals['_ZCFLOWDIRECTION']._serialized_end=3277
  _globals['_ZCDEVICECMD']._serialized_start=3279
  _globals['_ZCDEVICECMD']._serialized_end=3367
  _globals['_ZCTEMPLOC']._serialized_start=3370
  _globals['_ZCTEMPLOC']._serialized_end=3586
  _globals['_ZCCALIBTYPE']._serialized_start=3589
  _globals['_ZCCALIBTYPE']._serialized_end=3718
  _globals['_ZCVERSION']._serialized_start=22
  _globals['_ZCVERSION']._serialized_end=223
  _globals['_ZCTEMPERATURE']._serialized_start=225
  _globals['_ZCTEMPERATURE']._serialized_end=280
  _globals['_ZCSTATUS']._serialized_start=283
  _globals['_ZCSTATUS']._serialized_end=529
  _globals['_ZCCURVEPOINT']._serialized_start=531
  _globals['_ZCCURVEPOINT']._serialized_end=578
  _globals['_ZCCSOMMODCONFIG']._serialized_start=580
  _globals['_ZCCSOMMODCONFIG']._serialized_end=629
  _globals['_ZCCSOMCONFIG']._serialized_start=631
  _globals['_ZCCSOMCONFIG']._serialized_end=705
  _globals['_ZCCURVECONFIG']._serialized_start=707
  _globals['_ZCCURVECONFIG']._serialized_end=790
  _globals['_ZCOCPHWCONFIG']._serialized_start=792
  _globals['_ZCOCPHWCONFIG']._serialized_end=895
  _globals['_ZCOUVPCONFIG']._serialized_start=897
  _globals['_ZCOUVPCONFIG']._serialized_end=958
  _globals['_ZCOUFPCONFIG']._serialized_start=960
  _globals['_ZCOUFPCONFIG']._serialized_end=1021
  _globals['_ZCNOTIFCONFIG']._serialized_start=1023
  _globals['_ZCNOTIFCONFIG']._serialized_end=1056
  _globals['_ZCCALIBCONFIG']._serialized_start=1058
  _globals['_ZCCALIBCONFIG']._serialized_end=1114
  _globals['_ZCCONFIG']._serialized_start=1117
  _globals['_ZCCONFIG']._serialized_end=1363
  _globals['_ZCREQUESTVERSION']._serialized_start=1365
  _globals['_ZCREQUESTVERSION']._serialized_end=1397
  _globals['_ZCREQUESTSTATUS']._serialized_start=1399
  _globals['_ZCREQUESTSTATUS']._serialized_end=1430
  _globals['_ZCREQUESTDEVICECMD']._serialized_start=1432
  _globals['_ZCREQUESTDEVICECMD']._serialized_end=1479
  _globals['_ZCREQUESTSETCONFIG']._serialized_start=1481
  _globals['_ZCREQUESTSETCONFIG']._serialized_end=1528
  _globals['_ZCREQUESTGETCONFIGCURVE']._serialized_start=1530
  _globals['_ZCREQUESTGETCONFIGCURVE']._serialized_end=1592
  _globals['_ZCREQUESTGETCONFIGCSOM']._serialized_start=1594
  _globals['_ZCREQUESTGETCONFIGCSOM']._serialized_end=1632
  _globals['_ZCREQUESTGETCONFIGOCPHW']._serialized_start=1634
  _globals['_ZCREQUESTGETCONFIGOCPHW']._serialized_end=1673
  _globals['_ZCREQUESTGETCONFIGOUVP']._serialized_start=1675
  _globals['_ZCREQUESTGETCONFIGOUVP']._serialized_end=1713
  _globals['_ZCREQUESTGETCONFIGOUFP']._serialized_start=1715
  _globals['_ZCREQUESTGETCONFIGOUFP']._serialized_end=1753
  _globals['_ZCREQUESTGETCONFIGNOTIF']._serialized_start=1755
  _globals['_ZCREQUESTGETCONFIGNOTIF']._serialized_end=1794
  _globals['_ZCREQUESTGETCONFIGCALIB']._serialized_start=1796
  _globals['_ZCREQUESTGETCONFIGCALIB']._serialized_end=1849
  _globals['_ZCREQUESTGETCONFIG']._serialized_start=1852
  _globals['_ZCREQUESTGETCONFIG']._serialized_end=2178
  _globals['_ZCERROR']._serialized_start=2180
  _globals['_ZCERROR']._serialized_end=2203
  _globals['_ZCRESPONSE']._serialized_start=2206
  _globals['_ZCRESPONSE']._serialized_end=2341
  _globals['_ZCREQUEST']._serialized_start=2344
  _globals['_ZCREQUEST']._serialized_end=2558
  _globals['_ZCMESSAGE']._serialized_start=2560
  _globals['_ZCMESSAGE']._serialized_end=2633
# @@protoc_insertion_point(module_scope)