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
average_time    = 60  # Average commute time (Minutes)
variability     = 30  # Standard deviation (Minutes)
num_simulations = 500 # Number of simmulations 
late_threshold  = 75  # Time to be considered as late (Minutes)
bridge_closure_probability  = 0.1  # Probability of a bridge closure (10%)
bridge_closure_delay        = 5   # Additional delay due to bridge closure (Minutes)

# Create a normal distribution data based on average time, variability, and number of simulations
def simulate_commute_time(average_time, variability):
    global commute_time, arrival_times, late_arrivals
    late_arrivals = 0
    arrival_times = []  # Empty list to store normal (gauss) distribution
    for i in range(num_simulations):
        # Create a normal (gauss) distribution and pick a random instance from it
        commute_time = random.gauss(average_time, variability) 
        # Simulate discrete event such as bridge closure
        if random.random() < bridge_closure_probability:
            commute_time += bridge_closure_delay  
        arrival_times.append(commute_time)
        # Count late arrivals
        if commute_time > late_threshold:
            late_arrivals += 1  # Count late arrivals
simulate_commute_time(average_time, variability)

# Estimate average arrival time and late arrival probability
average_arrival_time = sum(arrival_times) / num_simulations
late_arrival_probability = round(late_arrivals / num_simulations * 100, 2) 
print("Estimated average arrival time:", average_arrival_time, "minutes")
print("Estimated probability of arriving late:", late_arrival_probability , "%")  # Convert to percentage

# Prepare a label for the legend entry with probability information
late_arrival_label = "Late Arrival Prob (" + str(late_arrival_probability) + "%)"

# Plot the normal distribution for the commute time 
plt.figure(figsize=(8, 6), dpi=300)
plt.hist(arrival_times, bins=20, edgecolor='black')  # Adjust bins as needed
plt.xlabel("Commute Time (minutes)")
plt.ylabel("Frequency")
plt.title("Distribution of Simulated Commute Times")
plt.axvline(average_arrival_time, color='r', linestyle='dashed', linewidth=2, label='Average')
plt.axvline(late_threshold, color='g', linestyle='dashed', linewidth=2, label='Late Threshold')
plt.legend(loc='upper left', labels=['Average', 'Late Threshold', late_arrival_label])
plt.grid(True)
plt.show()
