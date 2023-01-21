# -*- coding: utf-8 -*-
from aws_cdk import Stack, pipelines
from constructs import Construct

from backend.backend_deploy_stage import  BackendDeployStage


class BackendCodepipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.codepipeline = pipelines.CodePipeline(
            self,
            'backend_codepipeline',
            synth=pipelines.ShellStep(
                'synth',
                input=pipelines.CodePipelineSource.connection(
                    'sleepy0owl/backend',
                    'main',
                    connection_arn='arn:aws:codestar-connections:us-east-1:960351580303:connection/501a36ad-80cb-47b9-83e2-ae4e1b0aa511'
                ),
                install_commands=['pip install -r requirements.txt'],
                commands=[
                    'npx cdk synth',
                ]
            ),
        )

        self.codepipeline.add_stage(
            BackendDeployStage(self, 'dev')
        )
