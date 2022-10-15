import csv

file = open('data.csv', 'a')

name = input('Enter name: ')
phone = input('Enter phone number: ')
county = input('Enter county: ')
merger = input('Enter merger: ')

writer = csv.writer(file)

writer.writerow([name, phone, county, merger])

file.close()
