# READING FROM FILES

# print(help(open("data.csv", 'r')))

# filename = 'data.csv'
# file = open(filename, "r")

# data = file.readline()

# print(data)
# data = file.readline()

# print(data)
# data = file.readline()

# print(data)
# data = file.readline()

# print(data)


# filename = 'products.csv'
# file = open(filename, "a")

# file.write("champagne,50,5000\n")

# filename = "netflix_titles.csv"

# file = open(filename, "r", errors="ignore")

# data = file.readlines()[1:]
# # data.pop(0)

# # OPEN NEW FILE FOR WRITE

# filename = '2017_filter.csv'
# file = open(filename, "a")

# all_years = []
# durations = []


# for line in data:
    
#     try:
#         show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = line.split(",")
    
#         all_years.append(int(release_year))
#         durations.append(int(duration.split(' ')[0]))
#         # print(, int(duration.split(' ')[0]))

#         if max(durations) == int(duration.split(' ')[0]):
#             longest_movie = title
#     except:
#         pass

# years = list(set(all_years))
# years.sort()

# print(f"Dataset Duration - {years[0]}-{years[-1]}")

# print(f"Movie with longtest duration - {longest_movie} at {max(durations)} mins")

import requests

r = requests.get('https://www.jumia.com.ng/')
print((r.content))

