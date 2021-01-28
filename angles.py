# -*- coding: utf-8 -*-
import math


def deg2grad(deg):
    grad = (deg * 10) / 9
    return grad


def grad2deg(grad):
    deg = (grad * 9) / 10
    return deg


def grad2rad(grad):
    rad = (grad * math.pi) / 200

    return rad


def rad2grad(rad):
    grad = (rad * 200) / math.pi

    return grad


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    rad = (decimal_deg * math.pi) / 180

    return rad


def rad2decimal_deg(rad):
    dec = (rad * 180) / math.pi

    return dec



# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    min, sek = divmod(decimal_deg * 3600, 60)
    deg, min = divmod(min, 60)

    return deg, min, sek


def dms_deg2decimal_deg(dms_deg):
    decimal_deg = float(dms_deg[0]) + float(dms_deg[1]) / 60 + float(dms_deg[2]) / 3600

    return decimal_deg

# ======================== for 5
