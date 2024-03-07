import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // If phoneNumber is blacklisted, fail the job
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(errorMessage));
  } else {
    // Track progress to 50%
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done(); // Complete the job
  }
}

// Create a queue with concurrency 2
const queue = kue.createQueue({ concurrency: 2 });

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
