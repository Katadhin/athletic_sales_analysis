import pandas as pd

# Define a function to format columns as dollars
def format_to_dollars(df, column_name):
    df[column_name] = df[column_name].apply(lambda x: f'${x:,.2f}')
    return df

# Read CSV files into DataFrames
sales_2020_df = pd.read_csv('Resources/athletic_sales_2020.csv')
sales_2021_df = pd.read_csv('Resources/athletic_sales_2021.csv')

# Combine DataFrames
combined_sales_df = pd.concat([sales_2020_df, sales_2021_df]).reset_index(drop=True)

# Convert 'invoice_date' to datetime
combined_sales_df['invoice_date'] = pd.to_datetime(combined_sales_df['invoice_date'], format='%m/%d/%y')

# Determine Which Region Sold the Most Products
region_product_sales_df = combined_sales_df.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Total_Products_Sold'})
region_product_sales_df.sort_values('Total_Products_Sold', ascending=False, inplace=True)
print("\nTop 5 Regions by Product Sales:")
print(region_product_sales_df.head())

# Determine Which Region Had the Highest Sales
region_sales_df = combined_sales_df.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index().rename(columns={'total_sales': 'Total_Sales'})
region_sales_df = format_to_dollars(region_sales_df, 'Total_Sales')
region_sales_df.sort_values('Total_Sales', ascending=False, inplace=True)
print("\nTop 5 Regions by Total Sales:")
print(region_sales_df.head())

# Determine Which Retailer Had the Highest Sales
retailer_sales_df = combined_sales_df.groupby('retailer')['total_sales'].sum().reset_index().rename(columns={'total_sales': 'Total_Sales'})
retailer_sales_df = format_to_dollars(retailer_sales_df, 'Total_Sales')
retailer_sales_df.sort_values('Total_Sales', ascending=False, inplace=True)
print("\nTop 5 Retailers by Total Sales:")
print(retailer_sales_df.head())

# Determine Which Retailer Sold the Most Women's Athletic Footwear
womens_footwear_df = combined_sales_df[combined_sales_df['product'] == "Women's Athletic Footwear"]
retailer_womens_footwear_df = womens_footwear_df.groupby('retailer')['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
retailer_womens_footwear_df.sort_values('Womens_Footwear_Units_Sold', ascending=False, inplace=True)
print("\nTop 5 Retailers for Women's Athletic Footwear Sales:")
print(retailer_womens_footwear_df.head())

# Determine the Day with the Most Women's Athletic Footwear Sales
daily_sales_df = womens_footwear_df.pivot_table(index='invoice_date', values='total_sales', aggfunc='sum').rename(columns={'total_sales': 'Total_Sales'})
daily_sales_df = format_to_dollars(daily_sales_df.resample('D').sum(), 'Total_Sales')
daily_sales_df.sort_values('Total_Sales', ascending=False, inplace=True)
print("\nTop Days for Women's Athletic Footwear Sales:")
print(daily_sales_df.head())

# Determine the Week with the Most Women's Athletic Footwear Sales
weekly_sales_df = womens_footwear_df.pivot_table(index='invoice_date', values='total_sales', aggfunc='sum').rename(columns={'total_sales': 'Total_Sales'})
weekly_sales_df = format_to_dollars(weekly_sales_df.resample('W').sum(), 'Total_Sales')
weekly_sales_df.sort_values('Total_Sales', ascending=False, inplace=True)
print("\nTop Weeks for Women's Athletic Footwear Sales:")
print(weekly_sales_df.head())
