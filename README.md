# HadoopConcepts
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
* Step5: Now we have to execute mapreduce program:
