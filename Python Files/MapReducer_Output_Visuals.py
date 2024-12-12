#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the output data
price_comparison = pd.read_csv('price_comparison.csv', delimiter='\t', names=['date', 'ratio'])
price_comparison['date'] = pd.to_datetime(price_comparison['date'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(price_comparison['date'], price_comparison['ratio'], label='Raw/Adjusted Close Ratio', color='blue')
plt.axhline(y=1, color='red', linestyle='--', label='Ratio = 1')
plt.xlabel('Date')
plt.ylabel('Ratio')
plt.title('Comparison of Raw and Adjusted Closing Prices')
plt.legend()
plt.show()


# In[2]:


# Load yearly average data
yearly_avg = pd.read_csv('yearly_avg_price.csv', delimiter='\t', names=['year', 'avg_close'])
yearly_avg['year'] = yearly_avg['year'].astype(int)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg['year'], yearly_avg['avg_close'], marker='o', color='green')
plt.xlabel('Year')
plt.ylabel('Average Closing Price (USD)')
plt.title('Yearly Average Closing Price of AAPL')
plt.grid(True)
plt.show()


# In[3]:


# Load the preprocessed data
preprocessed_data = pd.read_csv('preprocessed_data.csv')

# Plot
plt.figure(figsize=(18, 12))
plt.scatter(preprocessed_data['volume'], preprocessed_data['change_percent'], alpha=0.6, color='purple')
plt.xscale('log')  # Use log scale for better visualization of volume
plt.xlabel('Trading Volume')
plt.ylabel('Price Change (%)')
plt.title('Volume vs. Daily Price Change (%)')
plt.grid(False)
plt.show()


# In[17]:


print(preprocessed_data.columns)


# In[23]:


print(split_analysis.columns)


# In[31]:


# Make an explicit copy of the original DataFrame slice to avoid SettingWithCopyWarning
split_analysis = preprocessed_data[['28.7392.2', '0.0992', '1980-12-12']].copy()

# Ensure the relevant columns are numeric, using .loc to avoid SettingWithCopyWarning
split_analysis.loc[:, '28.7392.2'] = pd.to_numeric(split_analysis['28.7392.2'], errors='coerce')
split_analysis.loc[:, '0.0992'] = pd.to_numeric(split_analysis['0.0992'], errors='coerce')

# Rename '1980-12-12' to 'date' and ensure it is in datetime format
split_analysis.loc[:, 'date'] = pd.to_datetime(split_analysis['1980-12-12'], errors='coerce')

# Calculate the split ratio
split_analysis.loc[:, 'split_ratio'] = split_analysis['28.7392.2'] / split_analysis['0.0992']

# Filter significant splits (where the split ratio is not 1)
significant_splits = split_analysis[split_analysis['split_ratio'] != 1.0].copy()  # Using .copy() to avoid SettingWithCopyWarning

# Extract the year from the date column
significant_splits.loc[:, 'year'] = significant_splits['date'].dt.year

# Group by year and count the number of splits
splits_per_year = significant_splits.groupby('year').size()

# Plot the result
splits_per_year.plot(kind='bar', figsize=(12, 6), color='orange', title='Significant Stock Splits by Year')
plt.xlabel('Year')
plt.ylabel('Count of Significant Splits')
plt.show()


# In[ ]:




