###Imports###
import git
from selenium import webdriver
import os
import subprocess
from time import sleep
import sys

###Decide Name###
repoName = sys.argv[1]

###Path###
mainPath = "$PATH TO MAIN FOLDER$"

###Make Files###
os.chdir(mainPath)
os.mkdir(repoName)
os.chdir(mainPath + "/" + repoName)
subprocess.call(['touch', repoName + ".py"])
subprocess.call(['touch', "README.md"])

###GITHUB PART###
subprocess.Popen(['git', 'init'])

browser = webdriver.Firefox()
browser.get("https://www.github.com/login")

username = browser.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys("$USERNAME HERE$")

password = browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys("$PASSWORD HERE$")

sign_in = browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')
sign_in.click()

browser.get("https://www.github.com/new")
gitreponame = browser.find_element_by_xpath('//*[@id="repository_name"]')
gitreponame.send_keys(repoName)

sleep(2)

create = browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
create.click()

remote = browser.find_element_by_xpath('/html/body/div[4]/div/main/div[3]/div/git-clone-help/div[2]/div[1]/div/pre/span[5]/span').get_attribute("innerHTML")

browser.quit()

#remove geckodriver
os.remove("geckodriver.log")

#Setting up remote git
subprocess.Popen(['git', 'remote', 'add', 'origin', remote])
#Adding file 
subprocess.Popen(['git', 'add', '.'])
#Initial commit
subprocess.Popen(['git', 'commit', '-m', '"first commit"'])
#Pushing to github
subprocess.Popen(['git', 'push', '-u', 'origin', 'master'])
sys.stdout.write("$USERNAME HERE$")
sys.stdout.write("$PASSWORD HERE$")
#Open Visual Studio Code
subprocess.call(['code', '.'])
