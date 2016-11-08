class Value:

    def __init__(self, p):
            pass

    def __eq__(self, other):
        """Override the equality method to compare state (values) and
        behavior (class)
        """
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """Override the hashing method to hash state & behavior
        """
        return hash(tuple([self.__class__.__name__, tuple(sorted(self.__dict__.items()))]))
