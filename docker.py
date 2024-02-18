import os
import re
from collections import Counter
import socket

def get_file_names(path):
    return os.listdir(path)

def get_word_count(file_path):
    with open(file_path) as f:
        data = f.read()
        words = re.findall(r'\w+', data)
        return len(words)
        
def get_top_words(file_path, num):
    with open(file_path) as f:
        data = f.read()
        words = re.findall(r'\w+', data)
        word_counts = Counter(words)
        return word_counts.most_common(num)
        
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

print("-----------------------------------------------------------------------------------")
file_names = get_file_names('/home/data')
txt_files = [f for f in file_names if f.endswith('.txt')]
print("Name of all the text file at location /home/data")
print(txt_files)
wc1 = get_word_count('/home/data/IF.txt')
wc2 = get_word_count('/home/data/Limerick-1.txt')
print("The count of total number of words in each text files is as follows")
print("Total number of words in IF.txt is ",wc1)
print("Total number of words in Limerick-1.txt is ",wc2)
total_words = wc1 + wc2
print("Grand total which is total number of words in both files is ",total_words)
top_words = get_top_words('/home/data/IF.txt', 3)
print("Top 3 words with maximum number of counts in IF.txt is as follows")
print(top_words)
print("The IP address of your machine")
ip = get_ip()
print(ip)

with open('/home/output/result.txt', 'w') as f:
    f.write("Name of all the text file at location /home/data")
    f.write('\n')
    f.write(str(txt_files))
    f.write('\n')
    f.write("The count of total number of words in each text files is as follows")
    f.write('\n')
    f.write('Total number of words in IF.txt is')
    f.write('\n')
    f.write(str(wc1))
    f.write('\n')
    f.write('Total number of words in Limerick-1.txt is ')
    f.write('\n')
    f.write(str(wc2))
    f.write('\n')
    f.write('Grand total which is total number of words in both files is ')
    f.write('\n')
    f.write(str(total_words))
    f.write('\n')
    f.write('Top 3 words with maximum number of counts in IF.txt is as follows')
    f.write('\n')
    f.write(str(top_words))
    f.write('\n')
    f.write('The IP address of your machine')
    f.write('\n')
    f.write(ip)

print("---------------------Content written sucessfully to result.txt---------------------")
print("  ")
print("------------------Reading and printing the contents of result.txt------------------")
print("-----------------------------------------------------------------------------------")
with open('/home/output/result.txt', 'r') as f:
  contents = f.read()
  print(contents)