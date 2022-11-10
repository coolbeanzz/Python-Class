#Author: Robert Murphy
#Class: Python 307
# Final project
#date 5/22/22

import ssl
import re

#Takes a domain string and checks if it has an active ssl certificate on port 443.
#The check's results are recorded in a text file called "certificate_log.txt".
def ssl_checker(url):
    try:
        ssl.get_server_certificate((url, 443))
        file2 = open("certificate_log.txt", "a")
        file2.write(url)
        file2.write("\tis SECURE with an active ssl cert!\n")
        file2.close()
    except:
        file2 = open("certificate_log.txt", "a")
        file2.write(url)
        file2.write("\tis UNSECURE! There is no active ssl cert on port 443 in this domain.\n")
        file2.close()

#Imported domains from "domains.txt" are sanitized here so that
#ssl_checker() can interprit them without error
def domain_cleaner(url):
    new_url = re.search(".*\....", url)
    return new_url.group()

#Reads each line from "domains.txt" into distinct string variables and sends them to respective functionss.
#Also, alerts user of the program's status.
if __name__ == '__main__':
    print("working...")
    try:
        domains = open("domains.txt", "r")

        url_1 = domains.readline()
        new_1 = domain_cleaner(url_1)
        ssl_checker(new_1)

        url_2 = domains.readline()
        url_2 = re.search(".*\...", url_2)
        new_2 = url_2.group()
        ssl_checker(new_2)

        url_3 = domains.readline()
        new_3 = domain_cleaner(url_3)
        ssl_checker(new_3)

        url_4 = domains.readline()
        new_4 = domain_cleaner(url_4)
        ssl_checker(new_4)

        url_5 = domains.readline()
        ssl_checker(url_5)

        domains.close()
        print("Finished!\nOpen \"certificate_log.txt\" in your present working directory for results.")
    except FileNotFoundError as fnfe:
        print("File is not in dir")
