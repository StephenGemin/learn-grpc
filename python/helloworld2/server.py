import logging
import random
from concurrent import futures
from datetime import datetime, timezone

import grpc
import helloworld2_pb2
import helloworld2_pb2_grpc
import pytz
import recipe_resources

BREAKFAST = "breakfast"
DINNER = "dinner"


def get_current_time_in_timezone(request):
    try:
        tz = pytz.timezone(request.timezone)
        current_time = datetime.now(tz)
        return current_time.isoformat(timespec="seconds")
    except pytz.UnknownTimeZoneError:
        return f"Unknown timezone: {timezone}"


class CurrentTime(helloworld2_pb2_grpc.WhatIsTheTimeServicer):
    def Now(self, request, context):
        return helloworld2_pb2.TimeStampReply(
            current_time=get_current_time_in_timezone(request)
        )


class RandomRecipe(helloworld2_pb2_grpc.HealthyRecipeServicer):
    def __init__(self):
        self.db = recipe_resources.read_recipe_db()

    def Breakfast(self, request, context):
        recipe_choice = random.choice(
            [r for r in self.db if r["meal_type"] == BREAKFAST]
        )
        return helloworld2_pb2.Recipe(**recipe_choice)

    def Dinner(self, request, context):
        recipe_choice = random.choice([r for r in self.db if r["meal_type"] == DINNER])
        return helloworld2_pb2.Recipe(**recipe_choice)

    def _meal_by_type(self, meal_type):
        return (r for r in self.db if r["meal_type"] == meal_type)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor())
    helloworld2_pb2_grpc.add_WhatIsTheTimeServicer_to_server(CurrentTime(), server)
    helloworld2_pb2_grpc.add_HealthyRecipeServicer_to_server(RandomRecipe(), server)
    server.add_insecure_port(f"[::]:{port}")
    try:
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass
    finally:
        print("Stopping service")
        server.stop(grace=True)
        print("Service stopped, goodbye")


if __name__ == "__main__":
    logging.basicConfig()
    serve()
