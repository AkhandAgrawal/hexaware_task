import re

class Customer:
    def __init__(self, customer_id, first_name, last_name, dob, email, phone_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = self.validate_email(email)
        self.phone_number = self.validate_phone(phone_number)
        self.address = address

    def validate_email(self, email):
        """Validate the email format using a regex pattern."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            raise ValueError("Invalid email format.")

    def validate_phone(self, phone_number):
        """Validate the phone number format using a regex pattern."""
        pattern = r'^\d{10}$'  
        if re.match(pattern, phone_number):
            return phone_number
        else:
            raise ValueError("Invalid phone number format. Must be 10 digits.")

    def __str__(self):
        return (f"Customer[ID={self.customer_id}, Name={self.first_name} {self.last_name}, "
                f"DOB={self.dob}, Email={self.email}, Phone={self.phone_number}, Address={self.address}]")
