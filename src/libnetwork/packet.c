
#include <stdlib.h>
#include <stdio.h>

char *recv_packet(int fd)
{
    static size_t n = 0;
    static char *buffer = NULL;
    static FILE *stream = NULL;

    if (!buffer) {
        if (!(stream = fdopen(fd, "r+")))
            return NULL;
        if (setvbuf(stream, NULL, _IOLBF, 0) != 0)
            return NULL;
        buffer = NULL;
    }
    if (-1 == getline(&buffer, &n, stream))
        return NULL;
    return buffer;
}