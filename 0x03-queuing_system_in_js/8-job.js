function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw Error('Jobs is not an array');
    }
    for (let jobData of jobs) {
        let job = queue.create('push_notification_code_3', jobData);
        job
          .on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
          })
          .on('failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error}`);
          })
          .on('progress', (progress, data) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
          })
          .save((error) => {
            if (!error) {
                console.log(`Notifcation job created: ${job.id}`);
            }
          });
    }
}

module.exports = createPushNotificationsJobs;
