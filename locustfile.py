from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 1)

    @task
    def dependent_service_1(self):
        self.client.get("/dependent-service-1")