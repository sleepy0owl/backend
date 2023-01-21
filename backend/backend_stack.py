from aws_cdk import Stack, RemovalPolicy
from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda_event_sources

class BackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.bucket = s3.Bucket(
            self,
            "backend-bucket",
            removal_policy=RemovalPolicy.DESTROY
        )

        self.function = _lambda.Function(self,
            id="backend-function",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.AssetCode.from_asset('src'),
            handler='main.handler'
        )

        self.function.add_event_source(
            source=aws_lambda_event_sources.S3EventSource(
                bucket=self.bucket,
                events=[s3.EventType.OBJECT_CREATED],
                filters=[s3.NotificationKeyFilter(prefix='files/')]
            )
        )