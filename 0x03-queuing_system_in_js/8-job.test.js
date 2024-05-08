import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;
const testQueue = kue.createQueue();

// Set up kue test mode before running test
before((done) => {
    testQueue.testMode.enter();
    done();
});

// Clean up the test after running tests
after((done) => {
    testQueue.testMode.clear();
    testQueue.testMode.exit();
});

describe('createPushNotificationJobs', () => {
    it('should display an error message if job not an array', () => {
        const invalidJobs = 'This is not an array';

        // Assert
        expect(() => createPushNotificationsJobs(invalidJobs, testQueue)).to.throw('Jobs is not an array');
    });
    it('should create new jobs in the queue', () => {
        // Arrange
        const validJobs = [
            { title: 'Job 1', data: { /* job data */ } },
            { title: 'Job 2', data: { /* job data */ } },
        ]
        // Act
        createPushNotificationsJobs(invalidJobs, testQueue);

        // Asset
        // use kue test mode to check the jobs in the queue
        const job = testQueue.testMode.jobs;
        expect(jobs).to.have.lengthOf(2); // Ensure two job were added
        expect(job[0].type).to.equal(''); // Check the job type
        expect(job[1].type).to.equal('');
    });
})