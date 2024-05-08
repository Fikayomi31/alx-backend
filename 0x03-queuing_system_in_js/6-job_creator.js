import { createQueue } from 'kue';

const queue = createQueue();

// Define the job data object
const data = {
  phoneNumber: '34567542323',
  message: 'This is the notification message to verify your account',
}

//
const job = queue.create('push_notification_code', data)

// Event to handler job save
job.save(function (error) {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Event to handle job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () =>  {
  console.log('Notification job failed');
});
