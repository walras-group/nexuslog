# NexusLog

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue)
![Version](https://img.shields.io/pypi/v/nexuslog?color=blue)

High-performance async logging library, compatible with Python standard logging API.

[中文文档](README_CN.md)

## Benchmark

```
Benchmarking with 1,000,000 log messages

------------------------------------------------------------
Logger               Time (s)     Msgs/sec        Log size    
------------------------------------------------------------
Python logging       5.157        193,896         81,888,890 bytes
picologging          1.893        528,323         78,888,882 bytes
NexusLogger          0.135        7,426,915       97,888,890 bytes
NexusLogger unix_ts  0.130        7,707,092       82,888,890 bytes
------------------------------------------------------------

NexusLogger is 38.30x faster than Python logging
NexusLogger is 14.06x faster than picologging
NexusLogger unix_ts is 39.75x faster than Python logging
NexusLogger unix_ts is 14.59x faster than picologging
```

## Installation

```bash
pip install nexuslog
```

## Quick Start

```python
import nexuslog as logging

logging.basicConfig(level=logging.INFO)

logging.info("Hello, world!")
logging.warning("This is a warning")
logging.error("This is an error")
```

## API

### Log Levels

```python
logging.TRACE
logging.DEBUG
logging.INFO
logging.WARNING
logging.ERROR
```

### Module-level Functions

```python
logging.basicConfig(filename=None, level=logging.INFO, unix_ts=False)
logging.trace(message)
logging.debug(message)
logging.info(message)
logging.warning(message)
logging.error(message)
```

### Logger Class

```python
from nexuslog import Logger, Level

logger = Logger("myapp", path="/var/log/app", level=Level.Info)
logger.info("message")
logger.shutdown()
```

### getLogger

```python
import nexuslog as logging

logging.basicConfig(filename="/var/log/app.log", level=logging.DEBUG)
logger = logging.getLogger("myapp")
logger.info("message")
```

## License

MIT
