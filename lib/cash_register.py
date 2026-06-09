#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        # Initialize attributes
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

        # Initializing via the setter property ensures validation occurs immediately
        self.discount = discount

  # Getter for discount
  @property
  def discount(self):
    return self._discount
  
# Setter for discount (Handles validation)
  @discount.setter
  def discount(self, value):
      if not isinstance(value, int) or not (0 <= value <= 100):
          print("Not valid discount")
          # If invalid initialization happens, we fall back to a safe default of 0
          self._discount = 0
      else:
        self._discount = value  
  # Method: Add Item
  def add_item(self, item, price, quantity=1):
    # Calculate the total cost for this transaction line item
    line_total = price * quantity
    self.total += line_total
        
    # Add the item name to the items list
    for _ in range(quantity):
      self.items.append(item)    
# Record the transaction breakdown as a dictionary
    transaction = {
      "item": item,
      "price": price,
      "quantity": quantity
      }
    self.previous_transactions.append(transaction) 

# Method: Apply Discount
  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
      print(f"Discount applied successfully! New total is: {self.total}")
      return self.total       
    else:
        #Prints a string error message that there is no discount to apply
      print("There is no discount to apply.")
    
# Method: Void Last Transaction
  def void_last_transaction(self):
    if not self.previous_transactions:
      print("No discount to void.")
      return
  # Remove the last recorded transaction dictionary
    last_tx = self.previous_transactions.pop()
        
    # Subtract the calculated line item price out of the running total
    tx_total = last_tx["price"] * last_tx["quantity"]
    self.total -= tx_total
        
    # Remove the item name string out of the items list
    if last_tx["item"] in self.items:
      self.items.remove(last_tx["item"])
    # Enforce clean floating-point reset if everything is cleared out
    if not self.items:
      self.total = 0.0