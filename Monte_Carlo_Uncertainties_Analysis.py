# =============================================================================
# MONTE CARLO UNCERTAINTIES ANALYSIS 
# =============================================================================

# Import Python Libraries 
import matplotlib.pyplot as plt
import random

# Problem Context 
"""
Imagine you have a somewhat unpredictable commute to work each day. 
Factors like traffic conditions, weather, and public transit delays can significantly impact your travel time. 
Being able to estimate your arrival time more accurately can help you manage your schedule and avoid unnecessary stress.

Monte Carlo Simulation Approach:
    A. Identify Uncertainties Variables:
        There are two uncertainties variable in this case, which are 
        - Average_Time (Track your daily commute time for a period to establish an average).
        - Variability (Analyze the historical data to determine the typical range or standard deviation of your commute times).
    B. Simulate Daily Commute:
        Generate random values within the defined range or probability distribution for your commute time each day.
    C. Analyze Results:
        Calculate the estimated arrival time for each simulated commute.
    D. Interpretation:
        The average completion time across simulations provides a more realistic estimate compared to a single baseline plan.
"""

# Set the daily commute variable 
average_time    = 30  # Average commute time (Minutes)
variability     = 5   # Minutes (standard deviation)
num_simulations = 100 # Number of simmulations

# Create a normal distribution data based on average time, variability, and number of simulations
def simulate_commute_time(average_time, variability):
    global commute_time, arrival_times
    arrival_times = []                                     # Empty list to store normal (gauss) distribution
    for i in range(num_simulations):
        commute_time = random.gauss(average_time, variability)  # Pick a random number within a normal (gauss) distribution
        arrival_times.append(commute_time)                      # Append the random number into the normal (gauss) distribution
simulate_commute_time(average_time, variability)

# Estimate average arrival time 
estimated_average_arrival_time = sum(arrival_times) / num_simulations
print("Estimated average arrival time:", estimated_average_arrival_time, "minutes")

# Plot the normal distribution for the commute time 
plt.figure(figsize=(8, 6), dpi=300)
plt.hist(arrival_times, bins=20, edgecolor='black')  # Adjust bins as needed
plt.xlabel("Commute Time (minutes)")
plt.ylabel("Frequency")
plt.title("Distribution of Simulated Commute Times")
plt.axvline(estimated_average_arrival_time, color='r', linestyle='dashed', linewidth=2, label='Average')
plt.legend(loc='upper left') 
plt.grid(True)
plt.show()

