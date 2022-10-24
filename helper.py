def fetch_production_tally(df,year,country):
    production_tally = df[['Year','County','Production']]
    if year == 'Overall' and country == 'Overall':
        temp_df = production_tally
    if year == 'Overall' and country != 'Overall':
        temp_df = production_tally[production_tally['County'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = production_tally[production_tally['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = production_tally[(production_tally['Year'] == int(year)) & (production_tally['County'] == country)]

    x = temp_df.groupby('County')[['Year', 'County', 'Production']].value_counts().sort_values(
        ascending=False).reset_index()
   # x=temp_df
    x = x.sort_values('Production', ascending=False)
    x = x[['Year','County','Production']]
    x['Production'] = x['Production'].astype(int)

    return x

def production_tally(df):
    production_tally = df.iloc[:, [0, 1, 4]]
    production_tally = production_tally.groupby('County')[['Year', 'County', 'Production']].value_counts().sort_values(
        ascending=False).reset_index()
    production_tally = production_tally.sort_values('Production', ascending=False).reset_index()
    production_tally = production_tally.iloc[:, [1, 2, 3]]
    return production_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    country = df['County'].unique().tolist()
    country.sort()
    country.insert(0, 'Overall')
    return years,country

def over_all_production(df):
    year = df.groupby('Year').max().reset_index()
    return year

def top_10_producer(df):
    production_tally = df.iloc[:, [0, 1, 4]]
    total_pro = (production_tally.groupby(['County', 'Year']).first().groupby('County').sum())
    total_pro = (total_pro.sort_values(by='Production', ascending=False)).reset_index()
    top10 = total_pro.head(10)
    return top10

def cheepest_price(df):
    min_value1 = df.iloc[:, [0, 1, 5]]
    min_value = min_value1[min_value1['Price(Dollars/Unit)'] == min_value1['Price(Dollars/Unit)'].min()]
    min_value['Price(Dollars/Unit)']=min_value['Price(Dollars/Unit)'].astype(int)
    return min_value

def costliest_price(df):
    min_value1 = df.iloc[:, [0, 1, 5]]
    max_value = min_value1[min_value1['Price(Dollars/Unit)'] == min_value1['Price(Dollars/Unit)'].max()]
    max_value['Price(Dollars/Unit)']=max_value['Price(Dollars/Unit)'].astype(int)
    return max_value


def fetch_price_tally(df,year, country):
    price_tally = df.iloc[:, [0, 1, 5]]
    if year == 'Overall' and country == 'Overall':
        temp_df = price_tally
    if year == 'Overall' and country != 'Overall':
        temp_df = price_tally[price_tally['County'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = price_tally[price_tally['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = price_tally[(price_tally['Year'] == int(year)) & (price_tally['County'] == country)]

    x = temp_df.groupby('County')[['Year', 'County', 'Price(Dollars/Unit)']].value_counts().sort_values(
        ascending=False).reset_index()
    x = x.sort_values('Price(Dollars/Unit)', ascending=False).reset_index()
    x = x.iloc[:, [1, 2, 3]]
    return x