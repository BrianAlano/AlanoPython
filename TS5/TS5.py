class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            raise ValueError("Item ID already exists.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        self.items[item_id] = Item(item_id, name, description, price)

    def read_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        return self.items[item_id]

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        if name:
            self.items[item_id].name = name
        if description:
            self.items[item_id].description = description
        if price is not None:
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError("Price must be a non-negative number.")
            self.items[item_id].price = price

    def delete_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        del self.items[item_id]

    def list_items(self):
        return [str(item) for item in self.items.values()]

if __name__ == "__main__":
    manager = ItemManager()
    try:
        manager.create_item(1, "Laptop", "A high-end gaming laptop", 1500)
        manager.create_item(2, "Mouse", "Wireless mouse", 25)
        print("Items after creation:")
        print(manager.list_items())

        manager.update_item(1, price=1400)
        print("\nItems after update:")
        print(manager.list_items())

        manager.delete_item(2)
        print("\nItems after deletion:")
        print(manager.list_items())

    except ValueError as e:
        print(e)