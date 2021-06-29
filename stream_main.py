import ctypes
import numpy as np
import time
from picosdk.usbtc08 import usbtc08 as tc08
from picosdk.functions import assert_pico2000_ok
import sys

from pico_stream import pico_stream

for i in range(0,11):
  print (pico_stream())
