const crypto = require('crypto');

module.exports.checkSecret = (event) => {
    const signature = event.headers['X-Share-Webhook-Signature'];
    const generatedSignature = crypto.createHmac('sha256', process.env.webhookSecret).update(event.body).digest('hex');
    if (generatedSignature === signature) {
        return true;
    }
    return false;
}
