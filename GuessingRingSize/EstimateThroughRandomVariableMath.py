# For working with command-line arguments
import sys
import os
# For working with the .csv / Excel sheets:
import csv
import pandas as pd
# To work with plots and generating random numbers
import matplotlib.pyplot as plt
import numpy as np


# Some in-file utility functions
def GetClosestStandardRingSize( input_size: float ) -> float:
   STANDARD_US_RING_SIZES = [2, 3, 3.5, 4, 4.5, 5, 5.25, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]
   diff = 0.0
   diff_min = 100.0
   closest_ring_size = 100
   for ring_size in STANDARD_US_RING_SIZES:
      diff = abs(input_size - ring_size)
      if diff < diff_min:
         diff_min = diff
         closest_ring_size = ring_size

   return closest_ring_size


# Constants for the whole file
OUTPUT_CSV_FILE_NAME = 'DivOfRVs_NormUniform.csv'

# Print initial display message...
print('\nRunning EstimateThroughRandomVariableMath.py...')
print('\nTHE GOAL: Get the best estimate I can of Hope\'s ring finger size.')
print('\n...So all I\'ve got to go off of is a measurement of the diameter of Hope\'s Order of the Engineer')
print('...ring (using a rule with 1/64" markings), which is worn on a pinkie finger, super rough estimates using')
print('...the unroll-paper method of measuring my own pinkie and ring finger sizes. I am going to assume that')
print('...the ruler measurement is normally distributed around my claimed measurement, +- half a marking, and')
print('...the unroll paper method is uniformly distributed around the claimed measurement +- 3/32 inches.')
print('...This script will')
print('......1) generate samples from the random distributions of aforementioned measurements,')
print('......2) generate samples for the ratio of the measurement distributions')
print('......3) use that ratio distribution to go from my ring finger measurement to Hope\'s')
print('......4) give me the probability that Hope\'s ring finger size is any one of the standard ring sizes')
print('......5) give me a 75 percent confidence interval of Hope\'s ring finger size')
print('......6) pretty plots')
print('......7) output the utilized data in file(s)')

#########################################################################
# Obtain distribution parameters from command-line arguments
#########################################################################
# TODO: Iterate through input arguments to find parameters

# For now, I'll just go with constants in the script
# For the normal distribution
H_pinkie_ring_mu = 5.7258
H_pinkie_ring_sigma = 0.2455/2
# For the uniform distributions
A_pinkie_min = 5.66
A_pinkie_max = 7.53
A_ring_min = 8.63
A_ring_max = 10.49
# Sampling parameters
NUM_OF_SAMPLES = 1000000
print(f'Number of Samples: {NUM_OF_SAMPLES}\n')

#########################################################################
# Generate samples of distributions
#########################################################################
H_pinkie_ring_samples = np.random.normal( H_pinkie_ring_mu, H_pinkie_ring_sigma, NUM_OF_SAMPLES )
A_pinkie_samples = np.random.uniform( A_pinkie_min, A_pinkie_max, NUM_OF_SAMPLES )
A_ring_samples = np.random.uniform( A_ring_min, A_ring_max, NUM_OF_SAMPLES )

#########################################################################
# Perform Operations
#########################################################################
R_samples = np.divide( H_pinkie_ring_samples, A_pinkie_samples )
print(f'\nMean of Ratio Samples: {np.mean(R_samples)}\n')
H_ring_size_samples = np.multiply( R_samples, A_ring_samples )

#########################################################################
# Find 75% Confidence Interval
#########################################################################
DESIRED_CONFIDENCE_LEVEL = 0.75  # 75%
STARTING_RANGE_SIZE = 0.01
LOOP_RANGE_STEP = 0.01
H_ring_size_samples_mean = np.mean( H_ring_size_samples )
accumulated_num_of_samples_in_range = 0
percentage_of_accumulation = 0.0
range_size = STARTING_RANGE_SIZE
# while loop protection
loop_iterations = 0
MAX_NUM_OF_WHILE_LOOP_ITERATIONS = 1000
while percentage_of_accumulation < DESIRED_CONFIDENCE_LEVEL and loop_iterations < MAX_NUM_OF_WHILE_LOOP_ITERATIONS:
   loop_iterations = loop_iterations + 1
   accumulated_num_of_samples_in_range = 0   # Reset counter
   range_min = H_ring_size_samples_mean - (range_size / 2)
   range_max = H_ring_size_samples_mean + (range_size / 2)
   for num in H_ring_size_samples:
      if num >= range_min and num <= range_max:
         accumulated_num_of_samples_in_range = accumulated_num_of_samples_in_range + 1

   percentage_of_accumulation = accumulated_num_of_samples_in_range / NUM_OF_SAMPLES
   range_size = range_size + LOOP_RANGE_STEP

# Remove the extra range step added for final loop before exit
range_size = range_size - LOOP_RANGE_STEP


#########################################################################
# Find Probabilities of Ring Sizes in Sample Range
#########################################################################
# Start by getting the ring sizes that came out of the estimation into a list
estimation_ring_sizes = list()
for sample in H_ring_size_samples:
   closest_ring_size = GetClosestStandardRingSize(sample)
   if closest_ring_size not in estimation_ring_sizes:
      estimation_ring_sizes.append(closest_ring_size)
# Sort from smallest to largest for readability in printout
estimation_ring_sizes.sort()

