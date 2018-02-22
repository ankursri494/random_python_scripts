import psycopg2


class PsqlDb:

    def __init__(self, db_credentials):
        self.db_credentials = db_credentials

    def __enter__(self):
        self.conn = psycopg2.connect(self.db_credentials)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


def main():
	db = "dbname=sampledb user=postgres password=postgres"
	with PsqlDb(db) as conn:
		cur = conn.cursor()
		query = input("Enter query to display result: ");
		print(query)
		cur.execute(query)
		print("\n\n\nResult Set:\n\n\n")
		row = cur.fetchone()
		while row:
			print(row)
			row = cur.fetchone()


if __name__ == '__main__':
	main()
