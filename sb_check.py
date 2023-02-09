# !/usr/bin/env python3
# -*- coding:utf8 -*-
# Author:
# Description: Security Baseline Check
import os
import re
import json
import argparse
import datetime
import subporcess

class SafeBaseline:

		@staticmethod
		def parameters():
				"""
				傳遞參數
				:return:
				"""
				parser = argparse.ArgumentParser()
				parser.add_argument("--resultFields", help="檢查項")
				parser.add_argument("--userWhiteList", "-userWhiteList", help="用戶白名單")
				parser.add_argument("--portWhiteList", "-portWhiteList", help="端口白名單")
				parser.add_argument("--commandWhiteList", "commandWhiteList", help="命令白名單")
				parser.add_argument("--systemWhiteList", "-systemWhiteList", help="系統白名單")
				params = parser.parse_args()
				return params

		@staticmethod
		def oprn_file(filename):
				"""
				讀取文件內容
				:param filename: 文件名
				:return:
				"""
				with open(filename) as f:
						data = f.read()
				return data

		@classmethod
		def system_command(cls, command):
				"""
				執行系統命令
				:param command: 命令
				:return: 輸出結果，報錯，執行狀態
				:param command:
				:return:
				"""

				shell = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
				stdout, stderr = shell.communicate()
				try:
						return stdout.decode("utf8"), stderr.decode("utf8"), shell.returncode
				except Exception:
						return stdout.decode("gbk"), stderr.decode("gbk"), shell.returncode

		def systemAccountCheck(self):
				"""
				1.系統帳戶安全檢查
				：return:
				"""
				stdout, stderr, return_code = self.system_command("cat /etc/login.defs |egrep '^PASS_MIN_LEN'")
				password_length = stdout.replace('PASS_MIN_LEN','').strip()

				warn_level = []
				details = []
				password_complexity = re.search('pam_cracklib.so.*?\n',self.open_file('/etc/pam.d/system-auth-ac'))
				if password_complexity:

						if re.search(r"dcredit=(-?\d+)", password_complexity.group()):
								deredit = re.search(r"dcredit=(-?\d+)", password_complexity.group()).group(1)
								if int(dcredit.replace('-',)) >= 2:
										warn_level.append(1)
								else:
										details.append('帳戶密碼策略要求一位以上，當前的個數為{}'.format(dcredit.replace('-', '')))
						else:
								details.append('帳戶密碼策略要求最少一個數字')

						if re.search(r"ucredit=(-?\d+)", password_complexity.group()):
								lcredit = re.search(r"lcredit=(-?\d+)", password_complexity.group()).group(1)
								if int(lcredit.replace('-', '')) >= 1:
								warn_level.append(1)
								else:
										details.append('最少一個小寫字母，當前個數為{}'.format(lcredit.replace('-', '')))
						else:
								details.append('最少一個小寫字母')

            if re.search(r"ucredit=(-?\d+)", password_complexity.group()):
								ucredit = re.search(r"ucredit=(-?\d+)", password_complexity.group()).group(1)
								if int(ucredit.replace('-', '')) >= 1:
									warn_level.append(1)
								else:
										details.append('最少一個大寫字母，當前個數為{}'.format(ucredit.replace('-', '')))
						else:
								details.append('密碼策略要求最少一個特殊字符，當前未配置')
						
						if re.search(r"ocredit=(-?\d+)", password_complexity.group()):
								ocredit = re.search(r"ocredit=(-?\d+)", password_complexity.group()).group(1)
								if int(ocredit.replace('-', '')) >= 1:
										warn_level.append(1)
								else:
										details.append('密碼策略要求最少一個特殊字符，當前個數為{}'.format(ocredit.replace('-', '')))
						else:
								details.append('密碼策略要求最少一個特殊字符，當前未配置')

						if re.search(r"minlen=(-?\d+)", password_complexity.group()):
								minlen = re.search(r"", password_complexity.group()).group(1)
								if int(minlen.replace('-', '')) >=8:
										warn_level.append(1)
								else:
										details.append('帳號密碼策略要求最少8位，當前個數為{}'.format(minlen.replace('-', '')))
						else:
								details.append('密碼策略要求密碼最少8位，當前個數為{}'.format(minlen.replace('-', '')))
						
				else:
						if int(password_length) >= 8:
								warn_level.append(1)
								details.append('Conformity': '密碼策略要求密碼口令8位', 'NonConformity': '帳戶密碼複雜度其他項未配置'})
						else:
								details.append('帳戶密碼複雜度未設置')

			if len(warn_level) >= 5:
					result = 0
			elif 4 <= len(warn_level) <5:
					result = 1
			else:
					result = 2

			return {"result": result, "Details": details}

