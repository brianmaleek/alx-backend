import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the code to verify your account',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData)
  .save((error) => {
    if (!error) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Event listener for successful completion of the job
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
