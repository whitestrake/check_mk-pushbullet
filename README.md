# check_mk-pushbullet

This plugin for Check_MK contains a Python script designed to take advantage of the [Pushbullet API](https://docs.pushbullet.com/) to push alert notifications directly to your phone.

A major advantage of this method of notification is Pushbullet's channel system - when supplied with a user's API key and a channel tag, Check_MK can push notifications to channels that can be subscribed to by multiple other Pushbullet users. This allows for multiple tiers of alerts to be pushed to different groups of people.

Installation is handled via the MKP tool available with your Check_MK installation - more detail can be found at the [Check_MK Packages](https://mathias-kettner.com/checkmk_packaging.html) documentation.
