# Import Libraries and Dependencies
import pandas as pd

# Read the athletic_sales_2020.csv and athletic_sales_2021.csv CSV files into DataFrames.
sales_2020_df = pd.read_csv('Resources/athletic_sales_2020.csv')
sales_2021_df = pd.read_csv('Resources/athletic_sales_2021.csv')

# Print Column Names
print(sales_2020_df.columns)
print(sales_2021_df.columns)


# Set all numbers to display as dollars with two decimal places.
pd.options.display.float_format = '${:,.2f}'.format


# View the first five rows of the DataFrame with numbers formatted as dollars.
print("\nFirst Five Rows of 2020 Sales Data:")
print(sales_2020_df.head())



# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index formatted as dollars.
combined_sales_df = pd.concat([sales_2020_df, sales_2021_df]).reset_index(drop=True)

# Convert the "invoice_date" to a datetime datatype
combined_sales_df['invoice_date'] = pd.to_datetime(combined_sales_df['invoice_date'])

# Use groupby to show the number of products sold for each region, state, and city.
# Rename the "units_sold" column to "Total_Products_Sold".
grouped_sales_df = combined_sales_df.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Total_Products_Sold'})
print("\nProduct Sales by Region, State, and City:")
print(grouped_sales_df.head())

# Show the number products sold for region, state, and city using pivot table.
# Rename the "quantity" column to "Total_Products_Sold".
pivot_sales_df = combined_sales_df.pivot_table(index=['region', 'state', 'city'], values='units_sold', aggfunc='sum').reset_index().rename(columns={'units_sold': 'Total_Products_Sold'})
print("\nProduct Sales by Region, State, and City:")
print(pivot_sales_df.head())

#Determine the region with the most sales
# Use groupby to show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales".
grouped_sales_df = combined_sales_df.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index().rename(columns={'total_sales': 'Total_Sales'})
print("\nProduct Sales by Region, State, and City:")
print(grouped_sales_df.head())


# Show the total sales for the products sold for each region, state, and city using pivot table.
# Rename the "total_sales" column to "Total Sales".
pivot_sales_df = combined_sales_df.pivot_table(index=['region', 'state', 'city'], values='total_sales', aggfunc='sum').reset_index().rename(columns={'total_sales': 'Total_Sales'})
print("\nProduct Sales by Region, State, and City:")
print(pivot_sales_df.head())

# Determine which retailer had the highest sales.
# Use groupby to show the total sales for each retailer.
# Rename the "total_sales" column to "Total Sales".
grouped_sales_df = combined_sales_df.groupby(['retailer'])['total_sales'].sum().reset_index().rename(columns={'total_sales': 'Total_Sales'})
print("\nProduct Sales by Retailer:")
print(grouped_sales_df.head())


# Filter the sales data to get the women's athletic footwear sales data.
womens_athletic_footwear_sales = combined_sales_df[combined_sales_df['product'] == "Women's Athletic Footwear"]

# Now, womens_athletic_footwear_sales contains only the rows for Women's Athletic Footwear
womens_athletic_footwear_sales.head()
print("\nWomen's Athletic Footwear Sales:")
print(womens_athletic_footwear_sales.head())

# Show the total number of women's athletic footwear sold for each retailer, region, state, and city using groupby.
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womens_athletic_footwear_sales_retailer_df = womens_athletic_footwear_sales.groupby('retailer')['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_region_df = womens_athletic_footwear_sales.groupby('region')['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_state_df = womens_athletic_footwear_sales.groupby('state')['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_city_df = womens_athletic_footwear_sales.groupby('city')['units_sold'].sum().reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})

print("\nWomen's Athletic Footwear Sales by Retailer:")
print(womens_athletic_footwear_sales_retailer_df.head())
print("\nWomen's Athletic Footwear Sales by Region:")
print(womens_athletic_footwear_sales_region_df.head())
print("\nWomen's Athletic Footwear Sales by State:")
print(womens_athletic_footwear_sales_state_df.head())
print("\nWomen's Athletic Footwear Sales by City:")
print(womens_athletic_footwear_sales_city_df.head())

# Show the total number of women's athletic footwear sold for each retailer, region, state, and city using pivot table.
womens_athletic_footwear_sales_retailer_df = womens_athletic_footwear_sales.pivot_table(index='retailer', values='units_sold', aggfunc='sum').reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_region_df = womens_athletic_footwear_sales.pivot_table(index='region', values='units_sold', aggfunc='sum').reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_state_df = womens_athletic_footwear_sales.pivot_table(index='state', values='units_sold', aggfunc='sum').reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_city_df = womens_athletic_footwear_sales.pivot_table(index='city', values='units_sold', aggfunc='sum').reset_index().rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})



# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womens_athletic_footwear_sales_retailer_df = womens_athletic_footwear_sales_retailer_df.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_region_df = womens_athletic_footwear_sales_region_df.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_state_df = womens_athletic_footwear_sales_state_df.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
womens_athletic_footwear_sales_city_df = womens_athletic_footwear_sales_city_df.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})


# Show the top 5 retailers results.
print("\nWomen's Athletic Footwear Sales by Retailer:")
print(womens_athletic_footwear_sales_retailer_df.head())
print("\nWomen's Athletic Footwear Sales by Region:")
print(womens_athletic_footwear_sales_region_df.head())
print("\nWomen's Athletic Footwear Sales by State:")
print(womens_athletic_footwear_sales_state_df.head())


#Determine the day with the most women's athletic footwear sales.
# Use groupby to show the total sales for each day.
# Rename the "total_sales" column to "Total Sales".
grouped_sales_df = womens_athletic_footwear_sales.groupby(['invoice_date'])['total_sales'].sum().reset_index().rename(columns={'total_sales': 'Total_Sales'})
print("\nWomen's Athletic Footwear Sales by Day:")
print(grouped_sales_df.head())

# Resample the pivot table into daily bins, and get the total sales for each day.
sales_by_date_df = combined_sales_df.pivot_table(index='invoice_date', values='total_sales', aggfunc='sum').rename(columns={'total_sales': 'Total_Sales'})
sales_by_date_df = sales_by_date_df.resample('D').sum()
sales_by_date_df.head()




# Sort the resampled pivot table in ascending order on "Total Sales".
sales_by_date_df = sales_by_date_df.sort_values('Total_Sales', ascending=True)
sales_by_date_df.head(25)



# Resample the pivot table into weekly bins, and get the total sales for each week.
sales_by_date_df = combined_sales_df.pivot_table(index='invoice_date', values='total_sales', aggfunc='sum').rename(columns={'total_sales': 'Total_Sales'})
sales_by_date_df = sales_by_date_df.resample('W').sum()
sales_by_date_df.head()



# Sort the resampled pivot table in ascending order on "Total Sales".
sales_by_date_df = sales_by_date_df.sort_values('Total_Sales', ascending=True)
sales_by_date_df.head(25)
print("\nWomen's Athletic Footwear Sales by Day:")
print(sales_by_date_df.head())























# Show the top 5 results.






      









