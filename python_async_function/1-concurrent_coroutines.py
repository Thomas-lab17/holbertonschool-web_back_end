#!/usr/bin/env python3
"""Provides a coroutine for spawning concurrent random delay tasks."""

import asyncio
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Spawn wait_random n times and return delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
