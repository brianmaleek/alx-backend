import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Keys and values for the hash
const keys = [
  'Portland',
  'Seattle',
  'New York',
  'Bogota',
  'Cali',
  'Paris',
];

const values = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

keys.forEach((data) => client.hset('HolbertonSchools', data, values[data], redis.print));

client.hgetall('HolbertonSchools', (error, value) => {
  if (error) {
    console.error('An error occurred:', error);
  } else {
    console.log(value);
  }
});
