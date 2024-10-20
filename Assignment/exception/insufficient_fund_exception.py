class InsufficientFundException(Exception):
    """Exception raised for errors in the withdrawal of funds."""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
