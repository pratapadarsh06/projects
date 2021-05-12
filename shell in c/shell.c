

#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>




int change_dir(char **args);     //own_commands
int shell_exit(char **args);     //own_commands


void loop();
char *read_line();                  //1 shell func
char **split_line(char *line);      //2 shell func
int execute(char **args);           //3 shell func

int main()
{
  loop();
  return 0;
}


void loop()
{
  char *line;
  char **args;
  int status;

  do {
    printf("SHELL_IN_'C'-$>> ");
    line = read_line();
    args = split_line(line);
    status = execute(args);

    free(line);
    free(args);
  } while (status);
}


/////
char *builtin_str[] = {"change_dir","shell_exit"};
int (*builtin_func[]) (char **) = {&change_dir,&shell_exit};


int num_builtins() 
{
 return sizeof(builtin_str) / sizeof(char *);
}

//cd command
int change_dir(char **args)
{
  if (args[1] == NULL) 
  {
    fprintf(stderr, "lsh: expected argument to \"cd\"\n");
  } 
  else 
  {
    if (chdir(args[1]) != 0)
     {
      perror("lsh");
     }
  }
  return 1;
}

//shell command
int shell_exit(char **args)
{
	char ch;
	printf("IF your want to shutdown to Enter y otherwise n");
	scanf("%c",&ch);
	if(ch==89 || ch==121)
		system("shutdown -P now");
	else
		return 0;
}


//////
int launch(char **args)
{
  pid_t pid;
  int status;

  pid = fork();
  if (pid == 0) {
    // Child process
    if (execvp(args[0], args) == -1) {
      perror("lsh");
    }
    exit(EXIT_FAILURE);
  } else if (pid < 0) {
    // Error forking
    perror("lsh");
  } else {
    // Parent process
    do {
      waitpid(pid, &status, WUNTRACED);
    } while (!WIFEXITED(status) && !WIFSIGNALED(status));
  }
  return 1;
}

/////

//1
char *read_line()
{
  char *line = NULL;
  size_t bufsize = 0; // have getline allocate a buffer for us
  getline(&line, &bufsize, stdin);
  return line;
}


//2
#define TOK_BUFSIZE 64
#define TOK_DELIM " \t\r\n\a"
char **split_line(char *line)
{
  int bufsize = TOK_BUFSIZE, position = 0;
  char **tokens = malloc(bufsize * sizeof(char*));
  char *token, **tokens_backup;

  if (!tokens) {
    fprintf(stderr, "lsh: allocation error\n");
    exit(EXIT_FAILURE);
  }

  token = strtok(line, TOK_DELIM);
  while (token != NULL) {
    tokens[position] = token;
    position++;

    if (position >= bufsize) {
      bufsize += TOK_BUFSIZE;
      tokens_backup = tokens;
      tokens = realloc(tokens, bufsize * sizeof(char*));
      if (!tokens) {
        free(tokens_backup);
        fprintf(stderr, "lsh: allocation error\n");
        exit(EXIT_FAILURE);
      }
    }

    token = strtok(NULL, TOK_DELIM);
  }
  tokens[position] = NULL;
  return tokens;
}


//3
int execute(char **args)
{
  int i;

  if (args[0] == NULL) {
    // An empty command was entered.
    return 1;
  }

  for (i = 0; i < num_builtins(); i++) {
    if (strcmp(args[0], builtin_str[i]) == 0) {
      return (*builtin_func[i])(args);
    }
  }
return launch(args);
}






