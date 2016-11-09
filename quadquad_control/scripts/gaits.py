from quadquad_hardware.msg import QuadServos
import time
import numpy as np

class Gait(object):
  def __init__(self):
    self.timestep = 0

  def get_next_position(self, timestep, speed, direction):
    msg = QuadServos
    msg.BLHip = 90.0
    msg.BRHip = 90.0
    msg.FLHip = 90.0
    msg.FRHip = 90.0

    msg.BLLeg = 0.0
    msg.BRLeg = 0.0
    msg.FLLeg = 0.0
    msg.FRLeg = 0.0
    return msg


class CreepGait(Gait):
  def __init__(self):
    self.index = 0
    self.timestep = 0
    self.hip = np.array([  0.00000000e+00,   6.95427857e-02,   1.36248000e-01,
         2.00159500e-01,   2.61321143e-01,   3.19776786e-01,
         3.75570286e-01,   4.28745500e-01,   4.79346286e-01,
         5.27416500e-01,   5.73000000e-01,   6.16140643e-01,
         6.56882286e-01,   6.95268786e-01,   7.31344000e-01,
         7.65151786e-01,   7.96736000e-01,   8.26140500e-01,
         8.53409143e-01,   8.78585786e-01,   9.01714286e-01,
         9.22838500e-01,   9.42002286e-01,   9.59249500e-01,
         9.74624000e-01,   9.88169643e-01,   9.99930286e-01,
         1.00000000e+00,   1.00000000e+00,   1.00000000e+00,
         1.00000000e+00,   1.00000000e+00,   1.00000000e+00,
         1.00000000e+00,   1.00000000e+00,   1.00000000e+00,
         1.00000000e+00,   1.00000000e+00,   1.00000000e+00,
         1.00000000e+00,   1.00000000e+00,   9.91962786e-01,
         9.81128000e-01,   9.69253786e-01,   9.56384000e-01,
         9.42562500e-01,   9.27833143e-01,   9.12239786e-01,
         8.95826286e-01,   8.78636500e-01,   8.60714286e-01,
         8.42103500e-01,   8.22848000e-01,   8.02991643e-01,
         7.82578286e-01,   7.61651786e-01,   7.40256000e-01,
         7.18434786e-01,   6.96232000e-01,   6.73691500e-01,
         6.50857143e-01,   6.27772786e-01,   6.04482286e-01,
         5.81029500e-01,   5.57458286e-01,   5.33812500e-01,
         5.10136000e-01,   4.86472643e-01,   4.62866286e-01,
         4.39360786e-01,   4.16000000e-01,   3.92827786e-01,
         3.69888000e-01,   3.47224500e-01,   3.24881143e-01,
         3.02901786e-01,   2.81330286e-01,   2.60210500e-01,
         2.39586286e-01,   2.19501500e-01,   2.00000000e-01,
         1.81125643e-01,   1.62922286e-01,   1.45433786e-01,
         1.28704000e-01,   1.12776786e-01,   9.76960000e-02,
         8.35055000e-02,   7.02491429e-02,   5.79707857e-02,
         4.67142857e-02,   3.65235000e-02,   2.74422857e-02,
         1.95145000e-02,   1.27840000e-02,   7.29464286e-03,
         3.09028571e-03,   2.14785714e-04,   0.00000000e+00,
         0.00000000e+00])
    self.leg = np.array([ 0.        ,  0.09983342,  0.19866933,  0.29552021,  0.38941834,
        0.47942554,  0.56464247,  0.64421769,  0.71735609,  0.78332691,
        0.84147098,  0.89120736,  0.93203909,  0.96355819,  0.98544973,
        0.99749499,  0.9995736 ,  0.99166481,  0.97384763,  0.94630009,
        0.90929743,  0.86320937,  0.8084964 ,  0.74570521,  0.67546318,
        0.59847214,  0.51550137,  0.42737988,  0.33498815,  0.23924933,
        0.14112001,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ])



  def get_next_position(self, curtime, speed, direction):
    msg = QuadServos()
    if speed == 0 and direction == 0:
      msg.BLHip = 90.0
      msg.BRHip = 90.0
      msg.FLHip = 90.0
      msg.FRHip = 90.0

      msg.BLLeg = 0.0
      msg.BRLeg = 0.0
      msg.FLLeg = 0.0
      msg.FRLeg = 0.0
      return msg

    msg.FRHip = self.hip[self.index % len(self.hip)]
    msg.FRLeg = self.leg[self.index % len(self.leg)]

    self.index += 1

    return msg


