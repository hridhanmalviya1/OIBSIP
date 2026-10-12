
import socket
import threading

# Default configuration
HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


# ---------- SERVER FUNCTIONS ----------

def broadcast(message, sender_socket, clients):
    """Send a message to all clients except the sender."""
    for client in list(clients):
        if client != sender_socket:
            try:
                client.sendall(message.encode("utf-8"))
            except (ConnectionResetError, BrokenPipeError, OSError):
                if client in clients:
                    clients.remove(client)
                try:
                    client.close()
                except OSError:
                    pass


def handle_client(client_socket, client_address, clients):
    """Receive messages from one client and broadcast them."""
    username = "Anonymous"

    try:
        username = client_socket.recv(BUFFER_SIZE).decode("utf-8").strip()
        if not username:
            username = "Anonymous"

        join_msg = f"[SERVER] {username} has joined the chat."
        print(join_msg)
        broadcast(join_msg, client_socket, clients)

        while True:
            message = client_socket.recv(BUFFER_SIZE).decode("utf-8")

            if not message:
                break

            formatted_msg = f"[{username}] {message}"
            print(formatted_msg)
            broadcast(formatted_msg, client_socket, clients)

    except (ConnectionResetError, BrokenPipeError, OSError):
        pass
    finally:
        if client_socket in clients:
            clients.remove(client_socket)

        client_socket.close()

        leave_msg = f"[SERVER] {username} has left the chat."
        print(leave_msg)
        broadcast(leave_msg, None, clients)


def run_server():
    """Initialize and run the chat server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    clients = []

    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"=== Chat Server Running on {HOST}:{PORT} ===")
        print("Press Ctrl+C to stop the server.")

        while True:
            client_socket, client_address = server.accept()
            clients.append(client_socket)

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address, clients),
                daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down server.")
    except OSError as error:
        print(f"[ERROR] Server error: {error}")
    finally:
        for client in list(clients):
            try:
                client.close()
            except OSError:
                pass
        server.close()


# ---------- CLIENT FUNCTIONS ----------

def run_messages(sock):
    """Listen for incoming messages in the background."""
    while True:
        try:
            message = sock.recv(BUFFER_SIZE).decode("utf-8")
            if not message:
                print("\n[SERVER] Connection closed.")
                break

            print(f"\n{message}\nYou: ", end="", flush=True)

        except (ConnectionResetError, OSError):
            break


def run_client():
    """Initialize and run a chat client."""
    username = input("Enter your username: ").strip()
    if not username:
        username = "Anonymous"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(username.encode("utf-8"))
    except OSError as error:
        print(f"[ERROR] Could not connect to {HOST}:{PORT}: {error}")
        client_socket.close()
        return

    print(f"=== Connected to Chat Room as {username} ===")
    print("Type messages and press Enter. Type 'quit' to leave.")

    recv_thread = threading.Thread(
        target=run_messages,
        args=(client_socket,),
        daemon=True
    )
    recv_thread.start()

    try:
        while True:
            msg = input("You: ")

            if msg.lower().strip() == "quit":
                break

            if msg.strip():
                client_socket.sendall(msg.encode("utf-8"))

    except (KeyboardInterrupt, OSError):
        pass
    finally:
        client_socket.close()
        print("\nDisconnected from server.")


# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    print("=== Terminal Chat App ===")
    print("1. Start Server")
    print("2. Join as Client")

    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        run_server()
    elif choice == "2":
        run_client()
    else:
        print("Invalid choice. Exiting.")