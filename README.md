# Kalman-Filter
Kalman filter, also known as linear quadratic estimation (LQE), is an algorithm that uses a series of measurements observed over time, containing statistical noise and other inaccuracies, and produces estimates of unknown variables that tend to be more precise than those based on a single measurement alone, by using Bayesian inference and estimating a joint probability distribution over the variables for each timeframe. Kalman filter is a very powerful algorithm to not only remove error in the measurement from sensors but also predict the right value.

Kalman Filter can also be applied to fuse the readings of sensors for example we can fuse the readings of accelerometer and gyroscope in the navigation of a robot. In case of predicting more than 1 parameter (multi dimensional), matrices are used. But for estimating 1 parameter (1-Dimensional) equations can be reduced to a simple iterative numerical process. 
I have integrated Arduino and python using pyserial to remove glitches in the reading of ultrasonic sensor and predict the correct distance of an object.

A Closer look to the 1-D Equations used in Kalman Filter Algorithm.
First we assume an estimate and error in estimate then apply the below equations to converge the estimate to actual value. Number of iterations depends on the initial value we choose. 

