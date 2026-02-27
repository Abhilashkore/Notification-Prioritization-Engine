from datetime import datetime

class Notification:
    def __init__(self, message, urgency, n_type, timestamp=None):
        self.message = message
        self.urgency = urgency
        self.n_type = n_type
        self.timestamp = timestamp if timestamp else datetime.now()

    def calculate_priority(self):
        urgency_score = {
            "High": 3,
            "Medium": 2,
            "Low": 1
        }.get(self.urgency, 0)

        type_score = {
            "System": 3,
            "Security": 3,
            "Message": 2,
            "Social": 1
        }.get(self.n_type, 0)

        time_score = 1  # Basic weight for recency (can be expanded)

        return urgency_score * 3 + type_score * 2 + time_score

    def __repr__(self):
        return f"{self.message} | Priority Score: {self.calculate_priority()}"
    

class NotificationEngine:
    def __init__(self):
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

    def get_sorted_notifications(self):
        return sorted(
            self.notifications,
            key=lambda n: n.calculate_priority(),
            reverse=True
        )
