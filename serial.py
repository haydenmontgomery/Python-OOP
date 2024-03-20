"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """
        Initializer for the SerialGenerator class. Starts at start
        """
        self.start = start
        self.serial = start

    def __repr__(self):
        """
        Representation string
        """
        return f"SerialGenerator start={self.start} serial={self.serial}"
    
    def generate(self):
        """
        Instance method that generates the next serial number. Essentially serial += 1
        """
        self.serial += 1
        return self.serial - 1
    
    def reset(self):
        """
        Instance methos that resets the serial back to the start number
        """
        self.serial = self.start
        return