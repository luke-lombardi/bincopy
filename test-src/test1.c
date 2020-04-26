#include <stdio.h>
#include "hook.h"

int main(int argc, char **argv)
{
    char cmd[255];
    while (1)
    {
        printf("> ");
        scanf("%s\r\n", cmd);
    }
    return 0;
}