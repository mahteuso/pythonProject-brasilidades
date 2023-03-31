from datetime import datetime


class DateBr:
    def __init__(self):
        self.register_user = datetime.today()

    def __str__(self):
        return f'User was registered at {self.register_user.hour}:{self.register_user.minute} on {self.day_register()}\n' \
               f'In ' \
               f'{self.register_user.day}/{self.month_register()}/{self.register_user.year}'

    def month_register(self):
        month_list = ["January", "February", "March", "April",
                      "May", "June", "July", "August", "September",
                      "November", "December"
                      ]
        month_register = self.register_user.month
        return month_list[month_register - 1]

    def day_register(self):
        day_lista = ["Monday", "Tuesday", "Wednesday", "Thursday",
                     "Friday", "Saturday", "Sunday"
                     ]
        day_register = self.register_user.weekday()
        return day_lista[day_register - 1]


user = DateBr()
print(user)
