from locust import HttpUser, task, tag

class LoadTestShortener(HttpUser):
    
    @task
    def test_post_load(self):
        """Insert stress test (POST)"""

        payload = {
            "original_url": "https://www.google.com"
        }
        
        with self.client.post("/url/", data=payload, catch_response=True) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f"Erro: Status {response.status_code}")

