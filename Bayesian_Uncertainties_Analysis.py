# =============================================================================
# BAYESIAN UNCERTAINTIES ANALYSIS 
# =============================================================================

# Import Python Libraries 
import arviz as az
import matplotlib.pyplot as plt
import numpy as np
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

# Define model context
average_time = 30  # Minutes (assumed known)
variability_prior_mean = 5  # Prior mean for variability
variability_prior_std = 2  # Prior standard deviation for variability

# Simulate observed commute times (replace with your actual data)
observed_commute_times = np.random.normal(loc=average_time, scale=variability_prior_std, size=100)  # Example with 100 data points

# Define the true variability for simulation (unknown in practice)
true_variability = np.random.normal(loc=variability_prior_mean, scale=variability_prior_std)

# Simulate actual commute times based on true variability (hidden information)
actual_commute_times = np.random.normal(loc=average_time, scale=true_variability, size=100)

# **Analysis using arviz (assuming you don't have access to true variability)**

# 1. Define the likelihood function (represents how likely observed data is under different variability values)
def likelihood(variability, data):
  return np.exp(-0.5 * np.sum(((data - average_time) / variability) ** 2))

# 2. Sample a range of possible variability values (assuming a uniform prior)
variability_grid = np.linspace(0, 10, 100)  # Adjust range based on expected variability

# 3. Calculate likelihood for each variability value
likelihoods = np.array([likelihood(var, observed_commute_times) for var in variability_grid])

# 4. Normalize likelihoods to get posterior probabilities (considering prior is uniform here)
posterior_probs = likelihoods / likelihoods.sum()

# 5. Sample possible commute times based on the posterior distribution (weighted by likelihoods)
sampled_commute_times = np.random.choice(actual_commute_times, size=100, replace=True, p=posterior_probs)

# Analyze the sampled commute times (posterior predictive distribution)
estimated_average_arrival_time = sampled_commute_times.mean()
arrival_time_std = sampled_commute_times.std()

print("Estimated average arrival time (considering uncertainty in variability):", estimated_average_arrival_time, "minutes")
print("Uncertainty in arrival time (standard deviation):", arrival_time_std, "minutes")
X = 99