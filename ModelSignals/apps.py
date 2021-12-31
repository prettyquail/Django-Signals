from django.apps import AppConfig
from django.core.signals import request_started, request_finished


class ModelsignalsConfig(AppConfig):
    name = "ModelSignals"

    def ready(self):
        import ModelSignals.signals
        request_started.connect(self.print_started)
        request_finished.connect(self.print_finished)

    def print_started(self, sender, **kwargs):
        print("got request")

    def print_finished(self, sender, **kwargs):
        print("finished request")
