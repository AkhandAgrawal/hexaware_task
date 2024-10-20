class NullPointerException(Exception):
    """Exception raised for null reference errors."""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
