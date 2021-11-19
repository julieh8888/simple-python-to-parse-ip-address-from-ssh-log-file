#!/usr/bin/env python3
import re
import sys

file_name = sys.argv[1]
with open(file_name, 'r') as open_file:
  read_open_file = open_file.readlines()

ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ip_list=[]
total_count = 0
total_ip_list=[]
i=0
percent=[]
num_unique_ip=0
unique_ip_list = []


for line in read_open_file:  
  ip_list = ip_pattern.search(line)
  if ip_list:
    total_ip_list.append(ip_list.group(1))    
    total_count = total_count + 1

for ip in total_ip_list:
  if ip not in unique_ip_list:
    unique_ip_list.append(ip)
    num_unique_ip = num_unique_ip + 1

print("-------------------------------------")
print("| Percent | Count |        IP        |")
print("-------------------------------------")

for i in range (0, num_unique_ip):

  percent = total_ip_list.count(unique_ip_list[i]) / total_count
  print("| " + "{:.4f}".format(percent*100) + "  |  " + str(total_ip_list.count(unique_ip_list[i])) + "  |   " + str(unique_ip_list[i]) + " |")

print("| Total   | " + str(total_count) + " |")




    

  