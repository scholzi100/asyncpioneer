MAX_VOLUME = 185
MAX_ZONE_VOLUME = 81

CONNECT_RETRY_SECS = 15
TIMEOUT_SECS = 10

DEFAULT_NAME = 'Pioneer AVR'
DEFAULT_PORT = 8102   # Most Pioneer AVRs now use 8102

CONF_SERIAL_BRIDGE      = 'serial_bridge'
CONF_DISABLED_SOURCES   = 'disabled_sources'
CONF_RADIO_STATIONS     = 'radio_stations'
CONF_LAST_RADIO_STATION = 'last_radio_station'
CONF_INPUTS             = 'inputs'

DATA_PIONEER = 'pioneer'
ATTR_SPEAKER = 'speaker'
ATTR_SPEAKER_CONFIG = 'speaker_config'
ATTR_STATION = 'station'
ATTR_DIM_DISPLAY = 'dim_display'
ATTR_HDMI_OUT = 'hdmi_out'
SERVICE_SELECT_SPEAKER = 'pioneer_select_speaker'
SERVICE_SELECT_SPEAKER_CONFIG = 'pioneer_select_speaker_config'
SERVICE_SELECT_RADIO_STATION = 'pioneer_select_radio_station'
SERVICE_DIM_DISPLAY = 'pioneer_dim_display'
SERVICE_SELECT_HDMI_OUT = 'pioneer_select_hdmi_out'
SERVICE_SELECT_SOUND_MODE = 'select_sound_mode'

SOURCE_ID_PHONO         = "00"
SOURCE_ID_CD            = "01"
SOURCE_ID_TUNER         = "02"
SOURCE_ID_DVD           = "04"
SOURCE_ID_TV            = "05"
SOURCE_ID_SAT           = "06"
SOURCE_ID_MULTI_CH      = "12"
SOURCE_ID_USB_DAC       = "13"
SOURCE_ID_BR            = "15"
SOURCE_ID_IPOD          = "17"
SOURCE_ID_HDMI1         = "19"
SOURCE_ID_HDMI2         = "20"
SOURCE_ID_HDMI3         = "21"
SOURCE_ID_HDMI4         = "22"
SOURCE_ID_HDMI5         = "23"
SOURCE_ID_HDMI6         = "24"
SOURCE_ID_BD            = "25"
SOURCE_ID_NETWORK       = "26"
SOURCE_ID_BT_AUDIO      = "33"
SOURCE_ID_HDMI7         = "34"
SOURCE_ID_INTERNET      = "38"
SOURCE_ID_PANDORA       = "41"
SOURCE_ID_MEDIA_SERVER  = "44"
SOURCE_ID_FAVORITES     = "45"

VALID_ZONE2_SOURCES =  [
    SOURCE_ID_DVD, SOURCE_ID_SAT, SOURCE_ID_BR, SOURCE_ID_NETWORK, 
    SOURCE_ID_INTERNET, "40", SOURCE_ID_PANDORA, SOURCE_ID_MEDIA_SERVER, 
    SOURCE_ID_FAVORITES, SOURCE_ID_IPOD, SOURCE_ID_USB_DAC, SOURCE_ID_TV, SOURCE_ID_CD, SOURCE_ID_TUNER, SOURCE_ID_BT_AUDIO]

VALID_HDZONE_SOURCES = [
    SOURCE_ID_DVD, SOURCE_ID_SAT, SOURCE_ID_BR, 
    SOURCE_ID_HDMI1, SOURCE_ID_HDMI2, SOURCE_ID_HDMI3, SOURCE_ID_HDMI4, SOURCE_ID_HDMI5, SOURCE_ID_HDMI6, SOURCE_ID_HDMI7,
    SOURCE_ID_BD, SOURCE_ID_NETWORK, 
    SOURCE_ID_INTERNET, SOURCE_ID_PANDORA, SOURCE_ID_MEDIA_SERVER, SOURCE_ID_FAVORITES, SOURCE_ID_IPOD, SOURCE_ID_USB_DAC]

