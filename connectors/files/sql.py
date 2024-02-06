# -*- coding: UTF-8 -*-
#######################################
# SQL File
#######################################
#
# Principle: https://docs.fileformat.com/database/sql/
# Library: pandas (https://github.com/pandas-dev/pandas)
# Author: Rik Heijmann
#

from logger import log
import modin.pandas as pandas
import lxml


####################
# Extract
####################
def get_data(file, connection):
    return pandas.read_sql(file, connection)