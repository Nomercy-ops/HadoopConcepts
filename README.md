# HadoopConcepts
<<<<<<< HEAD
# Cli Commands
# 1. Version: 
Hadoop HDFS version Command  displays :
Command:  hadoop version

# 2. ls
HDFS Command to display the list of Files and Directories in HDFS.
Command:hdfs dfs -ls /

# 3. mkdir
HDFS Command to create the directory in HDFS.
Usage: hdfs dfs –mkdir /directory_name
Command: hdfs dfs –mkdir /newEdureka

# 4. put
HDFS Command to copy single source or multiple sources from local file system to the destination file system.
Usage: hdfs dfs -put <localsrc> <destination>
Command: hdfs dfs –put  ~/test/sample1.txt  /Demo
  
# 5. get
HDFS Command to copy files from hdfs to the local file system.
Usage: hdfs dfs -get <src> <localdst>
Command: hdfs dfs –get /Demo/sample1.txt  ~/mylocalfiles
It will copy files from hdfs to local file system folder mylocalfiles.
 
# 6. copyFromLocal
HDFS Command to copy the file from a Local file system to HDFS.
Usage: hdfs dfs -copyFromLocal <localsrc> <hdfs destination> 
Command: hdfs dfs –copyFromLocal  ~/test/sample2.text /Demo

# 7. copyToLocal
HDFS Command to copy the file from HDFS to Local File System.
Usage: hdfs dfs -copyToLocal <hdfs source> <localdst>
Command: hdfs dfs –copyToLocal  /Demo/sample2.txt  ~/mylocalfiles

 
# 8. cat
HDFS Command that reads a file on HDFS and prints the content of that file to the standard output.
Usage: hdfs dfs –cat /path/to/file_in_hdfs
Command: hdfs dfs –cat /dataflair/sample3.txt

# 9. mv
HDFS Command to move files from source to destination. This command allows multiple sources as well, in which case the destination needs to be a directory.
Usage:  hdfs dfs -mv <src> <dest>
Command:  hdfs dfs -mv /Demo/sample1.txt  /newEdureka

# 10. cp
HDFS Command to copy files from source to destination. This command allows multiple sources as well, in which case the destination must be a directory.
Usage: hdfs dfs -cp <src> <dest>
Command: hdfs dfs -cp /Demo/sample2.txt  /newEdureka
=======
# WORD COUNT PROGRAM EXECUTION
* Step1: Create input.txt file by writing command in terminal:
* $ cd mapreduce/ #getting inside mapreduce folder.
* $ touch input.txt   # creating input.txt file
* $ nano input.txt   # editing the file and adding data.        
* $ cat input.txt  #viewing that file.
* After that create mapper.py and reduce.py file from same process and write the code.
* Step2: Start the hadoop script --> $ start-all.sh
* Step3: now create a folder on hdfs --> $ hdfs dfs -mkdir /Demo
* Step4: now copy that input.txt file inside hdfs demo folder:
* --> $ hdfs dfs -put ~/mapreduce/input.txt /Demo
#  Step5: Now we have to execute mapreduce program:
* $ hadoop jar /home/rikesh/hadoop-3.3.1/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar
* -file /home/rikesh/Hadoop_ref/word_count_python/mapper.py -mapper 'python3 mapper.py'
* -file /home/rikesh/Hadoop_ref/word_count_python/reducer.py -reducer 'python3 reducer.py' 
* -input /Demo/input.txt 
* -output /Demo/output

>>>>>>> MapReduce
