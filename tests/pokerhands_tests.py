#! /usr/bin/python

from nose.tools import *
import pokerhands

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")