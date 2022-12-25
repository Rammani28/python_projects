# # with open('weather-data.csv') as weather_data:
# #     data_list = weather_data.readlines()
# # print(data_list)
#
# # import csv
# #
# # with open('weather-data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temp = row[1]
# #             temperature.append(int(temp))
# # print(temperature)
#
# import pandas
#
# data = pandas.read_csv('weather-data.csv')
#
# # temp_list = data['temp'].to_list()
# # average = sum(temp_list) / len(temp_list)
# # mean = temp_list.mean()
# # print(average)
#
# # temp_column = data.temp
# # max_temp = temp_column.max()
# # print(max_temp)
#
# monday_temp = data[data.day == 'Monday'].temp
# print(monday_temp)
# fahrenheit = monday_temp * 1.8 + 32
# print(fahrenheit)

import pandas

data = pandas.read_csv('the_squirrel_census.csv')
fur_color_series = data['Primary Fur Color']
color_count_dict = fur_color_series.value_counts().to_dict()
print(color_count_dict)
data2 = pandas.DataFrame(color_count_dict, index=[0])
data2.to_csv('squirrel_count.csv')
