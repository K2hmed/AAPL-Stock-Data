#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
import sys
import csv

def main():
    try:
        for line in sys.stdin:
            try:
                # Parse CSV data
                data = list(csv.reader([line]))[0]
                date = data[0]  # Assuming date is at index 0
                raw_close = float(data[4])  # Assuming raw_close is at index 6
                adjusted_close = float(data[6])  # Assuming adjusted_close is at index 5

                # Calculate the ratio
                if adjusted_close != 0:
                    ratio = raw_close / adjusted_close
                else:
                    ratio = 0  # Avoid division by zero

                # Output the date and ratio
                print("{}\t{}".format(date, ratio))
            except (IndexError, ValueError) as e:
                sys.stderr.write("Mapper Error: {}\n".format(e))
                continue  # Skip problematic lines
    except Exception as e:
        sys.stderr.write("Mapper Fatal Error: {}\n".format(e))

if __name__ == "__main__":
    main()

