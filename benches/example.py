import nexuslog as logging
import time

logging.basicConfig(level=logging.INFO, unix_ts=True)

class A:
    log = logging.getLogger()

class B:
    log = logging.getLogger()

def main():
    a = A()
    b = B()

    for i in range(1000):
        a.log.info(f"Message {i} from A")

    a.log.shutdown()
    b.log.shutdown()

if __name__ == "__main__":
    main()
