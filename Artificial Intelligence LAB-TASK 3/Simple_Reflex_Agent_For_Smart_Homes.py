# Simple Reflex Agent for Smart Home Temperature Control
#Copyright (c) 2026 Qasim Ashfaq
class SimpleReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp

    def act(self, current_temp):
        if current_temp < self.desired_temp:
            return "Heater ON"
        else:
            return "Heater OFF"


# Practical Example usage
if __name__ == "__main__":
    agent = SimpleReflexAgent(22)
    current_temperature = float(input("Enter current temperature: "))  #This is useful when an agent gets data from a sensor.
    action = agent.act(current_temperature)
    print(f"Current Temperature: {current_temperature}°C, Action: {action}")