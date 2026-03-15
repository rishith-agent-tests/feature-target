#!/usr/bin/env python3
"""Entry point. Wire and run accumulator, producer, consumer from src."""

from src.accumulator import accumulator
from src.producer import producer
from src.consumer import consumer

if __name__ == "__main__":
    res_acc = accumulator(0)
    res_prod = producer(res_acc)
    consumer(res_prod)
