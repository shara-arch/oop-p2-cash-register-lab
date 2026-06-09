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
  