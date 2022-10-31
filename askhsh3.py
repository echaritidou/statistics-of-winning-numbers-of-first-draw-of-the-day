import requests
import json
import datetime
import collections

lst = []
lst2 = []
lst3 = []
wn = []
tmp = []
#Φτιάχνω μία μεταβλητή με την τωρινή ημερομηνία
cur_date = datetime.datetime.now()
#Επαναλαμβάνω για 1 μήνα (31 ημέρες)
for i in range(31):
    #Εαπαναλμβάνω για όλες τις σελίδες που περιέχουν τα winningNumbers
    for j in range(1,19):
        np = j
        #Υπολογίζω από τη σημερινή ημερομηνία και κάθε φορά μείον μία μέρα
        cur_date = cur_date - datetime.timedelta(days=1)
        #Μετατρέπω την ημερομηνία στη μορφή που τη θέλω για το url
        date_str = cur_date.strftime("%Y-%m-%d")
        #Παίρνω από τη διεύθυνση τα δεδομένα
        ad = requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/{date_str}/{date_str}?page{np}")
        data = json.loads(ad.content)
        #Βρίσκω τα winningNumbers και τα βάζω σε λίστα
        for scan in data["content"]:
            wn = scan.get("winningNumbers")
            lst.append(scan["winningNumbers"])
        #Βάζω σε λίστα τις 20σάδες
        for scan in lst:
            tmp = scan.get("list")
            lst2.append(scan["list"])
    #Βάζω σε λίστα τις λίστες με τις πρώτες κληρώσεις της ημέρας
    lst3.append(lst2.pop())
#Βάζω σε μία λίστα ενιαία όλα τα νούμερα από τις πρώτες κληρώσεις της ημέρας
lst4=[]
for i in lst3:
    lst4.extend(i)
#Βγάζω τα στατιστικά των αριθμών των πρώτων κληρώσεων της ημέρας
counter=collections.Counter(lst4)
print("The statistics of the numbers that win the first draw of the day of the month are: \n",counter.most_common())





