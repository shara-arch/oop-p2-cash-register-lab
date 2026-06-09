#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        # Initialize attributes
        self.total = 0.0
        self.items = []
        self.previous_transactions = []