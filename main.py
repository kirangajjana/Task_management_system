from src.services import Task_service
from src.services import UserService


data=Task_service()
data.create_task(123,"kirangajjana","hey kiran gajjana how are you")
print(data.complete_task())
print(data.get_task_history())