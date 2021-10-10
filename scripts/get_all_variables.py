#
#   Simple script to:
#     - Retrieve the list of Devices known to an instance of the CirCarLife engine
#     - Retrieve the list of Variables known to each Device
#     - Retrieve the properties of each Variable
#
#   Assumes that 'evse' is the hostname of a Circontrol CCL-WBM-SMART or similar EVSE unit
#
#   Imports
import requests
from xml.etree import ElementTree
#
#   Constants
HTTP_STATUS_OK = 200
#
#   Global Variables
api_url_base = 'http://evse/services/'
#
#   Function to get the current Value for the specified Variable
def get_value_for_variable(variable):
    response = requests.get(api_url_base + 'user/values.xml', params={'var': variable})
    if response.status_code != HTTP_STATUS_OK:
        raise SystemExit('API call not successful; HTTP Status = ' + str(response.status_code))
    
    root = ElementTree.fromstring(response.content)
    for variable in root:
        for var_child in variable:
            if var_child.tag == 'value':
                return(var_child.text)

    return None


devices = []
variables = []

#   Get the names of the Devices known to this CirCarLife Engine
response = requests.get(api_url_base + 'chargePointsInterface/devices.xml')
if response.status_code != HTTP_STATUS_OK:
    raise SystemExit('API call not successful; HTTP Status = ' + str(response.status_code))

#   Build a List of the Device names from the 'id' elements in the XML response
devices_root = ElementTree.fromstring(response.content)
for child in devices_root:
    if child.tag == 'id':
        devices.append(child.text)

#   Iterate over all the Devices
for device in devices:

    #   Get the names of the Variables for this Device
    response = requests.get(api_url_base + 'chargePointsInterface/deviceInfo.xml',
                            params={'id': device})
    if response.status_code != HTTP_STATUS_OK:
        raise SystemExit('API call not successful; HTTP Status = ' + str(response.status_code))

    #   Build a List of the Variable names from the 'var' elements in the XML response
    devicesInfo_root = ElementTree.fromstring(response.content)
    for device_info in devicesInfo_root:
        for child in device_info:
            if child.tag == 'var':
                #   The names of the Variables already have the Device name as a prefix; no need to disabmiguate
                variables.append(child.text)


#   Iterate over all the Variables
for variable in variables:

    #   Get the properties for this Variable
    response = requests.get(api_url_base + 'user/varInfo.xml', params={'var': variable})
    if response.status_code != HTTP_STATUS_OK:
        raise SystemExit('API call not successful; HTTP Status = ' + str(response.status_code))

    #   Check if this Variable has a Value we can interrogate
    varInfo_root = ElementTree.fromstring(response.content)
    for var in varInfo_root:
        var_title = ''
        var_units = ''
        var_value = None
        for child in var:
            if child.tag == 'title':
                var_title = child.text
            if child.tag == 'measureUnits':
                var_units = child.text
            if child.tag == 'hasValue':
                if child.text == 'T':
                    var_value = get_value_for_variable(variable)

        #   Print a summary line                   
        print(variable + '\t' + var_title + '\t', end='')
        print(var_value, end='')
        print('\t', end='')
        print(var_units)
