import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
from google.rpc import error_details_pb2
from grpc_status import rpc_status

logger = logging.getLogger(__name__)


def run():
    logger.info("Sending request to greeter service")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        try:
            response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
            logger.info("Greet success: %s", response.message)
        except grpc.RpcError as e:
            logger.exception("Greet failure")
            status = rpc_status.from_call(e)
            for detail in status.details:
                if detail.Is(error_details_pb2.QuotaFailure.DESCRIPTOR):
                    info = error_details_pb2.QuotaFailure()
                    detail.Unpack(info)
                    logger.error("Quota failure: %s", info)
                else:
                    raise RuntimeError("Unexpected greeting failure") from e


if __name__ == "__main__":
    logging.basicConfig()
    run()
