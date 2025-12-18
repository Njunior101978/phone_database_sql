import sqlite3

DB_NAME = "phone_database.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE phone (
            phone_id INT,
            country_code INT NOT NULL,
            phone_number INT NOT NULL,
            phone_type VARCHAR(12),
            PRIMARY KEY(phone_id)
        )
    """)
    
    conn.commit()
    conn.close()
    print("Table 'phone' created successfully.")


def select_phone_numbers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT phone_number
        FROM phone
        WHERE country_code = "US"
    """)
    
    results = cursor.fetchall()
    conn.close()
    
    print("Phone numbers with country_code = 'US':")
    for row in results:
        print(row[0])
    
    return results


def update_phone_type():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE phone
        SET phone_type = "MOBILE"
        WHERE phone_type = "CELLULAR"
    """)
    
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    
    print(f"Updated {rows_affected} row(s) from 'CELLULAR' to 'MOBILE'.")


def delete_phone_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM phone
        WHERE country_code = "XX"
    """)
    
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    
    print(f"Deleted {rows_affected} row(s) with country_code = 'XX'.")


def drop_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE phone")
    
    conn.commit()
    conn.close()
    print("Table 'phone' dropped successfully.")


def main():
    print("=" * 50)
    print("PHONE DATABASE OPERATIONS")
    print("=" * 50)
    print()
    
    print("1. Creating table...")
    create_table()
    print()
    
    print("2. Selecting phone numbers...")
    select_phone_numbers()
    print()
    
    print("3. Updating phone types...")
    update_phone_type()
    print()
    
    print("4. Deleting phone records...")
    delete_phone_records()
    print()
    
    print("5. Dropping table...")
    drop_table()
    print()
    
    print("All operations completed.")


if __name__ == "__main__":
    main()

