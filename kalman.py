import serial
from visual import *
import sys
a=serial.Serial('com5', 9600)# a is an object for serial communication
def K_Gain(E_est,E_mea):
    k=(E_est)/(E_est+E_mea)# estimating kalman gain(measure of what % of estimate and measurement we have to take)
    return(k)
def Estimate(mea,k,Prev_Estimate):
    z=0.0
    z=(Prev_Estimate+k*(mea-Prev_Estimate))# calculating estimate based upon the previous estimate
    return (z)
def E_estimate(K,Prev_Error):
    error=0.0
    error=(Prev_Error*(1-K))# calculating the error in the estimate
    return(error)
E_est=10.0# my guess is 10cm(can be any value)
E_mea=2.0# max error depending upon the sensor
estimate=100.0# my guess is 100cm(can be any value)
while(1==1):
   while(E_est>0.1):
        if(a.inWaiting()>0):
            s=a.readline()# getting measurement from sensor
            mea=float(s)
            k=K_Gain(E_est,E_mea)
            estimate=Estimate(mea,k,estimate)
            E_est=E_estimate(k,E_est)
   print(estimate,mea)
   E_est=10.0
   estimate=100.0
