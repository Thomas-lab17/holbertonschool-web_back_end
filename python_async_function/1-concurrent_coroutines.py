#!/usr/bin/env python3
"""
This module provides a coroutine for spawning multiple
random delay tasks concurrently.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawn wait_random n times concurrently and
    return delays in completion order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
