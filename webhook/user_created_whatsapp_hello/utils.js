const crypto = require('crypto');
const twilio = require('twilio');

module.exports.checkSecret = (event) => {
    const signature = event.headers['X-Share-Webhook-Signature'];
    const generatedSignature = crypto.createHmac('sha256', process.env.webhookSecret).update(event.body).digest('hex');
    if (generatedSignature === signature) {
        return true;
    }
    return false;
}

module.exports.getTwillio = () => {
    const accountSid = process.env.twilioAccountSid;
    const authToken = process.env.twilioAuthToken;
    return require('twilio')(accountSid, authToken);
}
