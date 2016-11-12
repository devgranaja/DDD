import uuid


# ======================================================================================================================
# Universally Unique Identifier
#
class UniqueId:

    @staticmethod
    def id():
        return uuid.uuid4().hex
