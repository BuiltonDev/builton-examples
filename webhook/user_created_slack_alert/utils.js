const crypto = require('crypto');

// Headers are case insensitive, they may be automatically modified depending on the server you're using
const getHeader = (headers, key) => {
    const trueKey = Object.keys(headers).find(k => k.toLowerCase() === key.toLowerCase());
    return headers[trueKey];
}

module.exports.isPing = (event) => {
	const webhookType = getHeader(event.headers, 'x-builton-webhook-type');
    if (webhookType && webhookType === 'WebhookConfirmation') {
    console.log('pong');
        return true;
    }
    return false;
}

module.exports.verifySecret = (event) => {
    const signature = getHeader(event.headers, 'x-builton-webhook-signature');
    if (!signature) {
        return false;
    }
    const generatedSignature = crypto.createHmac('sha256', process.env.webhookSecret).update(event.body).digest('hex');
    if (generatedSignature === signature) {
        return true;
    }
    return false;
}
