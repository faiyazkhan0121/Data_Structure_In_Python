class Book:
    # Corrected parameter spelling and consistency
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        
    # Corrected function definition and discount calculation logic
    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

# Creating object
b1 = Book("Python Basic", "John Smith", 500)
b1.display()

# Applying a 10% discount
b1.discount(10)

print("\nAfter Discount:")
b1.display()