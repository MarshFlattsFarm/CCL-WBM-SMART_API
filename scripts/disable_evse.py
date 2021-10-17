#
#   Simple script to be run at about 05:00, after the end of the Octopus Go low-tariff period
#     - Puts an EVSE into the 'Disabled' state
#
#   Assumes that 'evse' is the hostname of a Circontrol EVSE unit
#
#   Imports
import urllib
import requests
from xml.etree import ElementTree
#
#   Constants
HTTP_STATUS_OK = 200
HTTP_STATUS_NO_CONTENT = 204
#
#   Global Variables
api_url_base = 'http://evse/services/user/'
#
#   Function to Get the current Value for the specified Variable
def get_variable(variable):
    """Return the Value of a Circontrol EVSE Variable.
    
    Note that the Value is always returned as a String, so something like a boolean 'True'
    is actually returned as '1.000000' (that's six zeros)
    """
    #   Some of the Variable names have embedded spaces which need converting to '%20'
    #   By default, these get converted to '+' which doesn't work
    quoted_params = urllib.parse.urlencode({'var': variable}, quote_via=urllib.parse.quote)

    #   Call the API to get the XML containing the value
    response = requests.get(api_url_base + 'values.xml', params=quoted_params)
    if response.status_code != HTTP_STATUS_OK:
        raise SystemExit('API GET not successful; HTTP Status = ' + str(response.status_code))
    
    #   Parse and return the value
    root = ElementTree.fromstring(response.content)
    for variable in root:
        for var_child in variable:
            if var_child.tag == 'value':
                return(var_child.text)

    #   There's probably never a case when the API worked but the XML doesn't contain the value,
    #   but if that does ever happen return None
    return None
#
#   Function to Set a new value for the specified Variable
def set_variable(variable, value):
    """Set the Value of a Circontrol EVSE Variable.
    
    Specify the fully-qualified Variable name, including the Device name (before the first '.')
    """
    #   Create the XML data ready for the API call
    root = ElementTree.Element('forceVariables')
    forceVar = ElementTree.SubElement(root, 'forceVar')
    forceName = ElementTree.SubElement(forceVar, 'forceName')
    forceValue = ElementTree.SubElement(forceVar, 'forceValue')
    forceName.text = variable
    forceValue.text = str(value)
    xmldata = ElementTree.tostring(root)

    #   Extract the Device name prefix from the Variable (up to the first '.')
    device = variable.split('.')[0]
    #   Some of the Device names have embedded spaces which need converting to '%20'
    #   By default, these get converted to '+' which doesn't work
    quoted_params = urllib.parse.urlencode({'id': device}, quote_via=urllib.parse.quote)
    #   Call the API to set the value
    response = requests.put(api_url_base + 'forceVariables.xml', params=quoted_params, data=xmldata)
    if response.status_code != HTTP_STATUS_NO_CONTENT:
        raise SystemExit('API PUT not successful; HTTP Status = ' + str(response.status_code))
    return None

#   MAIN PROGRAM

#   In general, we just want to set the EVSE to 'Disabled'
#   Might consider something more elegant if there is a vehicle connected *and charging*
#   But given that a full charge on the 94Ah i3 takes about 4.5 hours at 32A,
#   there's little chance of that happening after 05:00

#   Just Disable the EVSE
set_variable('EVSE.PLUG.ENABLE', 0)
