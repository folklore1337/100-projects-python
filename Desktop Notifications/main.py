import time
from winotify import Notification, audio

toast = Notification(app_id="кот Вася",
                    title="Привет, я котик!",
                    msg="Удачного дня! <3",
                    duration="short",
                    icon=r"C:\Users\Тимофей\Desktop\котик.png")

toast.set_audio(audio.Default, loop=False)

toast.show()