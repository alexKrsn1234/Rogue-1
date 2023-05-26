from Equipment import Equipment

class Wearable(Equipment):
    """A wearable equipment."""
    def __init__(self, name, place, effect, abbrv="", use=None):
        Equipment.__init__(self, name, abbrv, use)
        self.place = place
        self.effect = effect