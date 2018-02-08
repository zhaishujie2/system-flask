# -*- coding:utf-8 -*-
import paramiko
from config import ip_list,user,passwd
import time
def get_system_information(ip,user,passwd):
        print ip
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, 22, username=user, password=passwd, timeout=4)
	dict = {}
	#获取内存信息
	stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
	for std in stdout.readlines():
		if std.split(":")[0]=="MemTotal":
                        total_memory = int(std.split(":")[1].strip()[:-3])
		elif std.split(":")[0]=="MemFree":
                        free_memory=int(std.split(":")[1].strip()[:-3])
                elif std.split(":")[0]=="Buffers":
                        Buffers = int(std.split(":")[1].strip()[:-3])
	        elif std.split(":")[0]=="Cached":
                        Cached = int(std.split(":")[1].strip()[:-3])
        dict["total_memory"]=total_memory
        dict["free_memory"] =total_memory-free_memory-Buffers-Cached
        #获取cpu核数
	stdin, stdout, stderr = client.exec_command('cat /proc/cpuinfo')
	n=0
	for std in stdout.readlines():
		if std.split(":")[0]=="model name	":
			n+=1
	dict["cpu_code"]=n
	stdin, stdout, stderr = client.exec_command('cat /etc/sysconfig/network')
        for std in stdout.readlines():
                lis = std.split("=")
                if lis[0]=="HOSTNAME":
                        dict["hostname"]=lis[1].strip()

	#获取cpu运行状态
	stdin, stdout, stderr = client.exec_command('cat /data/system/rate.txt')
        for std in stdout.readlines():
		lis = std.split(":")
		if lis[0]=="CPU":
			dict["cpu"]=lis[1].strip()
		if lis[0]=="RAM":
			dict["ram"]=lis[1].strip()
		if lis[0]=="STATUS":
			dict["status"]=lis[1].strip()
	#获取ip
	stdin, stdout, stderr = client.exec_command("ifconfig eth0 | grep 'inet addr' | awk '{ print $2}' | awk -F: '{print $2}'")
	dict["ipaddr"]= stdout.read().strip()
	#获取线程数
	stdin, stdout, stderr = client.exec_command("ls /proc")
	n=0
	for std in stdout.readlines():
		std1 = std.strip()
		if std1.isdigit():
			n+=1
	dict["thread"]=n
	dict["time"]=int(time.time())
        dict["RAM"]=float('%.3f' %( dict["free_memory"]*1.0/dict["total_memory"]))*100
	print dict["free_memory"],dict["total_memory"]
	client.close()
	return dict
def get_all_system():
		result = []
		for ip in ip_list:
			dict = get_system_information(ip,user,passwd)
			result.append(dict)
		return result
def get_node_system(ip):
		dict = []
		dict = get_system_information(ip,user,passwd)
		return dict 


if __name__ == '__main__':
	print get_all_system()
