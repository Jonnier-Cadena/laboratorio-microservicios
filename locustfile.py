from locust import HttpUser, task, between

class UsuarioSimulado(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def probar_usuarios(self):
        self.client.get("/usuarios")

    @task
    def probar_productos(self):
        self.client.get("/productos")

    @task
    def probar_pedidos(self):
        self.client.get("/pedidos")
