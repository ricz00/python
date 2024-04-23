import tkinter as tk

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory System")

        self.inventory = {}

        self.label_item = tk.Label(master, text="Item:")
        self.label_item.grid(row=0, column=0, padx=5, pady=5)
        self.entry_item = tk.Entry(master)
        self.entry_item.grid(row=0, column=1, padx=5, pady=5)

        self.label_quantity = tk.Label(master, text="Quantity:")
        self.label_quantity.grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantity = tk.Entry(master)
        self.entry_quantity.grid(row=1, column=1, padx=5, pady=5)

        self.button_add = tk.Button(master, text="Add Item", command=self.add_item)
        self.button_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.button_display = tk.Button(master, text="Display Inventory", command=self.display_inventory)
        self.button_display.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.label_output = tk.Label(master, text="")
        self.label_output.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()

        if item and quantity:
            quantity = int(quantity)
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            self.label_output.config(text=f"{quantity} {item}(s) added to inventory.")
        else:
            self.label_output.config(text="Please enter both item and quantity.")

    def display_inventory(self):
        inventory_text = "Current Inventory:\n"
        for item, quantity in self.inventory.items():
            inventory_text += f"{item}: {quantity}\n"
        self.label_output.config(text=inventory_text)


def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
