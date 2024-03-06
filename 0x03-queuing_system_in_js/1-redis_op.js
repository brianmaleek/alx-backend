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

// Function to set a new school in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value of a school
function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
    if (error) {
      console.error(`Error retrieving value for ${schoolName}: ${error}`);
    } else {
      console.log(value);
    }
  });
}

// Calling functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
