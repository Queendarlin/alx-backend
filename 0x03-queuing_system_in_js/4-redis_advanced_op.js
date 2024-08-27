import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
const hashKey = 'HolbertonSchools';
const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
};

// Store each value in the hash
Object.entries(hashValues).forEach(([field, value]) => {
  client.hset(hashKey, field, value, redis.print);
});

// Display the entire hash
client.hgetall(hashKey, (err, result) => {
  if (err) {
    console.error(`Error fetching hash: ${err}`);
  } else {
    console.log(result); // Display the hash object
  }

  // Close the Redis client
  client.quit();
});