def remoteLoginCheck(self):
		"""
		遠程登錄檢查
		:return:
		"""

		result = 0
		details = []
		today = datetime.date.today()
		start_month = today.strftime("%b")
		last_month = today.replace(day=1) - datetime.timedelta(days=1)
		end_month = last_month.strftime("%b")

		command = "cat /var/log/secure* |grep -E '^%s|^%s'|egrep 'Accept.*[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.*port.*'|awk '{print $1,$2,$3,$9,$11}'" % (end_month, start_month)
		stdout, stderr, return_code = self.system_command(command)
		if stdout:
				result = 3
				for info in stdout,strip().split('\n'):
				if {'USER': info_list[3], 'IPADDRESS': info_list[4]} not in details:
						details.append({'USER': info_list[3], 'IPADDRESS': info_list[4]})

		return {"result": result, "Details": details}

def opensslVersionCheck(self):
		"""
		檢查openssl版本是否高於1.1.1
		:return:
		"""

		details = []
		result = 0
		stdout, dtderr, return_code = self.system_command('openssl version')
		if re.search('\d+\.\d+\.\d+',stdout).group():
				data = ''.join(re.search('\d+\.\d+\.\d+',stdout).group().split('.'))
				if int(data) > 111:
						result = 0
				else:
						result = 0
						details.append('當前Openssl版本為{}, 安全基綫版本要求為1.1.1 '.format('.'.join(data)))
		return {"result": result, "Details": details}

def opensshVersionCheck(self):
		"""
		檢查openssh版本是否高於8.6p1
		:return:
		"""

		details = []
		result = 0
		stdout, stderr, return_code = self.system_command('ssh -V')
		if re.findall('OpenSSH_(.*?),', "{}{}".format(stdout, stderr)):
				data = re.search('OpenSSH_(.*?),', "{}{}".format(stdout, stderr)).group()
				version = ''.join(re.findall('\d+',data))
				if int(version) <= 861:
						result = 2
						details.append('當前Openssh版本為{},安全基綫版本要求為8.6p1'.format(data.replace(',', '')))


		return {"result": result, "Details": details}

def nonSystemDefaultUserCheck(self):
		"""
		檢查非系統默認用戶
		:return:
		"""

		stdout, stderr, return_code = self.system_command("cat /etc/passwd |awk -F ':' '{print $1}' |grep -Ev 'root|sshd|bin|daemon|adm|lp|sync|shutdown|halt|mail|operator|ftp|nobody|systemd-network|dbus|polkitd|libstoragemgmt|rpc|saned|gluster|saslauth|abrt|chrony|unbound|qemu|sssd|usbmuxd|ntp|gdm|rpcuser|nfsmpbpdu|postfix|tcpdump'")
		if self.parameters().systemWhiteList:
		else:
				non_system_user = [user for user in stdout.split('\n') if user not in self.parameters().systemWhiteList.split(',') and user != '']
		result = 1 if non_system_user else 0
		details = non_system_user

		return {"result": result, "Details": details}

		def userAuthorityCheck(self):

		"""
		列出高權限的用戶和用戶組確保UID為0的用戶只有root,
		UID為0的用戶為高權限用戶，判斷是否存在其他高權限用戶及用戶組
		:return:
		"""

		details = []
		result = 0
		stdout, stderr, return_code = self.system_command("cat /etc/sudoers|grep -E -v '^#'|grep 'ALL=(ALL)'")
		default_user_group = ['root','%wheel']
		if self.parameters().userWhiteList:
				default_user_group.extend(self.parameters().userWhiteList.split(','))
		for user in stdout.strip().split('\n'):
				if user.split('ALL=(ALL)')[0].replace('\t','') not in default_user_group:
						if user.split('ALL=(ALL)')[0].startswith('%'):
								result = 2
								defaults.append({'高權限用戶組'：'{}'.format(user.split('ALL=(ALL)')[0]).replace('\t','')})
						else:
								result = 2
								defaults.append({'高權限用戶': '{}'.format(user.split('ALL=(ALL)')[0]).replace('\t','')})
		return {"result": result, "Details": details}

