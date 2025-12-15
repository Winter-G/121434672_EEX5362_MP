# Canteen Simulation - 121434672_EEX5362_MP

## Overview

This project simulates a simple canteen service system using **SimPy**, a process-based discrete-event simulation framework in Python.  
The simulation models customers arriving, waiting for service, and being served by multiple servers. It also captures peak periods and calculates basic performance metrics.

---

## Features

- Models customer arrivals with a base arrival rate and a **peak multiplier** during busy periods.  
- Tracks **waiting times**, **service times**, and **overall system events**.  
- Uses **multiple servers** to handle customers concurrently.  
- Prints a **sample event log** and summary **statistics** including average waiting time and 90th percentile waiting time.

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| `SIM_TIME` | Total simulation time in minutes (default: 120) |
| `MEAN_SERVICE` | Average service time per customer in minutes (default: 3) |
| `ARRIVAL_RATE` | Base customer arrival rate per minute (default: 0.5) |
| `PEAK_MULTIPLIER` | Multiplier for arrival rate during peak (default: 1.8) |
| `NUM_SERVERS` | Number of servers available (default: 3) |

---

## How to Run

1. Make sure you have Python installed (3.7 or higher recommended).  
2. Install **SimPy** if not already installed:
pip install simpy

3. Run the simulation:
python canteen_sim.py

4. Observe the output:
Event log (first 10 customers)
Total customers served
Average waiting time
90th percentile waiting time


Sample Output
------ Event Log (Sample) ------
Cust | Arrive | Start | End | Wait
['C1', 0.23, 0.23, 2.90, 0.0]
['C2', 1.45, 1.45, 4.12, 0.0]
...
------ Statistics ------
Total Customers Served: 50
Average Waiting Time: 1.34
90th Percentile: 3.2

Notes
Arrival rates change between 30 and 60 minutes to simulate a peak period.
The simulation is stochastic; results vary between runs.
Only canteen_sim.py is tracked in this repository.

Author
Student ID: 121434672
Course: EEX5362 - Mini Project
