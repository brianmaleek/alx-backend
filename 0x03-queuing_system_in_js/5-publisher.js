import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Event listener for successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
publisher.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

/**
 * Publishes a message to the "holberton school channel" after a specified time.
 * @param {string} message The message to be published.
 * @param {number} time The time delay in milliseconds.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Call publishMessage for different messages with specified time delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
