# from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()

print(service.add_user(name="Ermeson", job="Analista"))
print(service.remove_user(name="Ermeson"))
print(service.search_user(name="Ermeson"))




