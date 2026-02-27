from prioritizer import Notification, NotificationEngine

def demo():
    engine = NotificationEngine()

    engine.add_notification(Notification("Server Down Alert", "High", "System"))
    engine.add_notification(Notification("New Message from John", "Medium", "Message"))
    engine.add_notification(Notification("New Like on Your Post", "Low", "Social"))
    engine.add_notification(Notification("Security Login Attempt", "High", "Security"))

    sorted_notifications = engine.get_sorted_notifications()

    print("=== Sorted Notifications by Priority ===")
    for notification in sorted_notifications:
        print(notification)


if __name__ == "__main__":
    demo()
