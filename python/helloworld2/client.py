import argparse
import logging
import sys

import grpc
import helloworld2_pb2
import helloworld2_pb2_grpc


def run(tz, recipe):
    with grpc.insecure_channel("localhost:50051") as channel:
        if tz:
            get_current_time(channel)
        if recipe:
            get_recipe(channel, recipe)


def get_recipe(channel, recipe):
    stub = helloworld2_pb2_grpc.HealthyRecipeStub(channel)
    if recipe == "breakfast":
        response = stub.Breakfast(helloworld2_pb2.RecipeRequest())
    elif recipe == "dinner":
        response = stub.Dinner(helloworld2_pb2.RecipeRequest())
    print("Your randomly selected recipe is:")
    print("name: " + response.name + "\ningredients: " + response.ingredients)


def get_current_time(channel):
    stub = helloworld2_pb2_grpc.WhatIsTheTimeStub(channel)
    response = stub.Now(helloworld2_pb2.TimeRequest(timezone="America/New_York"))
    print("Current time: " + response.current_time)


if __name__ == "__main__":
    logging.basicConfig()
    parser = argparse.ArgumentParser(description="Handle recipe and time flags.")
    parser.add_argument(
        "--recipe",
        choices=["breakfast", "dinner"],
        help="Specify the recipe type (e.g., breakfast or dinner).",
    )
    parser.add_argument("-t", action="store_true", help="Get the current time")

    args = parser.parse_args()
    if not args.recipe and not args.t:
        print("No flags provided. Use --recipe <str> or -t")
        sys.exit(1)

    run(args.t, args.recipe)
