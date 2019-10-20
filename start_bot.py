from sense_status import *
import subprocess
import datetime

# start the bot
light_green()
bashCommand = "node bot.js"
process = subprocess.Popen(bashCommand.split())
output, error = process.communicate()

# if the bot crashes
#date = datetime.datetime.now()
#f = open(str(date) + " errorfile.txt", "a")
#f.write(error)
#f.close()
flash_red(10)