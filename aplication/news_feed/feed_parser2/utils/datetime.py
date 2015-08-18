# -*- coding: utf-8 -*-


from datetime import datetime, date
import re


def parse_str2datetime(aDateString):
    """parse a UTC date in "Seg, 17 Ago 2015 17:33:23 -0300" format"""
    today = date.today()

    date_pattern = re.compile(
        r'(\w{3}), (\d{2})(\w{3})(\d{4})(\d{2}): (\d{2}): (\d{2})'
    )

    day, str_month, year,\
        hour, minute, second = date_pattern.search(aDateString).groups()

    months_pt_BR = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']

    months_en_EUA = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                     'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    try:
        month = months_en_EUA.index(str_month.upper()) + 1
    except ValueError:
        month = months_pt_BR.index(str_month.upper()) + 1
    except:
        month = today.month

    obj_datetime = datetime(int(year), month, int(day),
                            int(hour), int(minute), int(second)
                            )
    return obj_datetime
