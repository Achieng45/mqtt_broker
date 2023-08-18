

const mqtt = require('mqtt');

const brokerUrl = '0c8e979e14d842cabf744cca3da9217d.s2.eu.hivemq.cloud'; 
const topic = 'ip_address_response';

const client = mqtt.connect(brokerUrl,8883);

client.on('connect', () => {
  console.log('Connected to MQTT broker');
  client.subscribe(topic, (err) => {
    if (!err) {
      console.log(`Subscribed to topic: ${topic}`);
    }
  });
});

client.on('message', (receivedTopic, message) => {
  if (receivedTopic === topic) {
    console.log(`Received message on topic '${topic}': ${message}`);
  }
});

client.on('error', (error) => {
  console.error('Error:', error);
});