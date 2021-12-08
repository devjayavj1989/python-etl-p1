import sql
from pgsql import query
from pgsql import csv_import
from pgsql import csv_import1
from pgsql import csv_import2
from pgsql import csv_import3
from pgsql import csv_import4
from pgsql import csv_import5
from pgsql import csv_import6
from pgsql import csv_import7
from pgsql import csv_import8
#import pgsql
#from ast import literal_eval


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # insert data
   # query(sql.test_insert, ["My Insert!"]);

    # select data
    results = query(sql.test_select);
    print("results: ", results)
    #for i in results:
    #  string value = value+i
     # final= [int[s] for s in value.split() if s.isdigit()]
     # print(final)

    #query(sql.test_CreateWideReleasesCount,["creating table9"])
    #query(sql.test_CreateTopProductionMethodsTable,["creating table8"])
    #query(sql.test_CreateTopGrossingSourceTable,["creating table7"])
    #query(sql.test_CreateTopGrossingRatings,["creating table6"])
    #query(sql.test_CreateTopGenres,["creating Table5"])
    #query(sql.test_CreateTopDistributors,["Creating table4"])
   # query(sql.test_CreateSchema, ["creating schema"])
   # query(sql.test_CreateHighestGrossersTable, ["creating table1"])
    #query(sql.test_CreateAnnualTicketsSalesTable, ["creating table3"])

#csv_import8()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
