import numpy as np 
import math

class Process:
    def __init__(self, drift, volatility, delta_t, initial_price):
        self.drift = drift
        self.volatility = volatility
        self.delta_t = delta_t
        self.current_price = initial_price
        self.asset_price = [initial_price] 

    def time_step(self):
        dw = np.random.normal(0, math.sqrt(self.delta_t))
        ds = self.drift * self.delta_t * self.current_price + self.volatility * self.current_price * dw
        self.current_price += ds
        self.asset_price.append(self.current_price)


class Stock:
    def __init__(self, strike):
        self.strike = strike


class CallSim:
    def __init__(self, call, n_options, initial_asset_price, drift, delta_t, volatility, tte, rfr):
        stochastic_processes = []
        for _ in range(n_options):
            stochastic_processes.append(Process(drift, volatility, delta_t, initial_asset_price))

        n_steps = int(tte / delta_t)

        for stochastic_process in stochastic_processes:
            for _ in range(n_steps):
                stochastic_process.time_step()

        payoffs = []
        for stochastic_process in stochastic_processes:
            payoff = stochastic_process.asset_price[-1] - call.strike
            payoffs.append(max(payoff, 0))

        self.price = np.average(payoffs) * math.exp(-tte * rfr)


# Example usage
print(CallSim(Stock(50), 10000, 110.15, 0.08, 1/365, 5.0117, 3/365, 0.08).price)
