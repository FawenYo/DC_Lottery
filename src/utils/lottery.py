import copy
import logging
import random

from utils.database import Database


class Lottery:
    def register(self, name: str):
        db = Database()
        db.insert(name=name)

    def unregister(self, name: str):
        db = Database()
        db.delete(name=name)

    def start(self):
        members = self.get_members()
        logging.debug(f"members: {members}")
        _members = copy.deepcopy(members)

        result = {}

        for receiver in members:

            def random_sender(receiver):
                sender = random.choice(_members)
                if receiver != sender:
                    return sender
                else:
                    return random_sender(receiver)

            sender = random_sender(receiver)
            result[receiver] = sender
            _members.remove(sender)
        return result

    def get_members(self):
        db = Database()
        origin_members = db.select()
        members = []
        for each in origin_members:
            members.append(each[0])
        return members
