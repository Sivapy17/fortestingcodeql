# example.py

import os

# Unsafe hard-coded secret (for testing only)
AWS_SECRET_ACCESS_KEY = "AKIA1234567890TEST"  # fake key

# Example of SQL injection vulnerability
def get_user_data(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "';"
    return query
