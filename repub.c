#include <stdbool.h>       // for bool type
#include <stdio.h>         // for printf, etc
#include <stdlib.h>        
#include <unistd.h>        // for fork
#include <string.h>        // for strlen, strcasecmp, etc
#include <ctype.h>
#include <signal.h>        // for signal
#include <sys/types.h>
#include <sys/wait.h>      // for wait, waitpid
#include <errno.h>

#define NUM_FUCK_YOUS 15
#define RECHARGE_TIME 2
#define BOMB_PAYLOAD "twilight.txt"


int main(int argc, char* argv[])
{
  if (argc < 2)
  {
    return 0;
  }
  char* target = argv[1];

  int fds[2];
  pipe(fds);

  pid_t pid = fork();
  if (pid == 0)
  {
    dup2(fds[1], 1);
    close(fds[0]);
    close(fds[1]);
    char* whoArgs[2] = {"who", NULL};
    execvp(whoArgs[0], whoArgs);
  }
  waitpid(pid, NULL, 0);

  bool targetFound = false;

  char buf[101];
  buf[100] = '\0';
  close(fds[1]);
  while(true)
  {
    int numRead = read(fds[0], buf, 100);
    if (numRead <= 0)
      break;
    buf[numRead] = '\0';
    if (strstr(buf, target) != NULL)
    {
      targetFound = true;
      break;
    }
  }
  if (!targetFound)
  {
    printf("0\n");
    return 0;
  }    
  printf("%d\n", (NUM_FUCK_YOUS - 1) * RECHARGE_TIME + 3);
  for (int i = 0; i < NUM_FUCK_YOUS; i++)
  {
    pid = fork();
    if (pid == 0)
    {
      dup2(fileno(fopen(BOMB_PAYLOAD, "r")), 0);
      char* args[3] = {"write", target, NULL};
      execvp(args[0], args);
    }
    waitpid(pid, NULL, 0);
    if (i != NUM_FUCK_YOUS - 1)
      sleep(RECHARGE_TIME);
  }
  return 0;
  
}
