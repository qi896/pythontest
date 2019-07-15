import sys
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\untitled1")
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\untitled1\\venv\\Lib\\site-packages\\BeautifulReport")
import unittest
from jmeter.test import *
from BeautifulReport import BeautifulReport




if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [sum('testfour'),sum('testtwo'),sum('testthee')]
    suite.addTests(tests)
    run = BeautifulReport(suite)
    run.report(filename='te', description='testreport')

