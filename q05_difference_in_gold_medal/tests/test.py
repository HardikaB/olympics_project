import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_difference_in_gold_medal
from inspect import getfullargspec
import pandas

path = "data/olympics.csv"
df = q05_difference_in_gold_medal(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q05_difference_in_gold_medal).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return(self):
        self.assertEqual(df, 880, "The Expected return does not match the return")
