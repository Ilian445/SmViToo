###################################################
#                                                 #
#                    VirusTool                    #
#                                                 #
#       Автор: https://github.com/ilian445        #
#                                                 #
#                  Версия: 0.1b                   #
#                                                 #
###################################################



#Lib
import os
os.system('pip3 install colorama')
import colorama


#Logo var
logo = ' ::::::::  ::::    ::::  :::     ::: ::::::::::: :::::::::::  ::::::::   ::::::::  \n:+:    :+: +:+:+: :+:+:+ :+:     :+:     :+:         :+:     :+:    :+: :+:    :+: \n+:+        +:+ +:+:+ +:+ +:+     +:+     +:+         +:+     +:+    +:+ +:+    +:+ \n+#++:++#++ +#+  +:+  +#+ +#+     +:+     +#+         +#+     +#+    +:+ +#+    +:+ \n       +#+ +#+       +#+  +#+   +#+      +#+         +#+     +#+    +#+ +#+    +#+ \n#+#    #+# #+#       #+#   #+#+#+#       #+#         #+#     #+#    #+# #+#    #+# \n ########  ###       ###     ###     ###########     ###      ########   ######## '



#DEFs
def main():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	colorama.init()
	print(colorama.Fore.GREEN + logo)
	print("\n"+colorama.Fore.CYAN+"Author: "+colorama.Fore.YELLOW+"https://github.com/ilian445")
	print("\n"+colorama.Fore.YELLOW+"1) Create MessageBox\n0) Exit\n")

	if int(input(colorama.Fore.RED +'VirusTool> ' + colorama.Fore.WHITE)) == 1:
		messagebox()
	else:
		pass

def messagebox():
	#lib
	os.system('pip3 install tkinter')
	os.system('pip3 install pyinstaller')


	#Enter text, title
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	colorama.init()
	print(colorama.Fore.GREEN + logo)
	print("\n"+colorama.Fore.CYAN+"Author: "+colorama.Fore.YELLOW+"https://github.com/ilian445"+'\n')
	title = str(input(colorama.Fore.RED +'Enter title: ' + colorama.Fore.WHITE))
	text = str(input(colorama.Fore.RED +'Enter text: ' + colorama.Fore.WHITE))


	#Select type
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	colorama.init()
	print(colorama.Fore.GREEN + logo)
	print("\n"+colorama.Fore.CYAN+"Author: "+colorama.Fore.YELLOW+"https://github.com/ilian445"+'\n')
	print(colorama.Fore.WHITE + 'Select type: ')
	print(colorama.Fore.YELLOW + '1) Info\n2) Warning\n3) Error\n4) Question (Yes/No)\n5) Question (Retry/Cancel)\n0) Exit\n')


	#Create virus
	answ = int(input(colorama.Fore.RED +'VirusTool> ' + colorama.Fore.WHITE))
	if answ == 1:
		with open('temp.py', 'w') as f:
			f.write(f"import tkinter.messagebox\ntkinter.messagebox.showinfo(title='{title}', message='{text}')")

	elif answ == 2:
		with open('temp.py', 'w') as f:
			f.write(f"import tkinter.messagebox\ntkinter.messagebox.showwarning(title='{title}', message='{text}')")
	
	elif answ == 3:
		with open('temp.py', 'w') as f:
			f.write(f"import tkinter.messagebox\ntkinter.messagebox.showerror(title='{title}', message='{text}')")

	elif answ == 4:
		with open('temp.py', 'w') as f:
			f.write(f"import tkinter.messagebox\ntkinter.messagebox.askyesno(title='{title}', message='{text}')")

	elif answ == 5:
		with open('temp.py', 'w') as f:
			f.write(f"import tkinter.messagebox\ntkinter.messagebox.askokcancel('{title}', '{text}')")

	else:
		pass

	#Build
	os.system('pyinstaller --noconfirm --onefile --windowed  "temp.py"')
	print(colorama.Fore.BLACK+colorama.Back.GREEN+'           Successful!          '+colorama.Fore.WHITE+colorama.Back.BLACK)
	print(colorama.Fore.BLACK+colorama.Back.GREEN+'    Saved to: /dist/temp.exe    '+colorama.Fore.WHITE+colorama.Back.BLACK)

def keylogger():
	

main()

#import tkinter.messagebox
#tkinter.messagebox.showinfo(title='Hi', message='Hello')