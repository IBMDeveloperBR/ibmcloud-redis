"""
    Python code snippets to work with IBM Redis and the `redis` library.
    The redis driver can be installed using the command: `pip install redis`.
    The openssl package is also a requirement.
    Updated the last time at: 22:04 19/AUG/2019
    # https://github.com/andymccurdy/redis-py
"""

import json
import redis
import base64
from urllib.parse import urlparse


# Copy the IPSQL credentials from the IBM Cloud Web page and save them as a json file, as named below. 
REDIS_JSONFILE = "iredis_credentials.json"
with open(REDIS_JSONFILE) as json_file:
    iredis_cred = json.load(json_file)['connection']['rediss']
connection_string = iredis_cred['composed'][0]
parsed = urlparse(connection_string)

# Build the root certificate file:
with open("rediscert.pem", "w") as rootcert:
    coded_cert = iredis_cred['certificate']['certificate_base64']
    rootcert.write(base64.b64decode(coded_cert).decode('utf-8'))


print("\nConnecting to IBM Cloud Redis...")
try:
    ### Authenticate and connect to the Redis database.
    # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
    # using the default encoding utf-8.
    iredis = redis.StrictRedis(
        host=parsed.hostname,
        port=parsed.port,
        password=parsed.password,
        ssl=True,
        ssl_ca_certs='rediscert.pem',
        decode_responses=True
    )
    print("\nConnected successfully to IBM Cloud Redis.")

    # Set the hello message in Redis
    iredis.set("msg:hello", "Hello Redis!!!")

    # Retrieve the hello message from Redis
    msg = iredis.get("msg:hello")
    print("\nRetrieved message: {}".format(msg))
except Exception as error:
    print("\nException: {}".format(error))
finally:
    pass