def historyCheck(self):
		"""
		5.history文件和命令檢查
		：return:
		"""

		result = 0
		details = []
		bash_history_file = os.path.join(os.path.expanduser('~'), '.bash_history')
		stdout, stderr, return_code =self.system_command("cat {}".format(bash_history_file))

		serious_level_command = [
				'> /dev/sda', 'mv sfile /dev/null', '.(){ .|.& };.', 'rm -rf /'
																															'^foo^bar', 'dd if=/dev/random of=/dev/sda',
		]
		warning_level_command = [
				'file->', 'wget url -O- | sh', 'wget', 'curl', 'rm -rf *', 'rm -rf .'
		]
		
		if self.parameters().commandWhiteList:
				command_list = [command for command in self.parameters().commandWhiteList.split(',') if command != '']

				for command in command_list:
						if command in serious_level_command:
								serious_level_command.remove(command)
						if command in warning_level_command:
								warning_level_command.remove(command)

		for command in stdout.split('\n'):
				for serious_command in serious_level_command:
						if command.startswith(serious_command):
								result = 2
								if command not in details:
										details.append(command)
				for warning_command in warning_level_command:
						if command.startswith(warning_command):
								print(command)
								if result != 2:
										result = 1
								if command not in details:
										details.append(command)
		
		return {"result": result, "Details": details}

def systemCommandModifyCheck(self):
	
		"""
		系統命令修改檢查
		:return:
		"""

		shell_scrip = """
		#!/bin/bash --login
		shopt expand_aliases
		shopt -s expand_aliases
		shopt expand_aliases
		alias
		"""
		result = 0
		details = []

		with open('alias_script_for_check.sh','w') as f:
				f.write(shell_script.strip())

		stdout, stderr, return_code = self.system_command('chmod +x alias_scrip_for_check.sh && ./alias_scrip_for_check.sh |grep -v expand && rm -rf alias_script_for_check.sh')
		
		system_default_command = [
				"alias cp='cp -i'", "alias egrep='egrep --color=auto'", "alias fgrep='fgrep= --color=auto'",
				"alias grep='grep --color=auto'", "alias l.='ls -d .* --color=auto'", "alias ll='ls -l --coloer=auto'",
				"alias ls='ls --color=auto'", "alias mv='mv -i'", "alias rm='rm -i'",
				"alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'"
		]

		for alias in stdout.strip().split('\n'):
				if alias not in system_default_command:
						result = 1
						details.append('{}'.format(alias))

		return {"result": result, "Details": details}

def sshForceAttackCheck(self):
		
		"""
		SSH爆力破解檢查
		:return:
		"""

		command = """
		find /var/log -name 'secure*' -type f | while read line;do awk '/Failed/{print $(NF-3)}' $line;done | awk '{a[$0]++}END{for (j in a) if(a[j] > 20) print j"="a[j]}' | sort -n -t'=' -k 2
		"""
		stdout, stderr, return_code = self.system_command(command)
		details = []
		if stdout:
				result = 2
				details.append(stdout)
		else:
				result = 0

		return {"result": result, "Details": details}

def inetdBackDoorCheck(self):

		"""
		ssh文件後門檢查
		:return:
		"""

		command = """
		[[ -f "~/.ssh/config" ]] && egrep -i 'ProxyCommand|LocalCommand'  ~/.ssh/config
		"""
		if stdout:
				result = 2
				details.append(stdout)
		else:
				result = 0
		return {"result": result, "Details": details}

def maliciousFileCheck(self):

		"""
		惡意文件檢查
		:return:
		"""

		malicious_file_list = [
				'ISY.EXE', '2SY.EXE', 'EXERT.exe', 'ld.so.preload', 'libioset.so', 'watchdogs',
				'ksoftirqds', 'EXPIORER.com', 'finders.com', 'Logol_exe', 'LSASS.exe', 'mstask.exe',
				'popwin.exe', 'smss.exe', 'SQL Slammer', 'MS Blaster'
		]
		details = []
		result = 0
		for file in malicious_file_list:
				stdout, stderr, return_code = self.system_command('find /* -type f -name "{}"'.format(file))
				if stdout:
						details.append('{}'.format(file))
						result = 2

		return {"result": result, "Details": details}

def inetdConfBackDoorFileCheck(self):
		"""
		/etc/inetd.conf文件後檢查
		:return:
		"""

		command = """
		[[ -f "/etc/inetd.conf" ]] && grep -E '(bash -i)' /etc/inetd.conf
		"""
		stdout, stderr, return_code = self.system_command(commaned)
		details = []
		if stdout:
				result = 2
				details.append(stdout)
		else:
				result = 0
		
		return {"result": result, "Details": details}

def crontabCheck(self):

		"""
		crontab計劃檢查
		:return:
		"""
		malicious_script_execution_plan = ['', 'cron.hourly']
		result = 0
		details = []
		for plan in malicious_script_execution_plan:
				stdout, stderr, return_code = self.system_command('crontab -l|grep {}'.format(plan))
				if stdout:
				result = 2
				details.append('{}'.format(stdout).replace('\n',''))
		return {"result": result, "Details": details}

