#Temperature control using Model Based Reflex Agent with Memory
#Copyright (c) 2026 Qasim Ashfaq
class ModelBased:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.state = None  # Memory to store the last known temperature
#We Can Also Use File Handling to Store The State of The Agent.
#But as we know that most embedded systems have very less memory so we will use Variable to Store The State of The Agent.
    def update_state(self, current_temp):
        self.state = current_temp

    def act(self, current_temp):
        self.update_state(current_temp)
        if self.state < self.desired_temp:
            return "Heater ON"
        else:
            return "Heater OFF"
# Practical Example Usage
if __name__ == "__main__":
    agent = ModelBased(22)
    current_temperature = float(input("Enter current temperature: "))  #This is useful when an agent gets data from a sensor.
    action = agent.act(current_temperature)
    print(f"Current Temperature: {current_temperature}°C, Action: {action}")
