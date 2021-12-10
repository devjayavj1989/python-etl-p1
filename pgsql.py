import psycopg2
from config import pgsql_config
import csv

def query(query, values=None):
    # Connect to your postgres DB
    cursor = connect()

    # Execute a query
    if (values):
        cursor.execute(query, values)
    else:
        cursor.execute(query)
        # return query results
        return cursor.fetchall()
def csv_import():
     cursor1= connect()
     with open('/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv', 'r',newline='') as f:
         reader = csv.reader(f,delimiter=',')
         next(reader) # Skip the header row.
         for row in reader:
            row.pop()
            # print (row)
            cursor1.execute(
           "INSERT INTO petl1.AnnualTicketsSales VALUES (%s,%s,%s,%s,%s)",row)



def csv_import1():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/HighestGrossers.csv',
            'r') as f:
        reader = csv.reader(f,delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
          #  print(row)
           cursor1.execute("INSERT INTO petl1.HighestGrossers VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",row)

def csv_import2():
        cursor1 = connect()
        with open(
                '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/PopularCreativeTypes.csv',
                'r') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # Skip the header row.
            for row in reader:
                #  print(row)
                cursor1.execute("INSERT INTO petl1.PopularCreativeTypes VALUES (%s,%s,%s,%s,%s,%s)", row)


def csv_import3():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopDistributors.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
            #  print(row)
            cursor1.execute("INSERT INTO petl1.TopDistributors VALUES (%s,%s,%s,%s,%s,%s)", row)

def csv_import4():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGenres.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
            #  print(row)
            cursor1.execute("INSERT INTO petl1.TopGenres VALUES (%s,%s,%s,%s,%s,%s)", row)

def csv_import5():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingRatings.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
            #  print(row)
            cursor1.execute("INSERT INTO petl1.TopGrossingRatings VALUES (%s,%s,%s,%s,%s,%s)", row)

def csv_import6():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopGrossingSources.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
            #  print(row)
            cursor1.execute("INSERT INTO petl1.TopGrossingSources VALUES (%s,%s,%s,%s,%s,%s)", row)


def csv_import7():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/TopProductionMethods.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
            #  print(row)
            cursor1.execute("INSERT INTO petl1.TopProductionMethods VALUES (%s,%s,%s,%s,%s,%s)", row)

def csv_import8():
    cursor1 = connect()
    with open(
            '/Users/yorkmac040/PycharmProjects/jaya/mohan/python-etl-p1/datasets/hollywood-theatrical-market-synopsis-1995-to-2021/WideReleasesCount.csv',
            'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row.
        for row in reader:
          #print(row)
            row.pop()
            cursor1.execute("INSERT INTO petl1.WideReleasesCount VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

def Import_all():
    csv_import()
    csv_import1()
    csv_import2()
    csv_import3()
    csv_import4()
    csv_import5()
    csv_import6()
    csv_import7()
    csv_import8()

def connect():
    connection = psycopg2.connect(f"""
        host='{pgsql_config['host']}'
        dbname='{pgsql_config['dbname']}'
        user='{pgsql_config['user']}'
        password='{pgsql_config['password']}'
    """)

    # Configure connection
    connection.autocommit = True

    # Return connection cursor to perform database operations
    return connection.cursor()