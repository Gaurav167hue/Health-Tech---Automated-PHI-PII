from app.database.redis_client import redis_client

DEFAULT_TTL = 300  # 5 menit

class TokenRepository:

    def save(self, token, value, ttl= DEFAULT_TTL):
        redis_client.set(token, value, ex=ttl)

    def save_many(self, mapping, ttl = DEFAULT_TTL):

        for token, value in mapping.items():
            redis_client.set(
                token,
                value,
                ex=ttl
            )

    def get(self, token):
        return redis_client.get(token)

    def get_many(self, tokens):
        mapping = {}
        for token in tokens:
            value = redis_client.get(token)
            if value is not None:
                mapping[token] = value
        return mapping

    def delete(self, token):
        redis_client.delete(token)