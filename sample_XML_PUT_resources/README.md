The files in the sub-directories under this directory are example resources for the HTTP API on a Circontrol WallBox Smart (CCL-WBM-SMART) EVSE unit, running firware v2.3b.

These were created to support HTTP requests using the `wget` utility on a Linux OS, using commands like:

    $ cd services/user/
    $ wget --method=PUT --body-file='forceVariables.xml?id=Plug - Mode 3' http://evse/services/user/forceVariables.xml\?id=Plug%20-%20Mode%203

    ...
    HTTP request sent, awaiting response... 204 No Content
    ...
    ‘forceVariables.xml?id=Plug - Mode 3.1’ saved[0]

(where `evse` is the hostname of the CCL-WBM-SMART unit)

The XML has had newline characters and indentation added to make it easier to read. This is not required.
