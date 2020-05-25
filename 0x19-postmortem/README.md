# Postmortem

## Issue Summary

At 8:22am PT on March 25 2020, we had an outage of 16 minutes on the **Hello Holberton** page. Had a Docker container started, when I curl the port 8080 mapped to the Docker container port 80, it does not returned a page, instead, it was returning an error message as shown below:

```
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```

## Timeline

**8:22am PT**: After starting the Docker container, and doing *curl 0:8080*, it was returning an empty reply from the server.

**8:24am PT**: First, I started reviewing the status of all the services running on the container to check everything was OK up and running.

**8:33am PT**: After checking, the Apache server wasn't running so we had to start it.

**8:36am PT**: We proceed to create a Bash script to start the Apache server *sudo service apache2 start*.

**8:38am PT**: Finally, the Apache server is running and returning the expected result **Hello Holberton** when doing the *curl 0:8080*.

## Root cause and resolution

The root cause of the problem, was that the Apache server wasn't running on the container. To solve the problem, my team and I created the following Bash script to start the Apache service on the container. 

```bash
#!/usr/bin/env bash
# Debugging Apache on container. Solution in script
sudo service apache2 start
```

Afterwards, when I curl the page again, it was fully running and returning the expected message:
```
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
```

## Corrective and preventative measures

To prevent this type of inconvenients, we are creating a Bash script that has to be runned everytime we initialize a Docker container with the basics steps that has to be done including: Starting the Apache/Nginx service, Starting the MYSQL service, amoung others that have to be done again and again on every container.
Also, every page has to be tested after each configuration, update or change made on containers or servers.
