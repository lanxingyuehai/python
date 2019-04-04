#！ /usr/bin/python3
"""
Usage:
  data_process.py [-i IN_FILE]

Options:
  -i       input file to process
"""
import os
import linecache
import argparse
import docopt from docopt

def get_content(path):
  if os.path.exists(path):
    content = ""
    cache_data = linecache.getlines(path)
    for data in cache_data[:]:
      if "=" in data or "#" in data:
        cache_data.remove(data)
    for line in range(len(cache_data)):
      if len(cache_data[line])>16:
        data = cache_data[line].strip("\n")
        content += "offset："+hex(line*32).rjust(3,"0")
      else :
        if content += "offset："+hex(line*4).rjust(3,"0")
    return content
  else :
    print("file is not exist")
    
def main():
   args = docopt(__doc__,version="1.0.0rc2")
   filename = args["IN_FILE"] 
  
   if "/" in filename:
     filename = filename.split("/")[-1]
     
   newFile = open(filename+".new","w")
   content = get_content(filename)
   newFile.write(content)
   
 if __name__ =="__main__":
    main()
  
