
import re
import random

import supybot.utils as utils
from supybot.commands import *
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Lunch(callbacks.Plugin):

    _responses = {'quick': ['Cafe Mercato', 'Cafe Duke', 'Han\'s Deli',
                               'Subway', 'Bite', 'Pinche Taqueria',
                               'Chipotle', 'Cosi', 'Fresh Inc', 'Qdoba' ],
                  'slow': ['Boyd Thai', 'Kelly and Ping',
                               'Peep', 'Burger Creations',
                               'Five Guys', 'Cafe Habana',
                               'Parm', 'High Heat', 'Grey Dog',
                               'Smile', 'Pops of Brooklyn', 'Cafetasia'
                               'Gonzalez y Gonzalez', 'Brad\'s', 'Potbelly'
                               'Apple', 'Num Pang', 'Pho 32', 'Mac Bar',
                               'delicatessan', 'calexico'],
                  'chipotle': ['Chipotle', ],
                 }

    def _checkTheList(self, lunchType):

        types = ['quick', 'slow', 'chipotle']

        if lunchType is None or len(lunchType) == 0  or lunchType not in types :
            lunchType = utils.iter.choice(types)

        return utils.iter.choice(self._responses[lunchType])

    def lunch(self, irc, msg, args, text):

        irc.reply(self._checkTheList(text))
    lunch = wrap(lunch, [additional('text')])

Class = Lunch


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
