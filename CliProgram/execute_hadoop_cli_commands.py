"""
@Author: Rikesh Chhetri
@Date: 2021-07-28 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-28 10:03:30
@Title : Program Aim perform HADOOP HDFS CLI Commands
"""

import subprocess

def run_cmd(args_list):
        """
    Description:
        This method is used for running hdfs commands using python program
    Parameter:
        It takes args_list as a parameter.
       
    """
        print('Running system command: {}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output = proc.communicate()
        return s_output

if __name__=="__main__":
        
        cmd = run_cmd(["hdfs",'dfs','-mkdir','/test'])
        cmd = run_cmd([ 'hdfs', 'dfs', '–put','~/mylocalfiles/sample1.txt', '/test'])
        cmd = run_cmd(["hdfs",'dfs','-ls','/'])
        cmd = run_cmd(['hadoop','version'])
        cmd = run_cmd(["hdfs",'dfs','-cp','/Demo/input.txt','/test'])
        cmd = run_cmd(["hdfs",'dfs','-rm','-r','/test'])
        print(cmd)
       
       
       
       # “sudo chmod a+rwx /path/to/file”         

