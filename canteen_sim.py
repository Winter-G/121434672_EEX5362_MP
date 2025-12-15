import simpy
import random
import statistics

# -------------------------
# PARAMETERS
# -------------------------
SIM_TIME = 120          # minutes
MEAN_SERVICE = 3        # minutes
ARRIVAL_RATE = 0.5      # customers per minute
PEAK_MULTIPLIER = 1.8   # used for 30-minute surge
NUM_SERVERS = 3

# -------------------------
# DATA COLLECTION
# -------------------------
event_log = []  # full table

def customer(env, name, server):
    arrival = env.now
    with server.request() as req:
        yield req

        start = env.now
        wait = start - arrival

        service_time = random.expovariate(1 / MEAN_SERVICE)
        yield env.timeout(service_time)

        end = env.now

        # store row
        event_log.append([
            name, 
            round(arrival, 2),
            round(start, 2),
            round(end, 2),
            round(wait, 2)
        ])

def arrival_process(env, server):
    i = 0
    while True:
        # time-based arrival rate
        if 30 <= env.now <= 60:
            lam = ARRIVAL_RATE * PEAK_MULTIPLIER
        else:
            lam = ARRIVAL_RATE
        
        inter_arrival = random.expovariate(lam)
        yield env.timeout(inter_arrival)

        i += 1
        env.process(customer(env, f"C{i}", server))

# -------------------------
# SIMULATION RUN
# -------------------------
env = simpy.Environment()
server = simpy.Resource(env, capacity=NUM_SERVERS)
env.process(arrival_process(env, server))
env.run(until=SIM_TIME)

# -------------------------
# PRINT RESULTS
# -------------------------
wait_times = [row[4] for row in event_log]

print("\n------ Event Log (Sample) ------")
print("Cust | Arrive | Start | End | Wait")
for row in event_log[:10]:     # first 10 customers
    print(row)

print("\n------ Statistics ------")
print("Total Customers Served:", len(event_log))
print("Average Waiting Time:", statistics.mean(wait_times))
print("90th Percentile:", statistics.quantiles(wait_times, n=10)[8])

