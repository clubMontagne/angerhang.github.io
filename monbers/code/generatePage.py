"""
The input will be the name of the person and and the
photo directory. The output will be the generately link
and the id page on github page
"""
import csv

## directories
# member page dir
member_dir = '../../members'
data_dir = '../data/test2.csv'
dest_dir = '../data/'

# import
def csv_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(" ".join(line))


with open(data_dir, newline='') as csvfile:
     spamreader = csv.DictReader(csvfile)
     for row in spamreader:
       print(row['Name'])
       # init file constants
       status = 'epfl student'
       exp_date = '2019.01.01'
       img_path = '/img/test.jpg'

       file_name = '../../members/' + row['Name'] + '.md'

       # csv_reader(data_dir)

       # writing to file
       file = open(file_name, "w+")
       file.write('---\nlayout: post\n')
       file.write('title: ' + row['Name'] + '\n---\n\nStatus: ' + status + '\n')
       file.write('Expiration date: ' + exp_date + '\n')
       file.write('![](' + img_path + ')\n')
       file.write('![](/members/img/bar.png)\n')

       file.close()
