import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('max_columns', None)

datar = pd.read_csv("aug_test.csv")

data_show = datar.set_index("city_development_index")

# set the size of the plot
plt.figure(figsize=(16, 6))


# simple plot that shows one value dependant on the index
sns.lineplot(data=data_show['training_hours'])



