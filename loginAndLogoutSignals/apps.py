from django.apps import AppConfig


class LoginandlogoutsignalsConfig(AppConfig):
    name = "loginAndLogoutSignals"

    def ready(self):
        import loginAndLogoutSignals.signals
