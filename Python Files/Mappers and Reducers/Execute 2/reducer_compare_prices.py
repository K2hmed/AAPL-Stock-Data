#!/usr/bin/env python
# coding: utf-8

# In[11]:


#!/usr/bin/env python
import sys

def main():
    try:
        for line in sys.stdin:
            try:
                # Strip and output the line directly (pass-through reducer)
                print(line.strip())
            except Exception as e:
                sys.stderr.write("Reducer Error: {}\n".format(e))
    except Exception as e:
        sys.stderr.write("Reducer Fatal Error: {}\n".format(e))

if __name__ == "__main__":
    main()

