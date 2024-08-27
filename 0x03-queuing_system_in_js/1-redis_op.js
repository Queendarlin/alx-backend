import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

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

// Function to display the school value
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error: ${err}`);
    } else {
      console.log(reply);
    }
  });
};

// Call functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
