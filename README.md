# Introduction

This GitHub repository contains information and examples relating to the 
[Circutor](https://circutor.com/en) [PowerStudio](http://circutor.es/en/products/measurement-and-control/energy-management-software/powerstudio-series-detail) HTTP & XML API implemented by some [Circontrol](https://www.circontrol.com/) EVSE units such as their [Wallbox Smart](https://circontrol.com/ev-charging/ac-wallbox/wallbox-smart/) series.

It seems that Circontrol used the Circutor PowerStudio SCADA environment to develop a PowerStudio SCADA *Application* called "CirCarLife" (sometimes abbreviated to CCL).
The Circontrol smart EVSE units run the CirCarLife *Engine* software (on the CCL1Mini processor board) and it is this Engine which implements the HTTP API.

The generic aspects of the PowerStudio SCADA API are covered in the documentation
available at: http://powerstudioscada.circutor.com/en/documents

This GitHub repository provides examples of the XML files returned by API calls to a CCL-WBM-SMART EVSE unit as well as some guidance on the specifics of the `chargePointsInterface` API.

Some of the information was taken from a Final Degree Project report (in Spanish) which is available for download from a couple of archive locations - use your favourite Internet search engine to look for reports on the subject of `MyCirCarLife`.
