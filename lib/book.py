class Book:
    """A class representing a book in the bookstore."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Getter for page_count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Setter for page_count. Ensures value is an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = value

    def turn_page(self):
        """Simulates turning a page in the book."""
        print("Flipping the page...wow, you read fast!")