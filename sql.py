test_select = ('''
  SELECT total_box_office
  FROM petl1.AnnualTicketsSales;
''')


test_CreateSchema=(''' create schema if not exists petl1''')

test_CreateAnnualTicketsSalesTable =(''' create table if not exists petl1.AnnualTicketsSales(
YEAR text,
TICKETS_SOLD TEXT,
TOTAL_BOX_OFFICE TEXT,
TOTAL_INFLATION_ADJUSTED_BOX_OFFICE TEXT,
AVERAGE_TICKET_PRICE varchar)
''')

test_CreateHighestGrossersTable = ('''create table if not exists petl1.HighestGrossers(
                                   year text,
                                   movie text,
                                   genre text,
                                   mpaa_rating text,
                                   distributor text,
                                   total_for_year text,
                                   total_in_2019_dollars text,
                                   tickets_sold text
                                   )''')

test_CreatePopularCreativeTypes=(''' create table if not exists petl1.popularCreativeTypes(
rank text,
creative_types text,
movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopDistributors=(''' create table if not exists petl1.TopDistributors(
rank text,
distributors text,
movies text,
total_gross text,
average_gross text,
market_share text
)
''')

test_CreateTopGenres=(''' create table if not exists petl1.TopGenres(
rank text,
genres text,
movies text,
total_gross  text,
average_gross text,
market_share text
)
''')
test_CreateTopGrossingRatings=('''create table if not exists petl1.TopGrossingRatings(
rank text,
Mpaa_ratings text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopGrossingSourceTable=('''create table if not exists petl1.TopGrossingSources(
rank text,
sources text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopProductionMethodsTable=('''create table if not exists petl1.TopProductionMethods(
rank text,
production_methods text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateWideReleasesCount=(''' create table if not exists petl1.WideReleasesCount(
year text,
Warner_Bros text,
walt_disney text,
"20th_Century_fox" text,
paramount text,
sony_pictures text,
universal text,
total_major_6 text,
total_other_studios text)
''')