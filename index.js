const express = require('express');
const AWS = require('aws-sdk');
const path = require('path');

const app = express();
const s3 = new AWS.S3();

// Configure AWS SDK with your credentials (if not using environment variables)
AWS.config.update({
  accessKeyId: 'YOUR_ACCESS_KEY_ID', // Replace with your AWS access key
  secretAccessKey: 'YOUR_SECRET_ACCESS_KEY', // Replace with your AWS secret key
  region: 'YOUR_REGION', // Replace with your AWS region (e.g., 'us-east-1')
});

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to generate a signed URL for the video
app.get('/video', (req, res) => {
  const params = {
    Bucket: 'your-bucket-name', // Replace with your S3 bucket name
    Key: 'videos/sample.mp4', // Replace with the path to your video file in S3
    Expires: 3600, // URL expires in 1 hour
  };

  // Generate a signed URL
  const signedUrl = s3.getSignedUrl('getObject', params);
  res.json({ url: signedUrl });
});

// Serve the HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
