#!/usr/bin/env python
# Notify via PushBullet
import os, sys, urllib2, json
 
# Gather notification data
hostname=os.getenv('NOTIFY_HOSTNAME')
hostalias=os.getenv('NOTIFY_HOSTALIAS')
notification=os.getenv('NOTIFY_NOTIFICATIONTYPE')
if os.getenv('NOTIFY_SERVICEDESC') == '$SERVICEDESC$':
  # Host report
  service='Host'
  output=os.getenv('NOTIFY_HOSTOUTPUT')
  oldstate=os.getenv('NOTIFY_LASTHOSTSTATE')
  newstate=os.getenv('NOTIFY_HOSTSTATE')
else:
  # Service report
  service=os.getenv('NOTIFY_SERVICEDESC')
  output=os.getenv('NOTIFY_SERVICEOUTPUT')
  oldstate=os.getenv('NOTIFY_LASTSERVICESTATE')
  newstate=os.getenv('NOTIFY_SERVICESTATE')
 
# Configure push auth, details, and format
push_channel=os.getenv('NOTIFY_PARAMETER_push_token')
push_token=os.getenv('NOTIFY_PARAMETER_push_channel')
push_title=hostalias.upper()+' '+notification
push_body=service+' '+oldstate+' -> '+output+' ('+hostname+')'
 
# Set up request
push_url='https://api.pushbullet.com/v2/pushes'
push_header={'Access-Token' : push_token,
             'Content-Type' : 'application/json'}
push_data=json.dumps({'type'        : 'note',
                      'channel_tag' : push_channel,
                      'title'       : push_title,
                      'body'        : push_body})
 
# Send to PushBullet API
try:
  req=urllib2.Request(push_url,headers=push_header,data=push_data)
  urllib2.urlopen(req)
except urllib2.HTTPError as e:
  print e
