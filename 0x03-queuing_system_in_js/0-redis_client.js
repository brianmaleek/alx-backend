import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener to monitor the connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener to monitor the error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});
