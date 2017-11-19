# myth-poke

## what

Late one night before a CS110 assignment was due, Wes and I got bored of working on the assignment, so we decided to flex our pipe, fork, and dup2 muscles and created a (questionably) fun little C program which takes credentials and a target (SUNet ID) as arguments, and proceeds to search the stanford myth machines for a logged in user match. If the target is found, it bombards their terminal with a given payload txt, our example being twilight.txt

## how

* `who()` - linux command showing who is currently logged in -  https://linux.die.net/man/1/who
* `write()` - linux command which lets you write to a file descriptor (including another logged in user on the machine) - https://linux.die.net/man/2/write
* paramiko - python library automating the remote ssh process - http://www.paramiko.org

The Stanford Myth machines are comprised of a series of computers in the Gates basement. You are not guaranteed to be assigned to the same machine everytime you ssh into the cluster (load balancing..), so to find a user we have to ssh into every machine (paramiko) and check if they've been logged in, using `who()`, to that marticular machine. Through trial and error, we found that machines are labelled from 1-33 (with some specific ones missing or down). Once target has been acquired, we print the payload to their terminal using the magic of `write()`.

## notes

* This was written for FUN NOT EVIL. The myth machines are where CS107 and CS110 students code their precious assignment. This tool is not for harassing students near assignment deadlines.
* This assumes the number of myth machines, it may have changed since this was written.
