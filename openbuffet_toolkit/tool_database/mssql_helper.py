import pyodbc
from typing import List, Dict, Any, Optional


class MSSQLHelper:
    """
    MSSQL veritabanı işlemleri için genel amaçlı bir yardımcı sınıftır.
    CRUD işlemleri ve stored procedure çağrılarını destekler.
    """

    def __init__(self, server: str, database: str, user: str = None, password: str = None,
                 driver: str = "ODBC Driver 17 for SQL Server", trusted_connection: bool = True):
        """
        MSSQLHelper sınıfını başlatır.

        Args:
            server (str): SQL Server adresi.
            database (str): Hedef veritabanı adı.
            user (str, optional): SQL kullanıcı adı (trusted_connection False ise gerekir).
            password (str, optional): SQL şifresi (trusted_connection False ise gerekir).
            driver (str): Kullanılacak ODBC sürücüsü.
            trusted_connection (bool): Windows Authentication kullanılıp kullanılmayacağı.
        """
        if trusted_connection:
            self.connection_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        else:
            self.connection_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        self.conn = None

    def connect(self):
        """
        MSSQL veritabanına bağlantı kurar (bağlantı yoksa yeni bağlantı oluşturur).

        Returns:
            pyodbc.Connection: Aktif bağlantı nesnesi.
        """
        if not self.conn:
            self.conn = pyodbc.connect(self.connection_str)
        return self.conn

    def execute_query(self, query: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
        """
        SELECT sorgusu çalıştırır ve sonuçları döner.

        Args:
            query (str): SQL sorgusu.
            params (List[Any], optional): Sorgu için parametre listesi.

        Returns:
            List[Dict[str, Any]]: Sorgu sonucu satırlar (sözlük listesi olarak).
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        return result

    def execute_non_query(self, query: str, params: Optional[List[Any]] = None) -> int:
        """
        INSERT, UPDATE veya DELETE gibi etki eden sorguları çalıştırır.

        Args:
            query (str): SQL sorgusu.
            params (List[Any], optional): Parametre listesi.

        Returns:
            int: Etkilenen satır sayısı.
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        affected = cursor.rowcount
        conn.commit()
        cursor.close()
        return affected

    def execute_stored_procedure(self, proc_name: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
        """
        Stored procedure çağırır ve sonuçları döner.

        Args:
            proc_name (str): Procedure adı.
            params (List[Any], optional): Procedure parametreleri.

        Returns:
            List[Dict[str, Any]]: Dönüş tablosu (eğer varsa).
        """
        conn = self.connect()
        cursor = conn.cursor()
        placeholders = ", ".join("?" for _ in (params or []))
        query = f"EXEC {proc_name} {placeholders}"
        cursor.execute(query, params or [])
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        return result

    def close(self):
        """
        Veritabanı bağlantısını kapatır.
        """
        if self.conn:
            self.conn.close()
            self.conn = None
