/**
 * Create push notification jobs.
 * @param {Array} jobs Array of job objects.
 * @param {Queue} queue Kue queue instance.
 */
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData)
      .save((error) => {
        if (!error) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

// Example usage:
// const jobs = [/* array of job objects */];
// const queue = kue.createQueue();
// createPushNotificationsJobs(jobs, queue);

export default createPushNotificationsJobs;
