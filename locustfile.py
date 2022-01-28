import time
from locust import HttpUser, task, between
import csv

file = "passwords.csv"

data = csv.reader(open(file), delimiter=",")
details = list(data)

# print(details.pop(0))
# print(len(details))


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def register(self):
        response = self.client.get("/register/")
        self.csrftoken = response.cookies["csrftoken"]

        self.userdata = details.pop(0)
        id = "0" + str(self.userdata[0][-3:])
        self.client.post(
            "/register/",
            {
                "firstName": "john",
                "lastName": "doe",
                "username": self.userdata[0],
                "email": "me@me.com",
                "bitsid": f"2019A7PS{id}P",
                "contact": f"982579{id}",
                "description": "KODER",
            },
            headers={"X-CSRFToken": self.csrftoken},
        )

    def login(self):
        response = self.client.get("/login/")
        self.csrftoken = response.cookies["csrftoken"]

        self.client.post(
            "/login/",
            {"username": self.userdata[0], "password": self.userdata[1]},
            headers={"X-CSRFToken": self.csrftoken},
        )

    def on_start(self):
        self.register()
        self.login()

    @task
    def workflow(self):
        self.client.get(f"/ques_detail_mcq/{self.userdata[0]}")

    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    # def on_start(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})
