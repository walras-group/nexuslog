import nexuslog as logging
import time


class A:
    log = logging.getLogger()

class B:
    log = logging.getLogger()

def main():
    a = A()
    b = B()

    for i in range(16):
        a.log.info(f"Message {i} from A")
        b.log.debug(f"Message {i} from B")

    # logging.shutdown()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, unix_ts=False, filename='tmp/app.log')

    main()
