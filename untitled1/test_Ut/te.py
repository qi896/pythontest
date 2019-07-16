import unittest
from jmeter.ss import ss


s = ss()
list = ['testone','testtwo','testthree','testfour','testfive']
for i in list:
    if i == 'testone':
        s.testone()

    elif i == 'testtwo':
        s.testtwo()