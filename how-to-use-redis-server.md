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
- If this is your first time running the `docker run` command, Docker will automatically download the official Redis image from Docker Hub.
- After the image has been downloaded, subsequent runs will be significantly faster.
- If the Redis container already exists, use `docker start` instead of `docker run` to avoid creating duplicate containers.
- Ensure the container is running (`docker ps`) before attempting to access the Redis CLI.
