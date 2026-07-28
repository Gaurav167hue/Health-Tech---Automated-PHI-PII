from app.database.redis_client import redis_client

class TokenRepository:

    def save(self, token, value):
        redis_client.set(token, value)

    def save_many(self, mapping):

        for token, value in mapping.items():
            redis_client.set(
                token,
                value
            )

    def get(self, token):
        return redis_client.get(token)

    def delete(self, token):
        redis_client.delete(token)