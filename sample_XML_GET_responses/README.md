
The files in the sub-directories under this directory are example responses from the HTTP API on a Circontrol WallBox Smart (CCL-WBM-SMART) EVSE unit, running firware v2.3b.

These were created by making HTTP requests using the `wget` utility on a Linux OS, using commands like:

    $ cd services/chargePointsInterface/
    $ wget --method=GET http://evse/services/chargePointsInterface/devices.xml
    ...
    HTTP request sent, awaiting response... 200 OK
    ...
    Saving to: 'devices.xml'
    ...

(where `evse` is the hostname of the CCL-WBM-SMART unit)

The XML has had newline characters and indentation added to make it easier to read.
