# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:03:32 2018

@author: sadvani
"""
from dateutil.relativedelta import relativedelta
import datetime
from time import sleep

def WC_countdown():
     print("2018 World Cup Countdown - press Ctrl-C to stop")
     try:
         while True:  
            today = datetime.datetime.today()
            rd = relativedelta(datetime.datetime(2018,6,14,9,00,00), today)
            print  ("World Cup starts in %(months)d months, %(days)d days, %(hours)d hours, %(minutes)d minutes and %(seconds)d seconds") % rd.__dict__
            sleep(1)
     except KeyboardInterrupt:
        pass
        
WC_countdown()
