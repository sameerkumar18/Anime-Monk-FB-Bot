'''
MIT License
Copyright (c) 2017 Sameer Kumar
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import csv


def csvv(email):
    f = open('email.csv', 'a')
    writer = csv.writer(f, dialect='excel')
    writer.writerow([email])


def main(id,passd):
    url = 'https://www.facebook.com'
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.get(url)

    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('pass')

    username.send_keys(id)
    password.send_keys(passd)
    password.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.get('https://www.facebook.com/groups/animemonk/requests/')

    for i in range(0,50):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.1)

    #rest = '//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/ul/li'
    words = ['Yes', 'yes', 'Yea', 'yea', 'Ofcourse', 'ofcourse', 'Will do', 'will do', 'Soon', 'soon', 'interesting','yeah','Yeah','yuss','Yuss','yus','Yus']
    #words are case sensitive



    #1

    for z1 in range(1,50):


        try:
            #z = 21
            one = '\0'
            two = '\0'

            wholer = driver.find_element_by_xpath('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/ul/li['+str(z1)+']')
            whole = wholer.text #done

            try:
                search_email = re.search(r'[\w\.-]+@[\w\.-]+', whole)
                email = search_email.group(0)
                print email
                csvv(email)
                one = 1

            except:

                print ' okay not email'


            zero = whole[whole.find('Did you like our page at fb.com/animemonk'):]


            if any(x in zero for x in words): #if zero.find('safe') != -1:
                two = 2

            else:
                print ' okay not words'



            if one == 1 or two == 2:
                try:
                    approve = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/ul/li['+str(z1)+']//a[@name="approve button"]')).click()
                    print str("clicks approve")
                    #print one
                    #print two
                except:
                    print "unable to be approve"
        except:
            print 'Unsuccessful'

    print '\n\n\n\n\n\nthis is second xDD'



            #2

    for z2 in range(1,50):
        try:
            #z = 21
            one = '\0'
            two = '\0'
            rest = ''
            wholer = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li['+str(z2)+']'))
            #//*[@id="u_a_1e"]/ul//li[1]
            whole = wholer.text #done

            try:
                search_email = re.search(r'[\w\.-]+@[\w\.-]+', whole)
                email = search_email.group(0)
                print email
                csvv(email)
                one = 1

            except:

                print ' okay not email'


            zero = whole[whole.find('Did you like our page at fb.com/animemonk'):]

            if any(x in zero for x in words): #if zero.find('safe') != -1:
                two = 2


            else:
                print ' okay not words'



            if one == 1 or two == 2:
                try:
                    approve = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li['+str(z2)+']//a[@name="approve button"]')).click()
                    print str('clicks approve')
                    #print one#//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li[2]//a[@name="approve button"]
                    #print two
                except:
                    print "unable to be approve"
        except:
            print 'Unsuccessful'

    print '\n\n\n\n\n\nthis is third xDD'



            #3

    for z3 in range(1,50):
        try:
            #z = 21
            one = '\0'
            two = '\0'
            rest = ''
            wholer = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li['+str(z3)+']'))
            #//*[@id="u_a_1e"]/ul//li[1]
            whole = wholer.text #done

            try:
                search_email = re.search(r'[\w\.-]+@[\w\.-]+', whole)
                email = search_email.group(0)
                print email
                csvv(email)
                one = 1

            except:

                print ' okay not email'


            zero = whole[whole.find('Did you like our page at fb.com/animemonk'):]

            if any(x in zero for x in words): #if zero.find('safe') != -1:
                two = 2


            else:
                print ' okay not words'



            if one == 1 or two == 2:
                try:
                    approve = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/div/ul/li['+str(z3)+']//a[@name="approve button"]')).click()
                    print str('clicks approve')
                    #print one#//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li[2]//a[@name="approve button"]
                    #print two
                except:
                    print "unable to be approve"
        except:
            print 'Unsuccessful'

    print '\n\n\n\n\n\nthis is fourth xDD'
            #4

    for z4 in range(1,50):
        try:
            #z = 21
            one = '\0'
            two = '\0'
            rest = ''
            wholer = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li['+str(z4)+']'))
            #//*[@id="u_a_1e"]/ul//li[1]
            whole = wholer.text #done

            try:
                search_email = re.search(r'[\w\.-]+@[\w\.-]+', whole)
                email = search_email.group(0)
                print email
                csvv(email)
                one = 1

            except:

                print ' okay not email'


            zero = whole[whole.find('Did you like our page at fb.com/animemonk'):]

            if any(x in zero for x in words): #if zero.find('safe') != -1:
                two = 2


            else:
                print ' okay not words'



            if one == 1 or two == 2:
                try:
                    approve = driver.find_element_by_xpath(str('//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li['+str(z4)+']//a[@name="approve button"]')).click()
                    print str('clicks approve')
                    #print one#//*[@id="pagelet_requests_queue"]/div/div[2]/div/div/div/ul/li[2]//a[@name="approve button"]
                    #print two
                except:
                    print "unable to be approve"
        except:
            print 'Unsuccessful'


id = raw_input("Enter ID: ")
passd = raw_input("Enter Password: ")
for i in range(0,4):

    main(id,passd)
    time.sleep(10)
