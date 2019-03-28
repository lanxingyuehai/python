import os
import linecache
import argparse

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
   parser = argparse.ArgumentParser()
   parser.add_argument("-i",action="store",help="input file")
   parser.add_argument("-o",action="store",help="output file")
   args = parser.parse_args()
   
   inputLog = args.i
   outputLog = args.o
   filename = ""
   if "/" in inputLog:
     filename = inputLog.split("/")[-1]
   else :
     filename = inputLog
     
   newFile = open(filename,"w")
   content = get_content(filename)
   newFile.write(content)
   
 if __name__ =="__main__":
    main()
  
