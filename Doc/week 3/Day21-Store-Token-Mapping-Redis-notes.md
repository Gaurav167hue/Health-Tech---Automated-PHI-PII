Today, I will write code for token mapping using a Redis server running in Docker.

First, start the Redis server in Docker using the command `docker start` or `docker run -d --name 'container' -p 'local':'dockerhub' redis`.
Second, launch FastAPI by typing `python -m uvicorn app.main:app --reload`.
Third, use `redis-cli`; since I am using Docker, simply type `docker exec -it 'container' redis-cli`.

In the code for storing token mappings, simply import the `redis` module and use the `set` function to save data to the Redis server while the FastAPI application is running, while also specifying a duration for how long the data should persist.

Redis server commands include `KEYS *` to display stored keys, `PING` to check if the server is active, `SET` to store data, and `GET` to retrieve data based on a key (if `GET` returns `(NIL)`, the data does not exist). Additionally, there is `DEL` to delete data based on a key, `TTL` to check the remaining time-to-live for data in seconds (if `TTL 'key'` returns `-1`, the key is permanent; if `-2`, the data does not exist), and `EXPIRE 'key' 'seconds'` to set the data to be automatically deleted after a specific period.
