#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python

import sys

current_year = None
total_close = 0.0
count = 0

try:
    for line in sys.stdin:
        try:
            line = line.strip()
            year, close_price = line.split("\t")
            close_price = float(close_price)

            if current_year and current_year != year:
                # Output the average for the previous year
                if count > 0:
                    avg_close = total_close / count
                    print("{0}\t{1:.2f}".format(current_year, avg_close))
                # Reset counters for the new year
                total_close = 0.0
                count = 0

            current_year = year
            total_close += close_price
            count += 1
        except ValueError:
            continue  # Skip lines with invalid data
        except Exception as e:
            sys.stderr.write("Error processing line: {0}\n".format(str(e)))

    # Output the last year's average
    if current_year and count > 0:
        avg_close = total_close / count
        print("{0}\t{1:.2f}".format(current_year, avg_close))
except Exception as e:
    sys.stderr.write("Reducer error: {0}\n".format(str(e)))

