# erp-bot
This is an application that was made for my personalized use. It uses selenium to get information from institute ERP website (of **Indian Institute of Technology Kharagpur**). This was made during placement process for automatically checking and notifying me if number of companies changed. 

## Instructions to run this:

- Clone this repository
- Make sure Python is installed. check - `python --version`
- Install Selenium - `pip3 install selenium` . (Required - Selenium version 4.3.0)
- Make changes and enter your login credentials in the file ‘erp-bot.py’. Note: ‘data.txt’ is required in the file directory to run this
- open ‘cmd’ and cd to the file directory.
- Execute the file - `python erp-bot.py`

A video of test run for this app is included in the git repo.

This code can also be used to login automatically to the institute website. by making the following changes.

- comment out lines 31-74. (select and press `Ctrl+/`)
- change `time.sleep(5)` value to something bigger and execute the code
- to exit the app, press `Ctrl+C` ,this will also close the browser.
