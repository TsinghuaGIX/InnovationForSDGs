# -*- encoding: utf-8 -*-
'''
@File    :   ColorUtils
@Time    :   2024/07/15
@Author  :   
@E-mail  :   
@License :   MIT
'''
import math

class ColorUtils:
    """! 
    

    @color #0FB1D2
    @link https://github.com/m5stack
    @category CUSTOM


    """


    def __init__(self):
        """! 
        @en %1 init

        """
        

    def HSV2RGB(self,hue:int=0,val:float=0,sat:float=0) -> any :
        """! 
        @en HSV2RGB %1 hue %2 val %3 sat %4

        @param hue
        @param val
        @param sat
        """
        h = hue
        s = sat
        v = val
        h = float(h)
        s = float(s)
        v = float(v)
        h60 = h / 60.0
        h60f = math.floor(h60)
        hi = int(h60f) % 6
        f = h60 - h60f
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        r, g, b = 0, 0, 0
        if hi == 0: r, g, b = v, t, p
        elif hi == 1: r, g, b = q, v, p
        elif hi == 2: r, g, b = p, v, t
        elif hi == 3: r, g, b = p, q, v
        elif hi == 4: r, g, b = t, p, v
        elif hi == 5: r, g, b = v, p, q
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        return [r, g, b]