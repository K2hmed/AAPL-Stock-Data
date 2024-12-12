#!/usr/bin/env python
# coding: utf-8

# In[12]:


#!/usr/bin/env python

import sys
import csv
from datetime import datetime

try:
    for line in sys.stdin:
        try:
            data = list(csv.reader([line]))[0]
            if len(data) >= 9:  # Ensure there are enough columns
                date_str = data[0]  # Assuming date is the first column
                close_price = data[4]  # Assuming close is the fifth column
                
                # Parse date and extract year
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    year = date_obj.year
                except ValueError:
                    continue  # Skip rows with invalid date format
                
                # Parse close price
                try:
                    close_price = float(close_price)
                except ValueError:
                    continue  # Skip rows with invalid price

                print("{0}\t{1}".format(year, close_price))
        except Exception as e:
            # Catch unexpected errors in processing individual lines
            sys.stderr.write("Error processing line: {0}\n".format(str(e)))
except Exception as e:
    # Catch unexpected errors in the whole process
    sys.stderr.write("Mapper error: {0}\n".format(str(e)))