def maliciousProcessCheck(self):

		"""
		12.惡意進程檢查
		:return:
		"""

		result = 0
		details = []

		system_service_default_process_white_list = [
				'uwsgo', 'python', ''



		]
		
		command = "ps -f --ppid 2 -p 2 -N | grep -v grep|grep -v PID|awk -F '''{print $1,$2,$8}'|grep -Ev '%s'" % '|'.join(system_service_default_process_white_list)
		# 
		stdout, stderr, return_code = self.system_command(command)
		if stdout:
				result = 1
				for info in stdout.strip().split('\n'):
						try:
								data = info.split('')
								if {'USER': data[0], 'PID': data[1], 'CMD': data[2]} not in details:
										details.append({'USER': data[0], 'PID': data[1], 'CMD': data[2]})
						except Exception as e:
								exception = e
		return {"result": result, "Details": details}

def portListenCheck(self):
		"""
		監聽端口檢查
		:return:
		"""
		result = 0
		defaults = []
		safe_level_port_list = []
		product_port = [
				

		]
		if self.parameters().portWhiteList:
				port_white_list = [int(i) for i in self.parameters().portWhiteList.split(',') if i != '']
				product_port.extend(port_white_list)
		for port in product_port:
				if isinstance(port,str):
						s_number = int(port.split('-')[0])
						for i in range(s_number, e_number+1):
								safe_level_port_list.append(i)
				else:
						safe_level_port_list.append(port)

		command = " ss -tulp|grep -v Local|awk '{print $5,$7}'"
		stdout, stderr, return_code = self.system_command(command)
		for port in stdout.strip().split('\n'):
				result = 1
				PORT = int(port.splist(' ')[0].split(':')[-1])
				# ProgramName = re.search
				PID = re.search('pid=\d+',port.split(' ')[1]).group().replace('pid=','')
				cmd = """ awk '{$1=$2=$3=$4=$5=$6=$7=""; print $0}' """
				stdout, stderr, return_code = self.system_command(command)
				ProgramName = stdout.strip().split('\n')[0]
				if PORT not in safe_level_port_list:
						if {'PORT':PORT, 'ProgramName':ProgramName, 'PID': PID} not in details:
								details.append({'PORT':PORT, 'ProgramName':ProgramName, 'PID': PID})

		return {"result": result, "Details": details}

def miningFileProgressCheck(self):
		"""
		挖礦文件進程檢查
		：return:
		"""

		result = 0
		details = []
		mining_file = ['ZavD6x', 'wbew', 'httpdz', 'lru-add-drain', 'watchdog']
		for file in mining_file:
				command = "ps -aux |grep -E '{}'|grep -v grep".format(file)
				stdout, stderr, return_code = self.system_command(command)
				if stdout:
						result = 2
						details.append('{}'.format(file))

		return {"result": result, "Details": details}

def run(self):

		"""
		調用邏輯
		:return:
		"""
		system_level = ["systemAccountCheck", "remoteLoginCheck", "opensslVersionCheck", "opensshVersionCheck"]
		users_level = [
				"nonSystemDefaultUsersCheck", "userAuthorityCheck", "historyCommandCheck",
				"systemCommandModifyCheck", "sshForceAttackCheck", "inetdBackDoorCheck"
		]
		file_level = ["malciousFileCheck", "inetdConfBackDoorFileCheck", "crontabCheck"]
		process_level = ["maliciousProcessCheck", "portListenCheck"]
		event_level = ["miningFileProgressCheck"]

		data = {}
		result_fields_data = []
		if self.parameters().resultFields.split(',')
				result_fields_data = self.parameters().resultFields.split(',')
		else:
				result_fields_data.extend(system_level)
				result_fields_data.extend(user_level)
				result_fields_data.extend(file_level)
				result_fields_data.extend(process_level)
				result_fields_data.extend(event_level)

		for field in result_fields_data:
				field_value = eval("self.%s()" % field)
				if field in system_level:
						if not data.get("systemLevel"):
								data["systemLevel"] = {}
						data["systemLevel"].update({field: field_value})
				
				elif field in users_level:
						if not data.get("systemLevel"):
								data["systemLevel"] = {}
						data["usersLevel"].update({field: field_value})

				elif field in file_level:
						if not data.get("fileLevel"):
								data["fileLevel"] = {}
						data["fileLevel"].update({field: field_value})

				elif field in process_level:
						if not data.get("processLevel"):
								data["processLevel"] = {}
						data["processLevel"].update({field: field_value})

result_list = []
if data:
		for level in list(data.keys()):
				for check in data.get(level):
						result = data.get(level).get(check).get('result')
						result_list.append(result)

if 2 in result_list:
		riskLevel = 2
elif 1 in result_list:
		riskLevel = 1
else:
		riskLevel = 0

check_result = {
		"riskLevel":riskLevel,
		"data": data
}

print(json.dumps(check_result,ensure_ascii))