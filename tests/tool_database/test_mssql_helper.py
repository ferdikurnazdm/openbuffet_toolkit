import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import unittest
from openbuffet_toolkit.tool_database.mssql_helper import MSSQLHelper

class TestMSSQLHelperIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = MSSQLHelper(
            server="your_server_name", 
            database="your_database_name",
            user="your_username",
            password="your_password", 
            trusted_connection=False #True: windows authentication, False: sql authentication
            )

        # 1. Tabloyu oluştur
        cls.db.execute_non_query("""
            CREATE TABLE TestCagrilar (
                Id INT PRIMARY KEY IDENTITY(1,1),
                Konu NVARCHAR(255),
                Mesaj NVARCHAR(MAX),
                Tarih DATETIME
            );
        """)

        # 2. Dummy veri ekle
        cls.db.execute_non_query("""
            INSERT INTO TestCagrilar (Konu, Mesaj, Tarih) VALUES (?, ?, GETDATE());
        """, ["Test Konusu", "Bu bir test mesajıdır."])

    def test_read_dummy_data(self):
        """Dummy veriyi sorgulayıp doğrular"""
        result = self.db.execute_query("SELECT * FROM TestCagrilar WHERE Konu = ?", ["Test Konusu"])
        self.assertTrue(len(result) == 1)
        self.assertEqual(result[0]["Konu"], "Test Konusu")
        self.assertEqual(result[0]["Mesaj"], "Bu bir test mesajıdır.")

    @classmethod
    def tearDownClass(cls):
        # 3. Tabloyu kaldır
        cls.db.execute_non_query("DROP TABLE TestCagrilar;")
        cls.db.close()


if __name__ == "__main__":
    unittest.main()