DEFAULT_SOURCES = [SOURCE_ID_BD, SOURCE_ID_DVD, SOURCE_ID_SAT,
    SOURCE_ID_HDMI1, SOURCE_ID_HDMI2, SOURCE_ID_HDMI3, SOURCE_ID_HDMI4,
    SOURCE_ID_HDMI5, SOURCE_ID_HDMI6, SOURCE_ID_INTERNET, SOURCE_ID_MEDIA_SERVER,
    SOURCE_ID_FAVORITES, SOURCE_ID_IPOD, SOURCE_ID_TV, SOURCE_ID_CD,
    SOURCE_ID_TUNER,SOURCE_ID_BT_AUDIO]

CONF_INVALID_ZONES_ERR = "Invalid Zone (expected Zone2 or HDZone)"
CONF_VALID_ZONES = ["Main", "Zone2", "HDZone"]
CONF_ZONES = "zones"

ACCEPTED_SPEAKER_VALUES = ['A', 'B', 'A+B']
ACCEPTED_HDMI_OUT_VALUES = ['1+2 ON', '1 ON', '2 ON', '1/2 OFF']
ACCEPTED_SPEAKER_CONFIG_VALUES = ['Height', 'Wide', 'SPK B', 'Bi Amp', 'Zone 2', 'HDZone']

CONF_INVALID_ZONES_ERR = "Invalid Zone (expected Zone2 or HDZone)"
CONF_VALID_ZONES = ["Main", "Zone2", "HDZone"]
CONF_ZONES = "zones"

ATTR_CURRENT_RADIO_STATION = 'current_radio_station'
ATTR_CURRENT_SPEAKER = 'current_speaker'
ATTR_CURRENT_SPEAKER_CONFIG = 'current_speaker_config'
ATTR_CURRENT_HDMI_OUT = 'current_hdmi_out'
ATTR_CURRENT_SOUND_MODE = 'current_sound_mode'

LISTENING_MODES = {
	"0001": "STEREO",
	"0010": "STANDARD",
	"0009": "STEREO",
	"0011": "2ch",
	"0013": "PRO LOGIC2 MOVIE",
	"0018": "PRO LOGIC2x MOVIE",
	"0014": "PRO LOGIC2 MUSIC",
	"0019": "PRO LOGIC2x MUSIC",
	"0015": "PRO LOGIC2 GAME",
	"0020": "PRO LOGIC2x GAME",
	"0031": "PRO LOGIC2z HEIGHT",
	"0032": "WIDE SURROUND MOVIE",
	"0033": "WIDE SURROUND MUSIC",
	"0012": "PRO LOGIC",
	"0016": "Neo:6 CINEMA",
	"0017": "Neo:6 MUSIC",
	"0037": "Neo:X CINEMA",
	"0038": "Neo:X MUSIC",
	"0039": "Neo:X GAME",
	"0040": "Dolby Surround",
	"0021": "Multi ch",
	"0022": "DOLBY EX",
	"0023": "PRO LOGIC2x MOVIE",
	"0024": "PRO LOGIC2x MUSIC",
	"0034": "PRO LOGIC2z HEIGHT",
	"0035": "WIDE SURROUND MOVIE",
	"0036": "WIDE SURROUND MUSIC",
	"0025": "DTS-ES Neo",
	"0026": "DTS-ES matrix",
	"0027": "DTS-ES discrete",
	"0030": "DTS-ES 8ch discrete",
	"0043": "Neo:X CINEMA ",
	"0044": "Neo:X MUSIC",
	"0045": "Neo:X GAME",
	"0050": "Dolby Surround",
	"0100": "ADVANCED SURROUND",
	"0101": "ACTION",
	"0103": "DRAMA",
	"0118": "ADVANCED GAME",
	"0117": "SPORTS",
	"0107": "CLASSICAL",
	"0110": "ROCK/POP",
	"0112": "EXTENDED STEREO",
	"0003": "Front Stage Surround Advance",
	"0200": "ECO MODE",
	"0212": "ECO MODE 1",
	"0213": "ECO MODE 2",
	"0153": "RETRIEVER AIR",
	"0113": "PHONES SURROUND",
	"0005": "AUTO SURR/STREAM DIRECT",
	"0006": "AUTO SURROUND",
	"0151": "Auto Level Control",
	"0007": "DIRECT",
	"0008": "PURE DIRECT",
	"0152": "OPTIMUM SURROUND"
}