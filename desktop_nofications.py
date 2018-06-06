import notify2

notify2.init('appname')
n = notify2.Notification("Summary",
                         "Some body text",
                         "notification-message-im"
                        )
n.show()