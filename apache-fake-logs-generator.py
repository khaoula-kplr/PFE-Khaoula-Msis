import time
import datetime
import random
from faker import Faker

faker = Faker()

response = ["200", "404", "500", "301"]
verb = ["GET", "POST", "DELETE", "PUT"]
resources = [
            "/list", "/wp-content", 
			    "/wp-admin", "/explore", 
            "/search/tag/list",
            "/app/main/posts", 
      	    "/posts/posts/explore", 
            "/apps/cart.jsp?appID="
                ]

ualist = [faker.firefox,
			  faker.chrome, 
		    faker.safari,
			  faker.internet_explorer, 
			  faker.opera]

while True:
    ip = faker.ipv4()
    dt = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S')
    tz = time.strftime('%z')
    vrb = random.choice(verb)
    uri = random.choice(resources)
    if uri.find("apps") > 0:
        uri += str(random.randint(1000, 10000))
    resp = random.choice(response)
    byt = int(random.gauss(5000, 50))
    referer = faker.uri()
    useragent = random.choice(ualist)()

    log_entry = '%s - - [%s %s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (ip, dt, tz, vrb, uri, resp, byt, referer, useragent)

    # You can customize what to do with the log entry here.
    # For example, you can write it to a file, print it, etc.
    with open("apache-logs.log", "a") as file:
        file.write(log_entry)

    # Sleep for a random duration between 1 and 5 seconds
    time.sleep(random.uniform(1, 5))
