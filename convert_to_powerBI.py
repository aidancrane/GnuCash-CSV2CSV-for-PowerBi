import csv
from re import sub
from decimal import Decimal
import time


# If we only want the transactions values, set this to true and they will print to console, they do not save to accounts_out.csv!
numbersOnly = False

# Anyone thats not me will want this to be false, this is used to show the transaction data on a live graph I use for scratching around with.
smoothieChartEmulation = False
sessionCookie = "39494goodluckguessingthispartlololol213232expiresanyway"

# Leave this here so that Notepad++ and Atom auto-suggest it.
# Date,Account Name,Number,Description,Notes,Memo,Category,Type,Action,Reconcile,To With Sym,From With Sym,To Num.,From Num.,To Rate/Price,From Rate/Price

if (smoothieChartEmulation):
     import requests

# Negative Numbers are bracketed when exported from GNUCash so we need to fix that for the float data type.
def convert_if_negative(number):
    returnNumber = str(number)
    if ("," in returnNumber):
        if ("(" in returnNumber):
            returnNumber = returnNumber[1:]
            returnNumber = returnNumber[:-1]
            returnNumber = returnNumber.replace(",", "")
            returnNumber = 0 - round(float(returnNumber), 2)
        returnNumber = str(returnNumber).replace(",", "")
    if ("(" in returnNumber):
        returnNumber = Decimal(sub(r'[^\d.]', '', returnNumber))
        return (0 - round(float(returnNumber), 2))
    return returnNumber

# open accounts.cvs, our exported file.
with open("accounts.csv", "r") as csvIn:
    reader = csv.DictReader(csvIn)
    entries = []

    runningTotal = float(0)
    
	# Save
    for row in reader:
        if (row["Account Name"] == ""):
            pass
        else:
            runningTotal = runningTotal + float(convert_if_negative(row["To Num."]))
            if (numbersOnly):
                print(str(round(runningTotal, 2)))
            else:
                if (smoothieChartEmulation):
                    payload = {'random_graph': runningTotal}
                    r = requests.get('https://dash.infinityflame.co.uk/dash/flex.php', params=payload, cookies={'PHPSESSID': sessionCookie})
                print(str(convert_if_negative(row["To Num."])) + " Description: "+ row["Description"] + " Account Balance: " + str(round(runningTotal, 2)))
                entries.append([row["Date"],row["Description"],row["Category"],str(convert_if_negative(row["To Num."])),str(round(runningTotal, 2))])

# Save what we care about to our new csv for power BI   
with open('accounts_out.csv', mode='w', newline='') as csvOut:
    titles = ["Date","Description","Destination","Transaction","Account Balance"]
    writer = csv.writer(csvOut, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(titles)
    for transaction in entries:
        writer.writerow(transaction)
