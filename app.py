#!/usr/bin/env python3
import os

import aws_cdk as cdk

from backend.backend_pipeline import BackendCodepipelineStack


app = cdk.App()

BackendCodepipelineStack(app, "BackendCodepipelineStack")

app.synth()
