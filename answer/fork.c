#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
    pid_t pid;

    pid = fork();
    if (pid == 0){
        execlp("ls", "ls", "-lt", (char *)NULL); //child process
        perror("execlp failed");
    	exit(1);   
     }
     else if (pid < 0) {
        perror("Fork failed.");
   	exit(1);
    }
    wait(NULL); //waits for child to finish
    printf("Child process is done\n");

    return 0;
}

