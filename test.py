import pika

def rabbitmq_alive(
    host="localhost",
    port=5672,
    username="guest",
    password="guest",
    vhost="/",
    timeout=5,
):
    try:
        credentials = pika.PlainCredentials(username, password)
        params = pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host=vhost,
            credentials=credentials,
            socket_timeout=timeout,
            blocked_connection_timeout=timeout,
        )

        connection = pika.BlockingConnection(params)
        connection.close()
        return True

    except pika.exceptions.AMQPError:
        return False

print(rabbitmq_alive())
print(rabbitmq_alive(port=5671))
print(rabbitmq_alive(host="rabbitmq"))
