#  i4i.py
#  Copyright 2016 Marcus Hogue <marcus@hogue.me>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""A module for ZNC (IRC bouncer software)
Purpose: React to slaps and insults
"""
import znc
import random

class i4i(znc.Module):
    description = "Gonzobot insult autoresponder for ZNC"
    module_types = [znc.CModInfo.NetworkModule]
    responses = [
        '.insult','.slap',
    ]

    def OnLoad(self, args, message):
        return True

    def OnChanMsg(self, nick, channel, message):
        own_nick = self.GetNetwork().GetIRCNick().GetNick()
        own_host = self.GetNetwork().GetIRCNick().GetHostMask()
        channel = channel.GetName()
        nick = nick.GetNick()
        msg = str(message)
        if ('.insult' in msg or '.slap' in msg) and own_nick in msg:
            response = random.choice(self.responses)
            self.PutModule("Triggered when {0} said {1} on {2}".format(nick, msg, channel))
            self.GetNetwork().PutIRC("PRIVMSG {0} :{1} {2}".format(channel, response, nick))
        return znc.CONTINUE
