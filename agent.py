import time

class AirdropTrackerAgent:
    def __init__(self):
        self.tasks = []

    def fetch_tasks(self):
        print("Fetching new airdrop tasks...")
        self.tasks = [
            {"name": "Claim Token Airdrop", "status": "pending"},
            {"name": "Complete Social Task", "status": "pending"},
        ]

    def notify_user(self):
        for task in self.tasks:
            if task["status"] == "pending":
                print(f"Reminder: {task['name']} is pending!")

    def run(self):
        print("Agent started.")
        while True:
            self.fetch_tasks()
            self.notify_user()
            time.sleep(60)  # Checks every 60 seconds

if __name__ == "__main__":
    agent = AirdropTrackerAgent()
    agent.run()
