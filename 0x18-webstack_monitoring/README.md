This project is about 0x18. Webstack monitoring
0x18-webstack_monitoring - Once you have an account set up, follow the instructions given on the website to install the Datadog agent.
Sign up for Datadog
Install datadog-agent on web-01
Create an application key
Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.

0x18-webstack_monitoring - Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.
Set up a monitor that checks the number of read requests issued to the device per second.
Set up a monitor that checks the number of write requests issued to the device per second.

2-setup_datadog - Now create a dashboard with different metrics displayed in order to get a few different visualizations.
Create a new dashboard
Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API
