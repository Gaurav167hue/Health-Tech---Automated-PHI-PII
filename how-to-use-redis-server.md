## Running Redis Server with Docker

### Prerequisites

Before running Redis, make sure you have **Docker Desktop** installed on your computer.

1. Download and install Docker Desktop:
   - https://docs.docker.com/desktop/
   - Choose the installer that matches your operating system (Windows, macOS, or Linux).

2. Redis runs as a Docker container, so you don't need to install Redis directly on your machine.
   - Redis Docker documentation:
   - https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/

---

## Create and Run a Redis Container

Open your terminal and execute:

```bash
docker run -d --name healthtech -p 6379:6379 redis
```

### Command Explanation

- `-d`
  - Runs the container in detached mode (background).

- `--name healthtech`
  - Sets the container name.
  - You can replace `healthtech` with any name you prefer.

- `-p 6379:6379`
  - Maps the Redis default port from the container to your local machine.

- `redis`
  - The official Redis Docker image.

---

## Useful Docker Commands

### Start Redis

```bash
docker start <container-name>
```

Example:

```bash
docker start healthtech
```

---

### Check Running Containers

```bash
docker ps
```

This command shows all currently running containers.

---

### Stop Redis

```bash
docker stop <container-name>
```

Example:

```bash
docker stop healthtech
```

---

## Access the Redis CLI

After your Redis container is running, you can access the Redis Command Line Interface (CLI) using:

```bash
docker exec -it <container-name> redis-cli
```

Example:

```bash
docker exec -it healthtech redis-cli
```

If the command is successful, you will enter the Redis CLI and see a prompt similar to:

```text
127.0.0.1:6379>
```

You can verify that Redis is working correctly by running:

```bash
PING
```

Expected output:

```text
PONG
```

To exit the Redis CLI, simply type:

```bash
exit
```

---

## Important Notes

- Make sure **Docker Desktop is running** before starting the Redis container.
- If this is your first time running the command, Docker will automatically download the official Redis image.
- After the image has been downloaded once, subsequent runs will be much faster.
- If the container already exists, use `docker start` instead of `docker run` to avoid creating another container.
- Ensure the container is running (`docker ps`) before attempting to access the Redis CLI.
