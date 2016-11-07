class Value:

    def __init__(self, p):
            self.param = p

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
