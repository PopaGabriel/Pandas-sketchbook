import pandas as pd

pd.set_option('max_columns', None)

data = pd.read_csv("aug_test.csv")
# column names
# enrollee_id  city  city_development_index  gender
# relevent_experience enrolled_university education_level
# major_discipline experience company_size company_type last_new_job training_hours

# how to show all the data
# print(data.head(10))

# how to show only one collumn
# print(data.city)
# print(data['city'])

# how to get only one value from a given index
# print(data.city[1])

# how to select one row by index
# print(data.iloc[0])


# show columns and rows using the first paradigm
# index based loc

# first number is the row, the second is the column
# all rows second column
# print(data.iloc[:, 2])

# second row all columns
# print(data.iloc[2,:])

# show the first 3 rows and all columns
# print(data.iloc[:3,:])

# show between two numbers rows and all columns
# shows all rows between 1 and 3 -> 1, 2 instead of 0, 1, 2
# print(data.iloc[1:3, :])

# shows specific rows and all columns using a list
# print(data.iloc[[0, 4, 5], :])

# shows the last rows
# print(data.iloc[-4:, 0])

# the second paradigm is label-based(loc)

# show the first value in data from the column named city
# print(data.loc[0, 'city'])

# show the specified column
# print(data.loc[[1, 2, 3], ['city', 'training_hours', 'enrollee_id']])

# show all the columns of the data frame in lexicographic order of the indexes
# shows all indexes that are between city and training in lexicographic order
# print(data.loc[:3, 'city':'training_hours'])

# it replaces the index of the DataFrame with the specified one
# print(data.set_index('enrollee_id'))

# it can replace with multiple indexes
# print(data.set_index('enrollee_id', 'city'))


# Conditionals

# returns a Series of true and false depending on the result of the operation
# print(data['city'] == 'city100')

# this Series can be used with loc to access the relevant data
# print(data.loc[data.city_development_index >= 0.9])

# we can combine the requirements to be inclusive of both '&' or to only require one at least '|'
# print(data.loc[(data.city_development_index >= 0.9) & (data.gender == 'Male')])

# SPECIAL conditionals "isin", it returns true if the value is in the list given
# print(data.loc[data.education_level.isin(['Graduate', 'Masters'])])

# SPECIAL conditional 'isnull' and 'notnull' pretty self explanatory


# he other way around  we can easily write values into the DataFrame

# data['city'] = 'Urziceni'
# print(data.city)

# we can also add values in a range to a specified dataFrame column
# data['city'] = range(len(data), 0, -1)
# print(data['city'])

# FUNCTIONS

# DESCRIBE
# This method generates a high-level summary of the attributes of the given column.
# It is type-aware, meaning that its output changes based on the data type of the input.
# print(data.describe())
# print(data.city.describe())

# functions for mathematical values 'mean' = 'average', median
# print(data.city_development_index.mean())
# print(data.city_development_index.median())

# if we want to see all the unique appearances of a value in a column we use unique()
# print(data.education_level.unique())

# if we also want to count how many times the unique value appears we use value_count
# print(data.education_level.value_counts())

# MAP
# This a simple function that applies a function to all the columns of a DataFrame
# mean_value_of_development = data.city_development_index.mean()


# print(mean_value_of_development)
# print(data.city_development_index.map(lambda p: p - mean_value_of_development))

# apply is the equivalent method if we want to apply it on the whole row

# example of function
# def function_example(row):
#  row.city_development_index = row.city_development_index - mean_value_of_development
# return row


# print(data.apply(function_example, axis='columns'))
# print(data.city_development_index)

# There are more, faster and more impressing methods to do some of these operations
# This does the same as the earlier example but in a faster time with easier complexity
# print(data.city_development_index - data.city_development_index.mean())

# we can also create series very easily using addition
# series_of_city_dev = data.city_development_index.map(lambda p: str(p))
# print(data.city + " - " + series_of_city_dev)


# a function to return the max from a series 'idxmax()'
# this prints the max id of the most developed city
# print(data.city_development_index.idxmax())

# a function that sums all the values from a series
# print(data.city_development_index.sum())

# GROUPBY
# this creates groups by the unique values in the collumn and than counts how many time they appear
# print(data.groupby("education_level").count())

# this is incredibly powerful as i can for example choose the highest marked graduate for example
# or the one that trained the most

# print(data.groupby('education_level').training_hours.max())

# Because they are just groups we can also apply() a function for each of them
# for example show the first person from each grouping

# print(data.groupby('education_level').apply(lambda graduate: graduate.iloc[0]))

# groupby can use more than a value to group for example we can use a list to group by print(data.groupby([
# 'city_development_index', 'gender']).apply(lambda df: df.training_hours.loc[df.training_hours.idxmax()]))

# Another great function is agg() can help u run multiple commands at once for example
# print(data.groupby('education_level').agg([len, min, max]))

# we can reset the multi indexes using the command reset indexes
# data = data.groupby(['education_level', 'city_development_index']).agg([len])
# print(data.head())

# We can sort by a columns values using the sort_values function
# this sorts by default in ascending order
# print(data.sort_values(by='city_development_index'))

# to change the order of the sort we just have to add another argument
# print(data.sort_values(by='city_development_index', ascending=False))

# MISSING DATA IMPORTANT!
# we have to first find those that are null, we can use the method explained earlier
# or we can simplify the formula


# first the pd.isnull(data.collumn) return a series of trues and falses
# and the data.loc creates a new DataFrame with the rows that have the null values
# for their education level

# print(data.loc[pd.isnull(data.education_level)])
# print(data.loc[data.education_level.isnull()])

# because we can always hit some nan values we should try to mitigate that problem
# pandas comes with a great function called fillna(argument) and it will replace the
# nan value with the arguments value

# data.education_level = data.education_level.fillna("Unknown")
# print(data.loc[data.education_level.isnull()])

# if for example there has been a change in the dataset
# for example one of the people changed their idee
# we can use the replace() method to replace the old name with the new one

# print(data.head(5))
# data.enrollee_id = data.enrollee_id.replace(32403, "Cine tentreba")
# print(data.head(5))

# Important!
# if we want to get the type of a column in a data frame we use data.column.dtype
# and if we want to change it we use data.comlumn.astype('other_type')

# print(data.enrollee_id.dtype)
# data.enrollee_id = data.enrollee_id.astype('str')
# print(data.enrollee_id.dtype)

# replace the values nan with "Unknown", count them and sort descending
# data.education_level = data.education_level.fillna("Unknown")
# rd = data.groupby('education_level').education_level.agg([len]).sort_values(by='len', ascending=False)
# print(rd)
# print(rd.sort_values(by='len', ascending=False))

# data csv comes with names that are not truly ok which means it would be faster and easier for us
# if we could change them, and we can of course the method rename helps us

# print(data.rename(columns={'education_level': 'education'}))

# we can also rename indexes there are multiple formats but the best one is the dictionary type
# print(data.rename(index={0:'first_entry', 1:'second_entry'}))

# we can rename the axises themselves for example rename the fields row from nothing to fields
# print(data.rename_axis('fields', axis='columns').rename_axis('people', axis='rows'))

# Combining

# we can concat two csv's with concat() join() or merge()
# concat merges them vertically


# data2 = pd.read_csv('aug_train.csv')
# print(pd.concat([data, data2]))

# we can also join them by a common index
# join merges them horizontally
# data.set_index(['enrollee_id', 'city_development_index'])
# data2.set_index(['enrollee_id', 'city_development_index'])
# print(data.join(data2, lsuffix='_train', rsuffix='_test'))



