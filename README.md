# My-First-Honeypot
## Intro
During the setup of my VPS/portfolio, I encountered an issue while trying to make a read-only user. This prompted me to check the logs on my server, and to my surprise, I saw countless bots trying to brute-force my root access. That's when the idea of my first honeypot came to mind. After doing some research, I knew Cowrie was exactly the tool I needed to make this work. This is a documentation of my first honeypot setup using Cowrie and how I implemented it on my server's dashboard for display.
## Documentation 
Before starting the installation, I checked my RAM usage to see how close I was to my 1GB cap. Noticing I didn't have much memory available, I did some research on how to optimize my server and free up resources.

<img width="589" height="73" alt="image" src="https://github.com/user-attachments/assets/ccc9b81d-607b-41e4-ad4d-4cb8c9970381" />

First, I uninstalled the `snapd` package.

<img width="671" height="19" alt="image" src="https://github.com/user-attachments/assets/d008917b-7bc4-4470-8669-10c32e5392d6" />



<img width="454" height="17" alt="image" src="https://github.com/user-attachments/assets/9d528309-6bb1-47c5-b627-4efd7ab6faa8" />



<img width="456" height="24" alt="image" src="https://github.com/user-attachments/assets/c95b70d8-0ca3-4960-b466-7913bb5e70bb" />

Next, I disabled the `multipathd` service.

<img width="736" height="19" alt="image" src="https://github.com/user-attachments/assets/ffb478ce-8e45-4478-b386-a2344ba1efb2" />

Last but not least, I used `nano` to edit the Nginx configuration, changing `worker_processes` from `auto` to `1`.

<img width="587" height="84" alt="image" src="https://github.com/user-attachments/assets/8450dea4-e1bb-4ca9-bbfb-389b7580bee3" />

After freeing up resources, I opened port 2222 on my UFW firewall and updated my SSH configuration to change the default listening port.

<img width="443" height="19" alt="image" src="https://github.com/user-attachments/assets/99da227f-aa44-4648-8732-79280e3a8400" />

<img width="216" height="84" alt="image" src="https://github.com/user-attachments/assets/bd407c01-0bc7-4a79-b90f-74a7993ad88a" />

Next, I installed the necessary dependencies for Cowrie and created an isolated Python virtual environment for it to run in.

<img width="1075" height="16" alt="image" src="https://github.com/user-attachments/assets/ad5338f5-059c-4d2e-9670-6965704bf1f4" />




<img width="561" height="20" alt="image" src="https://github.com/user-attachments/assets/ecf3dcca-0b52-41b9-b999-9f2003707005" />




<img width="402" height="35" alt="image" src="https://github.com/user-attachments/assets/926b3e37-29fd-4d1b-94a9-726bb16be60d" />




<img width="596" height="135" alt="image" src="https://github.com/user-attachments/assets/26851c04-a906-4a6c-b115-17021749c160" />




<img width="476" height="52" alt="image" src="https://github.com/user-attachments/assets/4d70fbc9-bc19-46de-a5cc-0a41dbe3e909" />

Then, I installed the required Python packages and used `nano` to create a `cowrie.cfg` file, setting the honeypot to listen on port 2223.

<img width="529" height="18" alt="image" src="https://github.com/user-attachments/assets/ccedf459-266e-4e3f-bdde-f8e94e9ff904" />

<img width="565" height="19" alt="image" src="https://github.com/user-attachments/assets/a7818219-8b7d-454f-9e62-2c42deab0c9f" />

<img width="329" height="56" alt="image" src="https://github.com/user-attachments/assets/05ef047c-7905-49f7-9d7b-1e2f3d37b334" />

After configuring the port, I tried to start Cowrie from the `bin` folder, but the command wasn't recognized.

<img width="478" height="33" alt="image" src="https://github.com/user-attachments/assets/b5dd1802-eefb-4e34-8c63-d982421a87d9" />

I inspected the Cowrie directory and found that the executable wasn't in the `bin` folder as expected. I then tried running the `make start` command and got the following error:

<img width="658" height="65" alt="image" src="https://github.com/user-attachments/assets/17622d8e-9884-4d9a-9751-1848dd5c53ff" />

I installed the missing `setuptools_scm` package and tried running Cowrie again. This time, it started successfully!

<img width="528" height="18" alt="image" src="https://github.com/user-attachments/assets/652efd28-2e3b-44a7-909a-4ed511b92b6c" />

<img width="825" height="87" alt="image" src="https://github.com/user-attachments/assets/29e51e28-618e-453b-acd9-ac3a616a6f2a" />

After that I made a simple python script that extracts data from my cowrie log file, I tested it and everything worked fine. Then I configured crontab to automate the script.

<img width="556" height="210" alt="image" src="https://github.com/user-attachments/assets/9db54cdb-1ed4-4aaf-a97b-6a878b5c71b0" />

<img width="528" height="37" alt="image" src="https://github.com/user-attachments/assets/4994fd41-c3e0-485f-8035-415c1d53ed61" />

Lastly, I embedded the honeypot data directly into my site's index to create a live dashboard.

<img width="731" height="425" alt="image" src="https://github.com/user-attachments/assets/bdfa9334-b57b-48c3-9831-d6c1a323ab8c" />

## Ending Notes
This was a fun little project but I still plan on expanding it more in the future with more features such as:

- **Tracking the Attackers:** I want to run some automated lookups on the captured IPs to see where in the world these bots are actually coming from.
    
- **Catching Malware:** A lot of these scripts try to download malicious files once they think they're in. I’d love to start isolating and analyzing those payloads.

