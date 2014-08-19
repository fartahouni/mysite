__author__ = 'farzanehtahooni'
#​ -*- coding: utf-8 -*-​

from django import template


register = template.Library()


@register.filter()
def sub(start_time,end_time):

    if end_time.hour - start_time.hour == 0:
        min_diff = end_time.minute - start_time.minute
        return str(min_diff)+' '+'دقیقه'
    elif end_time.minute - start_time.minute < 0 :
        min_diff = end_time.minute+60 - start_time.minute
        hour_diff = end_time.hour - start_time.hour - 1
        if hour_diff == 0:
            return str(min_diff)+' '+'دقیقه'
    else:
        min_diff = end_time.minute- start_time.minute
        hour_diff = end_time.hour-start_time.hour
    return str(hour_diff)+' '+'ساعت'+' '+ str(min_diff)+' '+'دقیقه'

@register.filter()
def address(name):
    result = str(name).split('/')
    result = '/' + result[-3] + '/' + result[-2] + '/' + result[-1]
    return result