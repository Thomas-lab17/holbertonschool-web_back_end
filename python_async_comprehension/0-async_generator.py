#!/usr/bin/env python3
"""Async generator coroutine that yields 10 random floats between 0 and 10."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop 10 times, wait 1 sec, yield a random float between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
