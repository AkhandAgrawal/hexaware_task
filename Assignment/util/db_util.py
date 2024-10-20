import pyodbc

class DBUtil:
    """Utility class for database operations."""

    @staticmethod
    def get_db_conn() -> pyodbc.Connection:
        """Establishes and returns a connection to the database."""
        try:
            connection_string = (
                "Driver={ODBC Driver 18 for SQL Server};"
                "Server=AKHAND\\SQLEXPRESS;"
                "Database=HMBank;"
                "TrustServerCertificate=yes;"
                "Trusted_Connection=yes;"
            )

            conn = pyodbc.connect(connection_string)
            print("Database connection successful!")
            return conn

        except Exception as e:
            print("Error while connecting to the DB: {}".format(e))
            raise  
