
<h3 align="center">Krypto-Backend-Task</h3>
<p align="center">
    A Python-based backend price alert application that triggers an email when the user’s target price is
achieved.
    <br /></p>

### Built With

- [Python](https://www.python.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [MongoDB Atlas](https://www.mongodb.com/)
- [Redis](https://redis.io/)
- [JWT](https://jwt.io/)

### Installation and Prerequisites
1. Clone the repo
    ```sh
     git clone https://github.com/AK0055/Krypto-Backend-Task.git
    ```
2. Python version > 3.6
3. Docker and Docker compose


## Usage
1. Start the application using
```sh
  cd Krypto-Backend-Task
  docker compose up
  ```
2. Navigate to `http://127.0.0.1:8000/alerts/create` and enter an alert price in console to create a new alert

3. Navigate to `http://127.0.0.1:8000/alerts/delete` and enter an alert price in console to delete an alert

4. Navigate to `http://127.0.0.1:8000/alerts/filter` and enter a status filter in console and display the particular alerts with a status: created/ deleted/ triggered

5. Navigate to `http://127.0.0.1:8000/alerts/` to view all alerts processed till this point

6. Navigate to `http://127.0.0.1:8000/trigger` to process all alerts that have been crossed by the current BTC price, trigger an email to the requested email address
 