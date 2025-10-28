""" Module for Intrest Calculations"""

def simple_interest(prin,ny,roi):
    """
    calculating Simple Intrest
    :param prin: principal amount
    :param ny: No. of years
    :param roi: Rate of interest
    :return:  Simple Interest,Total amount
    """
    si = prin * ny * roi
    amount = prin + si
    return si , amount

def compound_interest(prin,t,roi):
    """
    calculating Intrest
    :param prin: Principal amount
    :param ny: No. of years
    :param roi: Rate of interest
    :return:Total amount
    """
    amount = prin *(1 + (roi / 100)) ** (1 * ny)
    return amount
