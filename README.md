# Docker/fig Graceful Termination

When issuing the commands
`docker stop`, `fig stop`, or running `fig up-d`, with an already running service, a SIGTERM (15) signal is first sent to the process, if the process does not stop, then a SIGKILL (9) is sent a few (5) seconds later.

The example signal handler code in `src/loop.py` demonstrates how one might handle trapping the SIGTERM signal to terminate our runloop correctly.

The example in `src/loop.sh` does something similar for a bash script.

When running with fig:

    fig build
    fig up -d
    fig logs
    fig up -d
    fig stop

When running with docker:

    docker run --rm -it dockersignal_loop:latest python loop.py
    docker stop <prev container_id>