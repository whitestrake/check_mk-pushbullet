#!/usr/bin/python

register_notification_parameters("pushbullet.py",
    Dictionary(
        optional_keys = [],
        elements = [
            ( "push_token",
              TextAscii(
                title = _("Pushbullet Token"),
                help = _("Your Pushbullet API token, available from https://www.pushbullet.com/#settings/account")
              ),
            ),
            ( "push_channel",
              TextAscii(
                title = _("Channel Tag"),
                help = _("The channel tag, available from https://www.pushbullet.com/#settings/channels")
              ),
            ),
        ])
)