# Now check each ring size and get the probability that this ring size is the one.
# I will use a range of +- 0.25 around the ring size
estimation_ring_size_probabilities = list()
for ring_size in estimation_ring_sizes:
   range_min = ring_size - 0.25
   range_max = ring_size + 0.25
   accumulation_of_samples_in_range = 0

   # Iterate through samples
   for sample in H_ring_size_samples:
      if sample >= range_min and sample <= range_max:
         accumulation_of_samples_in_range = accumulation_of_samples_in_range + 1
   
   # Determine percentage and add to list
   estimation_ring_size_probabilities.append( accumulation_of_samples_in_range / NUM_OF_SAMPLES )

#########################################################################
# Plot Histogram Results
#########################################################################
num_of_bins = int( np.sqrt(NUM_OF_SAMPLES) )
H_pinkie_ring_count, H_pinkie_ring_bins, H_pinkie_ring_ignored = plt.hist( H_pinkie_ring_samples, num_of_bins, density=True )
A_pinkie_count, A_pinkie_bins, A_pinkie_ignored = plt.hist( A_pinkie_samples, num_of_bins, density=True )
R_count, R_bins, R_ignored = plt.hist( R_samples, num_of_bins, density=True)
A_ring_count, A_ring_bins, A_ring_ignored = plt.hist( A_ring_samples, num_of_bins, density=True )
H_ring_count, H_ring_bins, H_ring_ignored = plt.hist( H_ring_size_samples, num_of_bins, density=True )

print(f'Hope\'s Ring Size Mean of Estimate:\t\t{H_ring_size_samples_mean}')
print(f'Hope\'s Ring Size 75% Confidence Interval:\t( {H_ring_size_samples_mean - (range_size / 2)}, {H_ring_size_samples_mean + (range_size / 2)} )')
print(f'...................................Range:\t{range_size}')
print('\nRing Size Probabilities:')
for loop_counter, ring_size in enumerate(estimation_ring_sizes):
   print(f'\tRing Size: {ring_size}\tProbability: {estimation_ring_size_probabilities[loop_counter] * 100}%')

plt.plot( H_pinkie_ring_bins, 1/(H_pinkie_ring_sigma * np.sqrt(2*np.pi)) * np.exp( - (H_pinkie_ring_bins - H_pinkie_ring_mu)**2 / (2 * H_pinkie_ring_sigma**2) ), linewidth=2, color='r' )
plt.plot( A_pinkie_bins, np.divide( np.ones_like(H_pinkie_ring_bins), (A_pinkie_max - A_pinkie_min) ), linewidth=2, color='r' )
plt.plot( A_ring_bins, np.divide( np.ones_like(H_ring_bins), (A_ring_max - A_ring_min) ), linewidth=2, color='r' )
plt.show()

# TODO:
# I'll plot the normal distribution first, then the uniform, then the ratio samples
# This will be in a 3x1 grid (3 rows, 1 column)
# fig, axs = plt.subplots(3)
# axs[0].plot( H_pinkie_ring_bins, 1 / (H_pinkie_ring_sigma * np.sqrt(2*np.pi)) * np.exp( - (H_pinkie_ring_bins - H_pinkie_ring_mu)**2 / (2 * H_pinkie_ring_sigma**2) ), linewidth=2, color='r' )
# axs[1].plot( A_pinkie_bins, np.ones_like(A_pinkie_bins), linewidth=2, color='r' )
# plt.show()
#axs[0].plot( R_bins, 1 / (R_sigma * np.sqrt(2*np.pi)) * np.exp( - (R_bins - R_mu)**2 / (2 * R_sigma**2) ), linewidth=2, color='r' )

#########################################################################
# Output information to a csv file
#########################################################################
# TODO:
# Use the name of the input log file for the csv file
# output_csv_file_name = file_name[0:-4] + '.csv'
# print(f'Exporting to {output_csv_file_name} file...')
# with open( output_csv_file_name, 'w', newline='' ) as output_csv_file:
#    writer = csv.writer( output_csv_file )
#    writer.writerow( ['Left Inverter Address Claim Timestamp (ms)', startup_event_timestamps['Left Inverter Address Claim Timestamp (ms)'] ] )
#    writer.writerow( ['Right Inverter Address Claim Timestamp (ms)', startup_event_timestamps['Right Inverter Address Claim Timestamp (ms)'] ] )
#    writer.writerow( ['Left Inverter Invalid to Valid Timestamp (ms)', startup_event_timestamps['Left Inverter Invalid to Valid Timestamp (ms)'] ] )
#    writer.writerow( ['Left Inverter Invalid to Valid Timestamp (ms)', startup_event_timestamps['Right Inverter Invalid to Valid Timestamp (ms)'] ] )
#    writer.writerow('')
#    writer.writerow( [ 'Time Stamp (ms)', 'Left Motor Speed', 'Right Motor Speed', 'Left Motor Torque', 'Right Motor Torque', 'Left Motor Speed Estimate', 'Right Motor Speed Estimate' ] )
# 
#    for item in log_dictionary_list:
#       row = [ item['Time Stamp (ms)'], item['Left Motor Speed'], item['Right Motor Speed'], item['Left Motor Torque'], item['Right Motor Torque'], item['Left Motor Speed Estimate'], item['Right Motor Speed Estimate'] ]
#       writer.writerow( row )
# 
# print('Done! :D\n')