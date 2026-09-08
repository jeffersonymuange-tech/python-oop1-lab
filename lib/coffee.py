class Coffee:
    """A class representing a coffee item in the bookstore."""

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        """Getter for size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size. Ensures size is Small, Medium, or Large."""
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = None
        else:
            self._size = value

    def tip(self):
        """Adds a tip by increasing price by 1 and prints a thank-you message."""
        print("This coffee is great, here’s a tip!")
        self.price += 1