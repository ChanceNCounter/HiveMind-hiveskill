import json

import typing


class HiveSkill:
    """ HiveMind's device-side equivalent of a Mycroft Skill, using
        decorators similar to Adapt. If you aren't familiar with those
        APIs, go check out Mycroft's Hello World Skill tutorial. That's
        all the background you need.
    """

    author_name: str
    skill_name: str
    actions: typing.Dict[int, str]  # Master tracks Node's Skill and Action
    # dictionaries, so it can issue calls
    # to HiveSkill actions in the messaging
    # protocol, using the smallest int that
    # can represent all your node's Skill and
    # Action indices. This reduces the size of
    # your payload to the data which is
    # needed *by* the HiveSkill to execute
    # the Action.

    def __init__(self):
        # Register this skill in the node's numeral-indexed Skill dict.
        # If the node is already running when the skill is installed/started,
        # compress and send the new skill directory to this node's master.

        # The dict of available Actions is housed in this HiveSkill's res
        # folder, generated by the author, rather than at runtime. This avoids
        # the need to sync immutable data with master every time the node is
        # restarted, or updates.
        pass

    def parse_instruction(self, action_id: int):
        eval("self." + self.actions[action_id])
