# IBM_MQ_PageSets_Monitor

use only if you don't have ITCAM, otherwise it's better to set up a monitoring agent

Simple monitor for IBM MQ.

Simplest application for the working needs of our development site.

Think of it as an application to the repository: https://github.com/CrazyDoc/NJElib/tree/py3

Use a file entry to display the last hour(every 5min default, without a Date) and an entry in sqlite for the archive. Django server with a schedule in real-time(used JS and Ajax) mode, see the neighboring repository

in the future, it will be upgraded to the client-server architecture level(nje server on the monitoring host and client on the lpar), an application collecting values in a more typical way on the lpar side.

if you have questions, suggestions for follow-up function - you can write to the mail
