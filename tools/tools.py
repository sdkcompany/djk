# -*- coding: utf-8 -*-

# Tools for different processing

from termcolor import colored
from rich.align import Align
from rich import print
from rich.console import Console
from datetime import datetime
import requests as r, os, time, random, shutil, zipfile, webbrowser, traceback
from sys import platform
from progress.bar import ChargingBar
from djkcolors import djkc

start_symbol = f"{djkc.WARNING}»{djkc.ENDC}"
prompt_text = f'{djkc.WARNING}↪{djkc.ENDC} Select the option'
final_prompt = f"{prompt_text} {djkc.FAIL}❯{djkc.ENDC} "
send_symbol = f"{djkc.FAIL}❯{djkc.ENDC}"

def clear():
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nИзвините наша программа не поддерживает вашу операционную систему ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def RCT(text):
	last_color = None
	colors = ["green", "yellow", "red", "magenta", "blue"]
	new_text = ""
	for i in str(text):
		new_color = random.choice(colors)
		while new_color == last_color:
			new_color = random.choice(colors)
		new_text += colored(i, new_color)
	return new_text

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("были сохранены в папку Download на вашем устройстве", "green"))
			print(colored("Пожалуйста отправьте поочередно эти 2 файла в наш чат телеграм", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
		elif platform == "win32" or platform == "darwin":
			print("")
			print(colored("Пожалуйста отправьте в наш чат телеграм", "green"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"), colored("поочередно файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("из папки", "green"), colored("tools", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
	except:
		print("")
		print(colored("Мы не смогли переместить файлы в нужную директорию", "yellow"))
		print(colored("Возможно у вас для Термукса в настройках разрешения приложению не доступны Файлы и медиаконтент", "yellow"))
		print(colored("Пожалуйста разрешите Термуксу в настройках все нужные разрешения и повторите попытку"))
		print(colored("За помощью по данному вопросу пишите в наш чат телеграм"), colored("https://t.me/+xWLy0dl5IsQ5YzYy", "cyan"))
		print("")
		print("\nНажмите Enter чтобы вернуться назад")
		input()

def clear_logs():
	with open("tools/logs.txt", "w"):
		pass
	with open("tools/error_logs.txt", "w"):
		pass
	print("")
	print(colored("Логи успешно были очищены", "green"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()
	
def app():
	if platform in ["darwin", "win32"]:
		print(colored("Открываю ссылку!", "green"))
		webbrowser.open("https://t.me/orion_cloud_bot", new=0, autoraise=True)
		print("\nНажмите Enter чтобы вернуть назад")
		input()
	else:
		print()
		print(colored(" Попробуй данный Sms Bomber в новом", "yellow"), colored("Android", "green"), colored("приложении", "yellow"), colored("ORION app", "green"))
		print(colored("\n                 ---> ", "magenta"), colored("@orion_cloud_bot", "cyan"), colored(" <---", "magenta"))
		print("\n\nНажмите Enter чтобы вернуть назад")
		input()

def check_root():
	clear()
	print(f"[red]» Warning![/]")
	time.sleep(1.5)
	clear()
	print(f"[red]» This feature is only available to developers![/]")
	time.sleep(1)
	print()
	print(f"[red]![/] To continue, enter the password code if you are aware of what you are doing.")
	time.sleep(1)
	while True:
		print("\n")
		print(f"[red](0) Exit[/]")
		print()
		try:
			password = input(f'{djkc.OKBLUE}[{djkc.ENDC} ! {djkc.OKBLUE}»{djkc.ENDC} DJK {djkc.FAIL}(Root){djkc.ENDC} {djkc.OKBLUE}]{djkc.ENDC} {send_symbol} ')
		except KeyboardInterrupt:
			return "return"
		if password == "84616457652412":
			return True
		elif password == "0":
			return "return"
		else:
			print(f"[red]❯[/] The password is not correct.")
			time.sleep(1)

def root_update():
	result_m = check_root()
	if result_m == "return":
		return
	elif result_m == True:
		result = r.get("https://pastebin.com/raw/6z4cjxZz")
		last_ver = result.content.decode("utf-8")

		update_list = r.get("https://pastebin.com/raw/WYUYX24Y")
		update_list = update_list.content.decode("utf-8").split("\n")

		clear()
		print("[grey46]»[/] New script update found: " + last_ver)
		print("")
		k = 0
		print("[green]❯[/] List of changes.")
		for par in update_list:
			if len(update_list)-1 == k:
				print(Align("   [grey46]↪[/] " + par))
			else:
				print(Align("   [grey46]↪[/] " + par))
				k+=1
		print("")
		print("[green]❯[/] Do you want to upgrade DJK to the [green]latest[/] version?")
		print("")
		print("[green](1)[/] Yes")
		print("[red](2)[/] No")
		print("")
		while True:
			how = input(f'{djkc.OKBLUE}[{djkc.ENDC} ↻ {djkc.OKBLUE}»{djkc.ENDC} DJK (Update) {djkc.OKBLUE}]{djkc.ENDC} {send_symbol} ')
			if how == "1":
				clear()
				if platform == "linux" or platform == "linux2":
					print(colored("Устанавливаю архив...", "green"))
					os.chdir("/data/data/com.termux/files/home")
					os.system("rm -rf DJK.zip")
					
					result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
					
					a = open("ORION-Bomber.zip", "wb")
					a.write(result.content)
					a.close()
					
					print(colored("Распаковка архива...", "green"))

					fantasy_zip = zipfile.ZipFile("ORION-Bomber.zip")
					fantasy_zip.extractall("ORION-Bomber")
					fantasy_zip.close()
					os.system("rm -rf ORION-Bomber.zip")

					os.chdir("ORION-Bomber")
					os.chdir("ORION-Bomber-master")
					 
					get_files = os.listdir(os.getcwd())
					 
					for g in get_files:
						shutil.move(g, "/data/data/com.termux/files/home/ORION-Bomber")
					os.chdir("/data/data/com.termux/files/home/ORION-Bomber")
					os.system("rm -rf ORION-Bomber-master")

					print(colored("Обновление прошло успешно, запускаю ORION-Bomber...", "green"))
					time.sleep(1.5)

					os.system("pip install -r requirements.txt")
					os.system("python main.py")
					exit()
				elif platform == "win32":
					clear()
					os.startfile(os.getcwd()+"/updaters/windows.exe")
					exit()
				else:
					print(colored("[!]", "red"), colored("Наша программа пока не может установить обновление на вашу операционную ситему, вам придется скачать обновление вручную. В будущем мы постораемся сделать автообновление под вашу ОС!", "magenta"))
					print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы я открыл ссылку на репозиторий с актуальной версией")
					if input() == "1":
						result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
						if not(result_open):
							clear()
							print(colored("Мне не удалось открыть ссылку на актуальную версию на вашем устройстве ;(", "red"))
							print("\n"+"Попробуйте открыть ее сами! "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
							print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы выйти")
							if input() == "1":
								exit()
							else:
								return
						else:
							clear()
							print(colored("Скачивайте обновление!", "green"))
							exit()
					else:
						return
			elif how == "2":
				clear()
				break



def CFU():
	in_d = False
	try:
		r.get("https://google.com", timeout=5)
		in_d = True
	except:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету или интернет слишком слабый!", "magenta"))
		exit()
	clear()
	if in_d:
		print(f"[red]»[/] Checking for updates.")
		time.sleep(0.5)
		# ├ └

		result = r.get("https://pastebin.com/raw/6z4cjxZz")
		last_ver = result.content.decode("utf-8")

		update_list = r.get("https://pastebin.com/raw/WYUYX24Y")
		update_list = update_list.content.decode("utf-8").split("\n")

		a = open("tools/version.txt", "r")
		current_ver = a.read()
		a.close()
		if last_ver != current_ver:
			clear()
			print("[grey46]»[/] New script update found: " + last_ver)
			print("")
			k = 0
			print("[green]❯[/] List of changes.")
			for par in update_list:
				if len(update_list)-1 == k:
					print(Align("   [grey46]↪[/] " + par))
				else:
					print(Align("   [grey46]↪[/] " + par))
				k+=1
			print("")
			print("[green]❯[/] Do you want to upgrade DJK to the [green]latest[/] version?")
			print("")
			print("[green](1)[/] Yes")
			print("[red](2)[/] No")
			print("")
			while True:
				how = input(f'{djkc.OKBLUE}[{djkc.ENDC} ↻ {djkc.OKBLUE}»{djkc.ENDC} DJK (Update) {djkc.OKBLUE}]{djkc.ENDC} {send_symbol} ')
				
				if how == "1":
					clear()
					if platform == "linux" or platform == "linux2":
						print(colored("Устанавливаю архив...", "green"))
						os.chdir("/data/data/com.termux/files/home")
						os.system("rm -rf ORION-Bomber")
						
						result = r.get("https://github.com/Lucky1376/ORION-Bomber/archive/refs/heads/master.zip")
						
						a = open("ORION-Bomber.zip", "wb")
						a.write(result.content)
						a.close()
						
						print(colored("Распаковка архива...", "green"))

						fantasy_zip = zipfile.ZipFile("ORION-Bomber.zip")
						fantasy_zip.extractall("ORION-Bomber")
						fantasy_zip.close()
						os.system("rm -rf ORION-Bomber.zip")

						os.chdir("ORION-Bomber")
						os.chdir("ORION-Bomber-master")
						 
						get_files = os.listdir(os.getcwd())
						 
						for g in get_files:
							shutil.move(g, "/data/data/com.termux/files/home/ORION-Bomber")
						os.chdir("/data/data/com.termux/files/home/ORION-Bomber")
						os.system("rm -rf ORION-Bomber-master")

						print(colored("Обновление прошло успешно, запускаю ORION-Bomber...", "green"))
						time.sleep(1.5)

						os.system("pip install -r requirements.txt")
						os.system("python main.py")
						exit()
					elif platform == "win32":
						clear()
						os.startfile(os.getcwd()+"/updaters/windows.exe")
						exit()
					else:
						print(colored("[!]", "red"), colored("Наша программа пока не может установить обновление на вашу операционную ситему, вам придется скачать обновление вручную. В будущем мы постораемся сделать автообновление под вашу ОС!", "magenta"))
						print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы я открыл ссылку на репозиторий с актуальной версией")
						if input() == "1":
							result_open = webbrowser.open("https://github.com/Lucky1376/ORION-Bomber", new=0, autoraise=True)
							if not(result_open):
								clear()
								print(colored("Мне не удалось открыть ссылку на актуальную версию на вашем устройстве ;(", "red"))
								print("\n"+"Попробуйте открыть ее сами! "+colored("https://github.com/Lucky1376/ORION-Bomber", "green"))
								print("\nНажмите Enter чтобы запустить программу на старой версии или введите 1 чтобы выйти")
								if input() == "1":
									exit()
								else:
									return
							else:
								clear()
								print(colored("Скачивайте обновление!", "green"))
								exit()
						else:
							return
				elif how == "2":
					clear()
					break
		else:
			clear()

class Logs:
	def __init__(self):
		pass

	def save_logs(self, service, status_code, error="There is not"):
		date = datetime.now()
		if status_code in [666, False]:
			status_code = "Unknown"
		with open("tools/logs.txt", "a", encoding="utf-8") as f:
			f.write(f"DATE - {date}\nService - {service}\nStatus_code - {status_code}\nERROR:\n{error}\n\n\n")

	def error_logs(self, error):
		date = datetime.now()
		with open("tools/error_logs.txt", "a", encoding="utf-8") as f:
			f.write(f"DATE - {date}\nERROR:\n{error}\n")

def check_files_fn(dir_, files):
	if dir_ != "":
		last_dir = os.getcwd()
		os.chdir(dir_)
	list_ = os.listdir()
	for f in files:
		if f not in list_:
			return False
	if dir_ != "":
		os.chdir(last_dir)
	return True

def check_files():
	anim_text("Проверка файлов...", speed=0.02, color="green")
	files = os.listdir()
	list_ = ["main.py", "LICENSE", "README.md", "tools"]
	list_2 = ["proxy.py", "sender.py", "services.json", "tools.py", "version.txt", "logs.txt", "error_logs.txt"]
	list_3 = ["windows.exe"]

	def ward():
		clear()
		print(colored("Наша программа не нашла некоторые наши файлы", "red"))
		print(colored("Пожалуйста установите программу заново предварительно удалив папку с этой!\n", "green"))
		exit()

	if not(check_files_fn("", list_)):
		ward()
	elif not(check_files_fn("tools", list_2)):
		ward()
	elif not(check_files_fn("updaters", list_3)):
		ward()