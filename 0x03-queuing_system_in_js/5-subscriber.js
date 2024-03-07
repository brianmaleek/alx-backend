import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Event listener for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Create a channel
const channel = 'holberton school channel';

// Subscribe to the channel
subscriber.subscribe(channel);

// Event listener for incoming messages
subscriber.on('message', (channel, message) => {
  console.log(`Received message on channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
