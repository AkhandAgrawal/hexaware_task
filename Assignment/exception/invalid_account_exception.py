class InvalidAccountException(Exception):
    """Exception raised for invalid account operations."""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
