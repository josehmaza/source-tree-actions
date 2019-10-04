import pyperclip
import sys
import datetime
import os

# ========== =
#1 $REPO (D:\workspaces\workspace-locales-4\max-recipientes-parent-4)
#2 $FILE (max-recipientes-ws/src/main/java/ec/com/smx/sic/recipientes/webservices/PedidoSuperSaldosWS.java)
#3 $command_type --full-address  | --name-file

class Command_type:
	full_address = '--full-address'
	file_name = '--file-name'

try:
	if len(sys.argv) == 4:
		repo_address, file_address, command_type = sys.argv[1:]
		full_address = repo_address.replace('\\', '/') + '/' + file_address
		only_file_name = os.path.basename(full_address)

		if command_type == Command_type.full_address:
			pyperclip.copy(full_address)

		if command_type == Command_type.file_name:
			pyperclip.copy(only_file_name)
	else:
		print 'incorrect arguments '+str(len(sys.argv))
		print sys.argv
		raise Exception('Incorrect arguments')
		

except Exception as error:		
	f = open("error.txt", "a")
	datetime_object = datetime.datetime.now()
	f.write(str(datetime_object)+" "+str(error)+" \n")
	f.close()
	print("An exception occurred: "+str(error))




