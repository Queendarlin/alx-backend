import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Connect event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Error event
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school value
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print); // redis.print logs the result
};

// Function to display the school value using async/await
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error: ${err}`);
  }
};

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
