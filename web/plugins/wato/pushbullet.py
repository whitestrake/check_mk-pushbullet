#!/usr/bin/python

register_notification_parameters("xmpp.pl",
    Dictionary(
        elements = [
            ( "push_token",
              TextAscii(
                title = _("Pushbullet Token"),
                help = _("Your Pushbullet API token, available from https://www.pushbullet.com/#settings/account")
              ),
            ),
            ( "user",
              TextAscii(
                title = _("Username/JID"),
                help = _("The channel tag, available from https://www.pushbullet.com/#settings/channels")
              ),
            ),
        ])
)
