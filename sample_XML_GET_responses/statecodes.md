
CHARGE_REQUEST_OK				0
CHARGE_REQUEST_SCHEDULED			1
CHARGE_REQUEST_NOT_SUPPORTED			-1
CHARGE_REQUEST_INVALID_DEVICE			-2
CHARGE_REQUEST_NOT_AVAILABLE			-3
CHARGE_REQUEST_INTERNAL_ERROR			-4
CHARGE_REQUEST_INVALID_PARAMETER		-5

CHARGE_DEVICE_ST_NO_INIT			-100
CHARGE_DEVICE_ST_UNKNOWN			-99
CHARGE_DEVICE_ST_DISABLED			-2
CHARGE_DEVICE_ST_ERROR				-1
CHARGE_DEVICE_ST_NONE				0
CHARGE_DEVICE_ST_WAITING_USER_CONNECT		1
CHARGE_DEVICE_ST_WAITING_USER_TAG		2

CHARGE_DEVICE_ERR_OK				0
CHARGE_DEVICE_ERR_CFG				1 << 0
CHARGE_DEVICE_ERR_READER			1 << 1
CHARGE_DEVICE_ERR_DISPLAY			1 << 2
CHARGE_DEVICE_ERR_TAMPER			1 << 3
CHARGE_DEVICE_ERR_TILT				1 << 4
CHARGE_DEVICE_ERR_SUPPLY			1 << 5
CHARGE_DEVICE_ERR_RCD				1 << 6
CHARGE_DEVICE_ERR_TEMPERATURE			1 << 7
CHARGE_DEVICE_ERR_OTHER				1 << 8
CHARGE_DEVICE_ERR_COMMUNICATION			1 << 9
CHARGE_DEVICE_ERR_TYPE				1 << 10
CHARGE_DEVICE_ERR_VERSION			1 << 11

CHARGE_DEVICE_EVE_STATE_BOOT			1
CHARGE_DEVICE_EVE_STATE_CHANGED			2  ? Device Automatic Heartbeat
CHARGE_DEVICE_EVE_STATE_CHANGED			3

CHARGE_PLUG_ST_NO_INIT				-100
CHARGE_PLUG_ST_UNKNOWN				-99
CHARGE_PLUG_ST_DISABLED				-2
CHARGE_PLUG_ST_ERROR				-1
CHARGE_PLUG_ST_AVAILABLE			0
CHARGE_PLUG_ST_RESERVED				1
CHARGE_PLUG_ST_WAITING_VEHICLE_CONNECTION	2
CHARGE_PLUG_ST_WAITING_ALLOWED_CHARGE		3
CHARGE_PLUG_ST_WAITING_SCHEDULE			4
CHARGE_PLUG_ST_WAITING_POWER			5
CHARGE_PLUG_ST_STARTING				6
CHARGE_PLUG_ST_RESUMING				7
CHARGE_PLUG_ST_CHARGING				8
CHARGE_PLUG_ST_PAUSING				9
CHARGE_PLUG_ST_PAUSED				10
CHARGE_PLUG_ST_STOPPING				11
CHARGE_PLUG_ST_WAITING_VEHICLE_DISCONNECTION	12

CHARGE_PLUG_ERR_OK				0
CHARGE_PLUG_ERR_CFG				1 << 0
CHARGE_PLUG_ERR_MASTER				1 << 1
CHARGE_PLUG_ERR_BEACON				1 << 2
CHARGE_PLUG_ERR_LOCK				1 << 3
CHARGE_PLUG_ERR_SUPPLY				1 << 4
CHARGE_PLUG_ERR_RCD				1 << 5
CHARGE_PLUG_ERR_CONTACTOR			1 << 6
CHARGE_PLUG_ERR_METER				1 << 7
CHARGE_PLUG_ERR_EMERGENCY			1 << 8
CHARGE_PLUG_ERR_TEMPERATURE			1 << 9
CHARGE_PLUG_ERR_EV_COMMUNICATION_DEVICE		1 << 10
CHARGE_PLUG_ERR_OTHER				1 << 11

CHARGE_PLUG_EVE_STATE_CHANGED			100
CHARGE_PLUG_EVE_CHARGE_START			101
CHARGE_PLUG_EVE_CHARGE_STOP			102

CHARGE_DENIED					-1
CHARGE_NOT_ALLOWED				0
CHARGE_ALLOWED					1

CHARGE_STOP_NONE				0
CHARGE_STOP_USER				1
CHARGE_STOP_SCHEDULER				2
CHARGE_STOP_CREDITS				3
CHARGE_STOP_DISCONNECT				4
CHARGE_STOP_REMOTE				5
CHARGE_STOP_TIMER				6
CHARGE_STOP_DISABLED				7
CHARGE_STOP_ERROR				8
CHARGE_STOP_VEHICLE_COMMUNICATION		9
CHARGE_STOP_VEHICLE_OVERCURRENT			10
