def notify_admin(notification_service, message):
    if not message:
        raise ValueError("Message cannot be empty")
    notification_service.notify("admin", message)
