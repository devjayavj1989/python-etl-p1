test_select = ('''
  SELECT total_box_office
  FROM pet1.AnnualTicketsSales;
''')

test_insert = ('''
  INSERT INTO public.test_table
  VALUES(%s);
''')
test_CreateSchema=(''' create schema pet1''')

test_CreateAnnualTicketsSalesTable =(''' create table pet1.AnnualTicketsSales(
YEAR text,
TICKETS_SOLD TEXT,
TOTAL_BOX_OFFICE TEXT,
TOTAL_INFLATION_ADJUSTED_BOX_OFFICE TEXT,
AVERAGE_TICKET_PRICE varchar,
null_column text)
''')

test_CreateHighestGrossersTable = ('''create table pet1.HighestGrossers(
                                   year text,
                                   movie text,
                                   genre text,
                                   mpaa_rating text,
                                   distributor text,
                                   total_for_year text,
                                   total_in_2019_dollars text,
                                   tickets_sold text
                                   )''')

test_CreatePopularCreativeTypes=(''' create table pet1.popularCreativeTypes(
rank text,
creative_types text,
movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopDistributors=(''' create table pet1.TopDistributors(
rank text,
distributors text,
movies text,
total_gross text,
average_gross text,
market_share text
)
''')

test_CreateTopGenres=(''' create table pet1.TopGenres(
rank text,
genres text,
movies text,
total_gross  text,
average_gross text,
market_share text
)
''')
test_CreateTopGrossingRatings=('''create table pet1.TopGrossingRatings(
rank text,
Mpaa_ratings text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopGrossingSourceTable=('''create table pet1.TopGrossingSources(
rank text,
sources text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateTopProductionMethodsTable=('''create table pet1.TopProductionMethods(
rank text,
production_methods text,
Movies text,
total_gross text,
average_gross text,
market_share text
)''')

test_CreateWideReleasesCount=(''' create table pet1.WideReleasesCount(
year text,
Warner_Bros text,
walt_disney text,
"20th_Century_fox" text,
paramount text,
sony_pictures text,
universal text,
total_major_6 text,
total_other_studios text,
null_column text
)
''')