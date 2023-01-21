# -*- coding: utf-8 -*-
from aws_cdk import Stage
from constructs import Construct

from backend.backend_stack import BackendStack

class BackendDeployStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.backend = BackendStack(self, 'BackendStack')
