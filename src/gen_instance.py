import pandas as pd
import random

random.seed(42)
SIZE = 1000000
size_name = 'large'

# Generate revenue instance
data = pd.DataFrame({'revenue': [random.uniform(0, 1) for _ in range(SIZE)]})
# Sort the data in descending order
sorted_data = data.sort_values('revenue', ascending=False)
# Add the 0 at the first position
sorted_data = pd.concat([pd.DataFrame({'revenue': [0]}), sorted_data], ignore_index=True)
sorted_data.to_csv('data/'+size_name+'-r.csv', index=False, header=False)

# Generate mu instance
data = pd.DataFrame({'mu': [random.uniform(0, 1) for _ in range(SIZE)]})
# Sort the data in descending order
sorted_data = data.sort_values('mu', ascending=False)
# Add the 0 at the first position
sorted_data = pd.concat([pd.DataFrame({'mu': [0]}), sorted_data], ignore_index=True)
sorted_data.to_csv('data/'+size_name+'-mu.csv', index=False, header=False)
