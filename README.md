README

# API Monitoring Application

This project consists of two components: a Node.js server and a Python script for monitoring the server's health. 

## Components

### Node.js Server

The Node.js server provides a simple health check endpoint.

#### `server.js`

- **Setup**: Uses Express framework to create an HTTP server.
- **Endpoint**: Defines `/testConnection` which responds with a JSON object `{ status: "OK" }` and an HTTP status code 200.
- **Port**: Listens on port 3000.

#### Running the Server

1. Install dependencies:
   ```
   npm install express
   ```

2. Start the server:
   ```
   node server.js
   ```

### Python Monitoring Script

The Python script monitors the health of the Node.js server and sends notifications if issues are detected.

#### `monitor.py`

- **Configuration**:
  - `API_URL`: URL of the Node.js health check endpoint.
  - `DISCORD_WEBHOOK_URL`: Discord webhook URL to send notifications.
  
- **Functions**:
  - `check_connection()`: Checks the status of the API endpoint and sends a Discord notification if there is an issue.
  - `send_discord_notification(title, description)`: Sends a notification to a Discord channel using the provided webhook URL.

#### Running the Monitor Script

1. Install dependencies:
   ```
   pip install requests
   ```

2. Update the configuration:
   - Replace `http://localhost:3000/testConnection` with the actual URL of your API if different.
   - Replace `https://discordapp.com/api/webhooks/xxxxxxxxxx/yyyyyyyyyyyyyyyyyyy_` with your actual Discord webhook URL.

3. Run the script:
   ```
   python monitor.py
   ```

## Logging

Both the Node.js server and the Python script log their activities:

- **Node.js Server**: Logs a message when the server starts.
- **Python Script**: Logs API status checks and notification sending results.

## Requirements

- **Node.js**: Ensure Node.js and npm are installed for running the server.
- **Python**: Ensure Python and pip are installed for running the monitoring script.
- **Discord Webhook**: Set up a Discord webhook for notifications.

## Troubleshooting

- **Server Not Responding**: Check if the Node.js server is running and accessible at the specified port.
- **Notification Issues**: Verify that the Discord webhook URL is correctly configured and that the webhook has the necessary permissions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the configuration and script according to your needs. If you encounter any issues or have questions, check the logs for detailed information or reach out for support.
