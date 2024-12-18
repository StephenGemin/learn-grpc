# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import helloworld2_pb2 as helloworld2__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in helloworld2_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HealthyRecipeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Breakfast = channel.unary_unary(
                '/helloworld2.HealthyRecipe/Breakfast',
                request_serializer=helloworld2__pb2.RecipeRequest.SerializeToString,
                response_deserializer=helloworld2__pb2.Recipe.FromString,
                _registered_method=True)
        self.Dinner = channel.unary_unary(
                '/helloworld2.HealthyRecipe/Dinner',
                request_serializer=helloworld2__pb2.RecipeRequest.SerializeToString,
                response_deserializer=helloworld2__pb2.Recipe.FromString,
                _registered_method=True)


class HealthyRecipeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Breakfast(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Dinner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthyRecipeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Breakfast': grpc.unary_unary_rpc_method_handler(
                    servicer.Breakfast,
                    request_deserializer=helloworld2__pb2.RecipeRequest.FromString,
                    response_serializer=helloworld2__pb2.Recipe.SerializeToString,
            ),
            'Dinner': grpc.unary_unary_rpc_method_handler(
                    servicer.Dinner,
                    request_deserializer=helloworld2__pb2.RecipeRequest.FromString,
                    response_serializer=helloworld2__pb2.Recipe.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld2.HealthyRecipe', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('helloworld2.HealthyRecipe', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HealthyRecipe(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Breakfast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/helloworld2.HealthyRecipe/Breakfast',
            helloworld2__pb2.RecipeRequest.SerializeToString,
            helloworld2__pb2.Recipe.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Dinner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/helloworld2.HealthyRecipe/Dinner',
            helloworld2__pb2.RecipeRequest.SerializeToString,
            helloworld2__pb2.Recipe.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class WhatIsTheTimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Now = channel.unary_unary(
                '/helloworld2.WhatIsTheTime/Now',
                request_serializer=helloworld2__pb2.TimeRequest.SerializeToString,
                response_deserializer=helloworld2__pb2.TimeStampReply.FromString,
                _registered_method=True)


class WhatIsTheTimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Now(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WhatIsTheTimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Now': grpc.unary_unary_rpc_method_handler(
                    servicer.Now,
                    request_deserializer=helloworld2__pb2.TimeRequest.FromString,
                    response_serializer=helloworld2__pb2.TimeStampReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld2.WhatIsTheTime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('helloworld2.WhatIsTheTime', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WhatIsTheTime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Now(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/helloworld2.WhatIsTheTime/Now',
            helloworld2__pb2.TimeRequest.SerializeToString,
            helloworld2__pb2.TimeStampReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
